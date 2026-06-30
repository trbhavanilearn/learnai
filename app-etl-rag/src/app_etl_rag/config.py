from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR / "data"

CHROMA_DB_DIR = BASE_DIR / "chroma_db"

COLLECTION_NAME = "pdf_documents"

EMBEDDING_MODEL = "nomic-embed-text"

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200