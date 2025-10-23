import os
import json
import pandas as pd
import PyPDF2

def read_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    elif ext == ".json":
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Convert JSON en texte
            return json.dumps(data)
    elif ext in [".xls", ".xlsx"]:
        df = pd.read_excel(file_path)
        return df.to_csv(index=False)
    elif ext == ".pdf":
        text = ""
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    else:
        print(f"⚠️ Format non supporté: {file_path}")
        return ""
