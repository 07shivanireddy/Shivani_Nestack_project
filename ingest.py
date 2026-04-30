import argparse
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


def ingest(file_path):
    print("📄 Loading PDF...")
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    print(f"✅ Loaded {len(documents)} pages")

    print("✂️ Splitting text...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(documents)

    print(f"✅ Created {len(chunks)} chunks")

    print("🧠 Creating embeddings...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("💾 Storing in vector DB...")
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="vectorstore"
    )

    vectordb.persist()
    print("🎉 Ingestion complete!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    args = parser.parse_args()

    ingest(args.file)