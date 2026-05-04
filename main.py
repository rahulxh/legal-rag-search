"""
Legal RAG Search Engine — FastAPI backend.
Endpoints:
  POST /search        — RAG query
  POST /upload-pdf    — Upload & ingest a PDF
  POST /ingest        — Add raw text documents
  GET  /stats         — Collection stats
  GET  /health        — Health check
"""

import os, sys, uuid, httpx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional
from app.rag_engine import RAGEngine

app = FastAPI(title="Legal RAG Search Engine", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])
app.mount("/static", StaticFiles(directory="static"), name="static")

rag = RAGEngine(persist_directory="./chroma_db")

OLLAMA_URL   = "http://localhost:11434/api/chat"
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "phi3")


# ── Schemas ───────────────────────────────────────────
class SearchRequest(BaseModel):
    query: str
    top_k: Optional[int] = 5
    language: Optional[str] = None   # "english" | "hindi" | "malayalam" | None

class SearchResponse(BaseModel):
    query: str
    answer: str
    sources: List[dict]
    total_chunks: int

class IngestDoc(BaseModel):
    id: str
    text: str
    metadata: Optional[dict] = {}

class IngestRequest(BaseModel):
    documents: List[IngestDoc]


# ── LLM ───────────────────────────────────────────────
async def generate_answer(query: str, context: str) -> str:
    prompt = f"""You are an expert Indian legal assistant. You help people understand Indian laws, acts, and legal procedures.
Answer questions using ONLY the legal context provided below.
Be clear, accurate, and explain legal terms in simple language.
Mention the relevant Act/Section/Article when answering.
If the context does not have enough information, say so honestly.
Always add a note: "This is for informational purposes only. Consult a qualified lawyer for legal advice."

Legal Context:
{context}

Question: {query}

Answer:"""

    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                OLLAMA_URL,
                json={
                    "model": OLLAMA_MODEL,
                    "messages": [{"role": "user", "content": prompt}],
                    "stream": False,
                }
            )
            if response.status_code != 200:
                raise HTTPException(status_code=502,
                    detail=f"Ollama error: {response.text}")
            return response.json()["message"]["content"]
    except httpx.ConnectError:
        raise HTTPException(status_code=503,
            detail="Cannot connect to Ollama. Run: ollama serve")


# ── Routes ────────────────────────────────────────────
@app.get("/")
async def root():
    return FileResponse("static/index.html")

@app.get("/health")
async def health():
    try:
        async with httpx.AsyncClient(timeout=3.0) as c:
            r = await c.get("http://localhost:11434")
            ollama = "running" if r.status_code == 200 else "error"
    except Exception:
        ollama = "not running"
    return {"status": "ok", "ollama": ollama, "model": OLLAMA_MODEL}

@app.get("/stats")
async def stats():
    return rag.stats()

@app.post("/search", response_model=SearchResponse)
async def search(req: SearchRequest):
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    chunks  = rag.retrieve(req.query, top_k=req.top_k,
                           language_filter=req.language)
    context = rag.build_context(chunks)
    answer  = await generate_answer(req.query, context)

    sources = [
        {
            "text":      c["text"][:220] + "..." if len(c["text"]) > 220 else c["text"],
            "act":       c["metadata"].get("act", ""),
            "section":   c["metadata"].get("section") or c["metadata"].get("article", ""),
            "language":  c["metadata"].get("language", "english"),
            "category":  c["metadata"].get("category", ""),
            "relevance": round(1 - c["distance"], 3),
        }
        for c in chunks
    ]
    return SearchResponse(query=req.query, answer=answer,
                          sources=sources, total_chunks=rag.collection.count())


@app.post("/upload-pdf")
async def upload_pdf(
    file: UploadFile = File(...),
    language: str    = Form("english"),
    category: str    = Form("uploaded")
):
    """Accept a PDF, extract text with PyMuPDF, chunk and ingest."""
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files accepted.")

    try:
        import fitz   # PyMuPDF
    except ImportError:
        raise HTTPException(status_code=500,
            detail="PyMuPDF not installed. Run: pip install pymupdf")

    data    = await file.read()
    doc_id  = f"pdf_{uuid.uuid4().hex[:8]}"
    text    = ""

    try:
        pdf = fitz.open(stream=data, filetype="pdf")
        for page in pdf:
            text += page.get_text()
        pdf.close()
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Could not read PDF: {e}")

    if not text.strip():
        raise HTTPException(status_code=422,
            detail="PDF appears to be scanned/image-only. Text extraction failed.")

    metadata = {
        "category": category,
        "act":      file.filename.replace(".pdf", ""),
        "language": language,
        "source":   "pdf_upload",
    }
    chunks = rag.chunk_text(text, doc_id, metadata)
    rag.add_documents(chunks)

    return {
        "message":     f"Successfully ingested '{file.filename}'",
        "chunks_added": len(chunks),
        "doc_id":      doc_id,
    }


@app.post("/ingest")
async def ingest(req: IngestRequest):
    docs = [{"id": d.id, "text": d.text, "metadata": d.metadata}
            for d in req.documents]
    rag.add_documents(docs)
    return {"message": f"Ingested {len(docs)} documents."}
