import hashlib

from app_etl_rag.chunking.text_splitter import split_documents
from app_etl_rag.loaders.pdf_loader import load_all_pdfs
from app_etl_rag.vectorstores.chroma_store import get_vector_store


def generate_chunk_id(chunk) -> str:
    """
    Generate a deterministic ID for each chunk.

    If the document doesn't change, the chunk ID stays the same.
    """

    source = chunk.metadata.get("source_file", "")
    page = chunk.metadata.get("page", 0)
    start = chunk.metadata.get("start_index", 0)

    text = f"{source}:{page}:{start}:{chunk.page_content}"

    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def ingest():

    print("=" * 60)
    print("Loading PDF files...")
    documents = load_all_pdfs() #load document

    print("=" * 60)
    print("Splitting documents...")
    chunks = split_documents(documents) #split documents

    print("=" * 60)
    print("Connecting to Chroma...")
    vector_store = get_vector_store() #embedding

    print("=" * 60)
    print("Preparing chunk IDs...")

    ids = [generate_chunk_id(chunk) for chunk in chunks]

    print("=" * 60)
    print("Writing chunks to ChromaDB...")

    #add chunks in vectro datstore
    vector_store.add_documents(
        documents=chunks,
        ids=ids,
    )

    print("=" * 60)
    print("Ingestion Complete")
    print(f"Documents : {len(documents)}")
    print(f"Chunks     : {len(chunks)}")
    print("=" * 60)


if __name__ == "__main__":
    print("Inside name and main")
    ingest()