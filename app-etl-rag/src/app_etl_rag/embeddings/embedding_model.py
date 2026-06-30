from functools import lru_cache

from langchain_ollama import OllamaEmbeddings

from app_etl_rag.config import EMBEDDING_MODEL


@lru_cache(maxsize=1)
def get_embedding_model():

    print("Loading Ollama embedding model...")

    return OllamaEmbeddings(
        model=EMBEDDING_MODEL,
    )