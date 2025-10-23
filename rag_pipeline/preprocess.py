# rag_pipeline/preprocess.py
import fitz  # PyMuPDF

def preprocess_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    doc.close()
    return text.strip()
