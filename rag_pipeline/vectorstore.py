import chromadb

def get_vectorstore():
    client = chromadb.PersistentClient(path="chroma_db")
    collection = client.get_or_create_collection("fitness_articles")
    return collection

def save_to_vectorstore(doc_id, text, embedding):
    collection = get_vectorstore()
    collection.add(
        ids=[doc_id],
        documents=[text],
        embeddings=[embedding]
    )
