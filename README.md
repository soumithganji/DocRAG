<div align="center">

#  DocRAG

**AI-Powered Document Q&A Platform using Retrieval-Augmented Generation**

A production-ready platform for intelligent document analysis, leveraging RAG with NVIDIA LLMs, advanced multi-format document ingestion, and hybrid vector databases. Features both an interactive web interface and REST API for real-time document Q&A.

</div>

<div align="center">

[![Python Version](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Framework: FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![Framework: Flask](https://img.shields.io/badge/Frontend-Flask-000000.svg)](https://flask.palletsprojects.com/)
[![LangChain](https://img.shields.io/badge/LangChain-Powered-green.svg)](https://langchain.com/)
[![NVIDIA NIM](https://img.shields.io/badge/NVIDIA-NIM_LLMs-76B900.svg)](https://build.nvidia.com/)

</div>

---

##  Features

- **Multiple AI Models** — Choose from 11+ NVIDIA-hosted LLMs including Qwen, Mistral, Llama, and Gemma models
- **Multi-Format Support** — Upload PDF, DOCX, PPTX, XLSX, TXT files or provide document URLs
- **Hybrid Vector Search** — FAISS for ephemeral storage + Pinecone for production-scale retrieval
- **Smart Caching** — Query caching system with hit rate tracking for optimized performance
- **Context Compression** — NVIDIA Reranker for complex queries with enhanced accuracy
- **Dual Interface** — Flask web UI for users + FastAPI REST API for integrations
- **Performance Monitoring** — Built-in metrics for response time, accuracy, and cache performance

---

##  Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         DocRAG Platform                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐        ┌──────────────┐        ┌────────────┐ │
│  │  Flask Web   │        │   FastAPI    │        │   NVIDIA   │ │
│  │      UI      │───────▶│   REST API   │───────▶│    LLMs    │ │
│  │  (Port 8000) │        │ (/api/v1/run)│        │            │ │
│  └──────────────┘        └──────────────┘        └────────────┘ │
│         │                       │                               │
│         ▼                       ▼                               │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                     RAG Pipeline                         │   │
│  │  ┌─────────┐    ┌──────────┐    ┌───────────────────┐    │   │
│  │  │ Document│───▶│ Chunking │───▶│ NVIDIA Embeddings │    │   │
│  │  │ Loaders │    │ (1000ch) │    │  (nv-embed-v1)    │    │   │
│  │  └─────────┘    └──────────┘    └───────────────────┘    │   │
│  │                                          │               │   │
│  │                       ┌──────────────────┴──────────────┐│   │
│  │                       ▼                                 ▼│   │
│  │               ┌──────────────┐              ┌───────────┐│   │
│  │               │    FAISS     │              │  Pinecone ││   │
│  │               │   (Local)    │              │  (Cloud)  ││   │
│  │               └──────────────┘              └───────────┘│   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

##  Getting Started

### Prerequisites

- Python 3.10+
- [NVIDIA API Key](https://build.nvidia.com/)
- Pinecone account for cloud vector storage
- System libraries for OCR:
  ```bash
  # Ubuntu/Debian
  sudo apt-get install -y tesseract-ocr libtesseract-dev tesseract-ocr-eng
  ```

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/DocRAG.git
cd DocRAG

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory:

```env
# Required
NVIDIA_API_KEY=your_nvidia_api_key_here

# Optional - for API authentication
AUTH_TOKEN=your_secure_auth_token

# Optional - for Pinecone cloud storage
PINECONE_INDEX_NAME=your_pinecone_index
PINECONE_API_KEY=your_pinecone_api_key

# Optional - Flask secret for sessions
FLASK_SECRET=your_flask_secret_key
```

### Running Locally

**Option 1: Web Interface (Flask)**
```bash
python run_flask.py
```
Access at: http://localhost:8000

**Option 2: REST API (FastAPI)**
```bash
python run_api.py
```
- API: http://localhost:8000/api/v1/run
- Docs: http://localhost:8000/docs

---

##  API Usage

### Endpoint: `POST /api/v1/run`

**Headers:**
```
Authorization: Bearer YOUR_AUTH_TOKEN
Content-Type: application/json
```

**Request Body:**
```json
{
  "documents": ["https://example.com/policy.pdf"],
  "questions": [
    "What is the coverage limit?",
    "What are the exclusions?"
  ]
}
```

**Response:**
```json
{
  "answers": [
    "The coverage limit is $500,000 per incident as stated in Section 3.",
    "Exclusions include pre-existing conditions and cosmetic procedures as outlined in Section 7."
  ]
}
```

### Health Check: `GET /health`

Returns performance metrics including average response time, cache hit rate, and request counts.

---

##  Project Structure

```
DocRAG/
├── run_flask.py          # Flask web server entry point
├── run_api.py            # FastAPI server entry point
├── requirements.txt      # Python dependencies
├── apt.txt               # System dependencies (Tesseract OCR)
│
├── app/                  # Application package
│   ├── flask_app.py      # Flask web UI with file upload
│   ├── api.py            # FastAPI REST endpoints
│   └── rag_logic.py      # RAG pipeline with caching
│
├── core/                 # Core utilities
│   ├── db.py             # SQLite logging for auditing
│   └── logger.py         # Performance & request logging
│
├── scripts/              # Utility scripts
│   ├── pinecone_uploader.py  # Bulk upload to Pinecone
│   └── diagram.py        # Architecture diagrams
│
├── static/               # Frontend assets
│   ├── css/style.css     # Styling
│   └── js/main.js        # Client-side JavaScript
│
└── templates/            # HTML templates
    └── index.html        # Main web interface
```

---

##  Supported AI Models

| Provider | Model | Best For |
|----------|-------|----------|
| Qwen | qwen2.5-7b-instruct | Fast, balanced responses |
| Qwen | qwen2.5-coder-32b-instruct | Technical documents |
| Mistral | mistral-small-24b-instruct | General purpose |
| Meta | llama-3.3-70b-instruct | Complex analysis |
| Meta | llama-4-maverick-17b | Latest capabilities |
| NVIDIA | llama-3.3-nemotron-super-49b | High accuracy |
| Google | gemma-3n-e4b-it | Lightweight, fast |

---


##  Tech Stack

| Component | Technology |
|-----------|------------|
| **LLM Provider** | NVIDIA NIM |
| **Embeddings** | NVIDIA nv-embed-v1 |
| **Vector DB** | FAISS (local) / Pinecone (cloud) |
| **RAG Framework** | LangChain |
| **Web Backend** | Flask + FastAPI |
| **Document Parsing** | PyPDF, docx2txt, Unstructured |
| **OCR** | Tesseract |

---
