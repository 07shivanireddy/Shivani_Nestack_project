# PDF Vectorisation Pipeline – Nestack Assessment

## 📌 Overview

This project implements a PDF vectorisation pipeline using LangChain. It includes:

* An **ingestion pipeline** to process PDF documents into embeddings
* A **retrieval API** that performs similarity search and returns relevant text chunks

No LLM or QA chain is used — only direct vector similarity search.

---

## ⚙️ Setup & Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run ingestion

```bash
python ingest.py --file data/document.pdf
```

### 3. Start API server

```bash
uvicorn app:app --reload
```

---

## 🌐 API Usage

**Endpoint:**
POST `/query`

**Request:**

```json
{
  "query": "What is the pipeline about?",
  "top_k": 3
}
```

**Response:**

```json
[
  {
    "chunk_text": "...",
    "page_number": 0,
    "score": 0.2
  }
]
```

---

## 🧠 Design Choices

* **Loader:** PyPDFLoader

  * Efficient and preserves page metadata

* **Splitter:** RecursiveCharacterTextSplitter

  * Chunk size: 500
  * Overlap: 100
  * Maintains context across chunks

* **Embedding Model:** all-MiniLM-L6-v2

  * Lightweight, fast, and good semantic performance

* **Vector Store:** Chroma

  * Simple, persistent, and easy to use locally

---

## ⚠️ Constraints Followed

* No LLM used
* No RetrievalQA or conversational chains
* Direct similarity search only
* Same embedding model used for ingestion and retrieval

---

## 📊 Results

Sample query outputs are provided in `results.json`.

---

## 📁 Project Structure

```
SHIVANI_NESTACK_SUBMISSION/
├── ingest.py
├── app.py
├── requirements.txt
├── README.md
├── results.json
├── data/
│   └── document.pdf
├── vectorstore/
```

---

## 🚀 Deployment

Add your live API link here:

```
https://your-app-url.com
```

---

## 👩‍💻 Author

Shivani Reddy
