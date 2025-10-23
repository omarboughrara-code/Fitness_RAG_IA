# scripts/ingest_all.py
import os
from rag_pipeline.preprocess import preprocess_pdf
from rag_pipeline.voyage_embedder import embed_text
from rag_pipeline.vectorstore import save_to_vectorstore

DATA_DIR = "data/fitness retrival articlces"

def ingest_all():
    for root, dirs, files in os.walk(DATA_DIR):
        for file in files:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                print(f"Processing: {pdf_path}")
                text = preprocess_pdf(pdf_path)
                if text:
                    embedding = embed_text(text)
                    save_to_vectorstore(file, text, embedding)

if __name__ == "__main__":
    ingest_all()
