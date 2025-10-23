# rag_pipeline/voyage_embedder.py
from voyageai import Client
import os
from dotenv import load_dotenv

load_dotenv()
client = Client(api_key=os.getenv("VOYAGE_API_KEY"))

def embed_text(texts):
    """Generate embeddings for input texts using VoyageAI"""
    response = client.embed(texts=texts, model="voyage-large-2")
    return response.embeddings
