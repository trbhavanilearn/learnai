from app_etl_rag.vectorstores.chroma_store import get_vector_store

vector_store = get_vector_store()

results = vector_store.similarity_search(
    "Who is Bhavani",
    k=3,
)

for doc in results:
    #print(doc.metadata)
    print(doc.page_content)