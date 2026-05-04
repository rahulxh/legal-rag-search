"""
RAG Engine for Legal Document Search.
Supports: pre-loaded data + PDF upload ingestion.
"""

from typing import List, Dict, Any, Optional
from data.legal_data import LEGAL_DOCUMENTS
from chromadb.utils import embedding_functions
import chromadb
import os
import sys
import re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


COLLECTION_NAME = "legal_knowledge_base"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
TOP_K = 5
CHUNK_SIZE = 500   # characters per chunk when splitting PDFs
CHUNK_OVERLAP = 80


class RAGEngine:
    def __init__(self, persist_directory: str = "./chroma_db"):
        print("⚖️  Initialising Legal RAG Engine...")

        self.ef = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=EMBEDDING_MODEL
        )
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            embedding_function=self.ef,
            metadata={"hnsw:space": "cosine"}
        )

        if self.collection.count() == 0:
            print("Ingesting legal documents...")
            self._ingest_documents()
        else:
            print(
                f"Collection ready with {self.collection.count()} documents.")

    # ── Ingestion ──────────────────────────────────────
    def _ingest_documents(self):
        ids = [d["id"] for d in LEGAL_DOCUMENTS]
        texts = [d["text"] for d in LEGAL_DOCUMENTS]
        metadatas = [d["metadata"] for d in LEGAL_DOCUMENTS]
        self.collection.add(ids=ids, documents=texts, metadatas=metadatas)
        print(f"Ingested {len(LEGAL_DOCUMENTS)} legal documents.")

    def add_documents(self, documents: List[Dict[str, Any]]):
        ids = [d["id"] for d in documents]
        texts = [d["text"] for d in documents]
        metadatas = [d.get("metadata", {}) for d in documents]
        self.collection.add(ids=ids, documents=texts, metadatas=metadatas)

    # ── PDF chunking ───────────────────────────────────
    def chunk_text(self, text: str, doc_id: str,
                   metadata: Optional[Dict] = None) -> List[Dict]:
        """Split a long text into overlapping chunks for better retrieval."""
        text = re.sub(r'\s+', ' ', text).strip()
        chunks = []
        start = 0
        idx = 0
        while start < len(text):
            end = min(start + CHUNK_SIZE, len(text))
            chunk = text[start:end]
            if chunk.strip():
                chunks.append({
                    "id":       f"{doc_id}_chunk_{idx}",
                    "text":     chunk,
                    "metadata": {**(metadata or {}), "chunk_index": idx,
                                 "source_doc": doc_id}
                })
            start += CHUNK_SIZE - CHUNK_OVERLAP
            idx += 1
        return chunks

    # ── Retrieval ──────────────────────────────────────
    def retrieve(self, query: str, top_k: int = TOP_K,
                 language_filter: Optional[str] = None) -> List[Dict]:
        where = {"language": language_filter} if language_filter else None
        results = self.collection.query(
            query_texts=[query],
            n_results=min(top_k, self.collection.count()),
            where=where
        )
        return [
            {
                "text":     results["documents"][0][i],
                "metadata": results["metadatas"][0][i],
                "distance": results["distances"][0][i],
            }
            for i in range(len(results["documents"][0]))
        ]

    def build_context(self, chunks: List[Dict]) -> str:
        parts = []
        for i, c in enumerate(chunks, 1):
            m = c["metadata"]
            act = m.get("act", "")
            sec = m.get("section") or m.get("article", "")
            label = f"{act}{' §'+sec if sec else ''}"
            parts.append(f"[{i}] [{label}]\n{c['text']}")
        return "\n\n".join(parts)

    def stats(self) -> Dict:
        return {
            "total_documents": self.collection.count(),
            "collection_name": COLLECTION_NAME,
            "embedding_model": EMBEDDING_MODEL,
        }
