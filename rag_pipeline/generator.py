import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_answer(question: str, context: list):
    prompt = f"Answer this question based on the following context:\n\n{context}\n\nQuestion: {question}"
    
    # Utiliser un modèle existant
    model = genai.GenerativeModel("models/gemini-2.5-pro")  # <-- Remplace par un modèle valide
    
    response = model.generate_content(prompt)
    return response.text
