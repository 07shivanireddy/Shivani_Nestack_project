from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# ✅ This line is REQUIRED
app = FastAPI()

# Load embedding model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector database
vectordb = Chroma(
    persist_directory="vectorstore",
    embedding_function=embedding
)

# Request format
class QueryRequest(BaseModel):
    query: str
    top_k: int = 3


# API endpoint
@app.post("/query")
def query_docs(request: QueryRequest):
    results = vectordb.similarity_search_with_score(
        request.query,
        k=request.top_k
    )

    output = []
    for doc, score in results:
        output.append({
            "chunk_text": doc.page_content,
            "page_number": doc.metadata.get("page", None),
            "score": float(score)
        })

    return output