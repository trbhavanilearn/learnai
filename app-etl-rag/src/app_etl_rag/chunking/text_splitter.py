from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app_etl_rag.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


def get_text_splitter() -> RecursiveCharacterTextSplitter:
    return RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        add_start_index=True,
    )


def split_documents(documents: list[Document]) -> list[Document]:
    splitter = get_text_splitter()
    chunks = splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks")
    return chunks