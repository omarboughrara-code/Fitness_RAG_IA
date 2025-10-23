# rag_pipeline/ingestion.py
import os
from rag_pipeline.preprocess import clean_text, chunk_text
from rag_pipeline.voyage_embedder import embed_text
from rag_pipeline.vectorstore import get_vectorstore
from rag_pipeline.file_reader import read_file

def ingest_data(data_dir="data"):
    collection = get_vectorstore()

    for file_name in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file_name)
        if os.path.isfile(file_path):
            text = read_file(file_path)
            if not text.strip():
                continue  # ignorer si aucun texte trouvé

            cleaned = clean_text(text)
            chunks = chunk_text(cleaned)
            embeddings = embed_text(chunks)
            ids = [f"{file_name}_{i}" for i in range(len(chunks))]
            collection.add(documents=chunks, embeddings=embeddings, ids=ids)

    print("Data ingestion complète pour TXT, PDF, JSON et Excel !")
