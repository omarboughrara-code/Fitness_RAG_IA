# list_models.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

models = genai.list_models()

for m in models:
    print("Name:", m.name)
    # Si available_methods existe
    if hasattr(m, "available_methods"):
        print("Methods:", m.available_methods)
    print("-----")
