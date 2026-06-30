from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

from app_etl_rag.config import DATA_DIR

def get_pdf_files() -> list[Path]:
    return sorted(DATA_DIR.rglob("*.pdf"))


def load_all_pdfs() -> list[Document]:
    pdf_files = get_pdf_files()

    if not pdf_files:
        raise FileNotFoundError(
            f"No PDF files found in: {DATA_DIR}"
        )

    documents: list[Document] = []

    for pdf_file in pdf_files:
        print(f"Loading: {pdf_file.name}")
        loader = PyPDFLoader(str(pdf_file))
        pdf_docs = loader.load()
        # Add useful metadata
        for doc in pdf_docs:
            doc.metadata["source_file"] = pdf_file.name
            doc.metadata["source_path"] = str(pdf_file)
        documents.extend(pdf_docs)
    print(f"\nLoaded {len(pdf_files)} PDF(s)")
    print(f"Total Pages: {len(documents)}")
    return documents