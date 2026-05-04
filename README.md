# ⚖️ Indian Legal RAG Search Engine

> ⚠️ **This project is built for educational purposes only. It is not intended to provide legal advice. Always consult a qualified lawyer for legal matters.**

An intelligent legal document search system built using **Retrieval-Augmented Generation (RAG)** architecture. Ask natural language questions about Indian laws in **English, Hindi, and Malayalam** — powered by a free local AI model with zero API costs.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)
![ChromaDB](https://img.shields.io/badge/ChromaDB-latest-orange)
![Ollama](https://img.shields.io/badge/Ollama-Phi3-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Education](https://img.shields.io/badge/Purpose-Educational%20Only-red)

---

## 📸 What You Can Search

- `What is Article 21?`
- `Punishment for murder under IPC?`
- `How to file an FIR?`
- `What is anticipatory bail?`
- `RTI application process`
- `अनुच्छेद 21 क्या है?` (Hindi)
- `ആർട്ടിക്കിൾ 21 എന്താണ്?` (Malayalam)

---

## 🧠 How It Works

```
User Question
      │
      ▼
[ Embed Query ]  ←  sentence-transformers (local, free)
      │
      ▼
[ ChromaDB ]  ←  cosine similarity → top 5 chunks
      │
      ▼
[ Phi3 via Ollama ]  ←  context + question → answer
      │
      ▼
[ Answer + Sources + Disclaimer ]  →  shown in UI
```

### RAG Pipeline Steps
1. **Ingestion** — Legal text chunks are embedded using `sentence-transformers` and stored in ChromaDB
2. **PDF Upload** — Upload any legal PDF, it gets extracted, chunked, and added to the knowledge base
3. **Retrieval** — Query is embedded and top-5 similar chunks retrieved via cosine similarity
4. **Generation** — Phi3 reads the chunks as context and generates a grounded answer
5. **Response** — Answer shown with source references, relevance scores, and legal disclaimer

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend API | FastAPI (Python) |
| Vector Database | ChromaDB |
| Embeddings | sentence-transformers `all-MiniLM-L6-v2` |
| PDF Parsing | PyMuPDF |
| LLM | Phi3 via Ollama (local, free) |
| Frontend | HTML, CSS, JavaScript |

---

## ✨ Features

- 🔍 Natural language legal search
- 🌐 Multilingual — English, Hindi, Malayalam
- 📄 PDF upload and ingestion from browser
- 🧠 Full RAG pipeline — retrieve then generate
- ⚖️ Covers Constitution, IPC, CrPC, RTI, Consumer Law
- 💾 Persistent vector storage with ChromaDB
- 🆓 100% free — runs entirely on local machine
- ⚠️ Auto legal disclaimer on every answer
- 🎨 Dark legal-themed responsive UI

---

## 📚 Legal Knowledge Covered

| Act | Topics |
|-----|--------|
| Constitution of India | Preamble, Art 14, 19, 21, 32, DPSP, Amendments |
| Indian Penal Code (IPC) | Murder (302), Cheating (420), Rape (375), Defamation (499) |
| CrPC | FIR (154), Bail (436-438), Anticipatory Bail |
| RTI Act 2005 | Application process, exemptions, appeals |
| Consumer Protection Act 2019 | Complaints, commissions, e-commerce |
| All topics | Available in English, Hindi & Malayalam |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- [Ollama](https://ollama.com/download) installed

### 1. Clone the repository
```bash
git clone https://github.com/rahulxh/legal-rag-search.git
cd legal-rag-search
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download Phi3 model
```bash
ollama pull phi3
```

### 4. Start the server
```bash
# Windows (Command Prompt)
set OLLAMA_MODEL=phi3 && python -m uvicorn main:app --port 8000

# Mac/Linux
OLLAMA_MODEL=phi3 uvicorn main:app --port 8000
```

### 5. Open in browser
```
http://127.0.0.1:8000
```

---

## 📁 Project Structure

```
legal-rag-search/
├── main.py              ← FastAPI server & API endpoints
├── requirements.txt     ← Python dependencies
├── app/
│   └── rag_engine.py    ← ChromaDB + embedding + PDF chunking
├── data/
│   └── legal_data.py    ← Pre-loaded Indian legal knowledge
└── static/
    └── index.html       ← Frontend UI
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| `GET` | `/` | Frontend UI |
| `GET` | `/health` | Health check |
| `GET` | `/stats` | Collection stats |
| `POST` | `/search` | RAG search query |
| `POST` | `/upload-pdf` | Upload & ingest PDF |
| `POST` | `/ingest` | Add raw text documents |

### Example — Search
```bash
curl -X POST http://127.0.0.1:8000/search \
  -H "Content-Type: application/json" \
  -d '{"query": "What is Article 21?", "top_k": 5}'
```

### Example — Search in Hindi
```bash
curl -X POST http://127.0.0.1:8000/search \
  -H "Content-Type: application/json" \
  -d '{"query": "अनुच्छेद 21 क्या है?", "language": "hindi"}'
```

---

## ➕ Adding More Legal Data

Open `data/legal_data.py` and add entries:

```python
{
    "id": "unique_id",
    "text": "Your legal text here...",
    "metadata": {
        "category": "constitution",
        "act": "Constitution of India",
        "article": "44",
        "language": "english"
    }
}
```

Delete `chroma_db/` folder and restart to re-ingest.

---

## 📄 Upload PDF

1. Open the app at `http://127.0.0.1:8000`
2. Click **Upload PDF** tab
3. Drag & drop any Indian law PDF
4. Select language and category
5. Click **Upload & Ingest**
6. PDF is chunked and immediately searchable!

---

## 🔄 Switching Models

Change in `main.py`:
```python
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "phi3")
```

| Model | Size | Speed |
|-------|------|-------|
| `phi3` | 2GB | Fast ⚡ |
| `tinyllama` | 600MB | Very Fast ⚡⚡ |
| `llama3` | 4GB | Medium |
| `mistral` | 4GB | Medium |

---

## 📚 What I Learned

- End-to-end RAG pipeline implementation
- Vector embeddings and multilingual semantic search
- PDF text extraction and chunking strategies
- Building REST APIs with FastAPI including file upload
- Running local LLMs with Ollama at zero cost
- Integrating ChromaDB as a persistent vector store

---

## ⚠️ Disclaimer

This project is developed **for educational and learning purposes only**. The information provided by this system does **not constitute legal advice**. The answers generated may be incomplete or inaccurate. For any legal matters, always consult a **qualified and licensed lawyer**. The developer is not responsible for any actions taken based on the information provided by this tool.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgements

- [ChromaDB](https://www.trychroma.com/) — vector database
- [sentence-transformers](https://www.sbert.net/) — embeddings
- [Ollama](https://ollama.com/) — local LLM runner
- [FastAPI](https://fastapi.tiangolo.com/) — backend framework
- [PyMuPDF](https://pymupdf.readthedocs.io/) — PDF parsing
