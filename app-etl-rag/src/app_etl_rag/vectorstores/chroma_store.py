from langchain_chroma import Chroma

from app_etl_rag.config import (
    CHROMA_DB_DIR,
    COLLECTION_NAME,
)
from app_etl_rag.embeddings.embedding_model import get_embedding_model


def get_vector_store() -> Chroma:
    embedding_model = get_embedding_model()
    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=str(CHROMA_DB_DIR),
        embedding_function=embedding_model,
    )
    return vector_store