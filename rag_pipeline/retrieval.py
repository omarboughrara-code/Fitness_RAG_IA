# rag_pipeline/retrieval.py
from rag_pipeline.vectorstore import get_vectorstore
from rag_pipeline.voyage_embedder import embed_text

def retrieve_docs(query: str, n_results=3):
    collection = get_vectorstore()
    query_embedding = embed_text([query])[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=n_results)
    return results
