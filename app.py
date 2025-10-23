# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline.retrieval import retrieve_docs
from rag_pipeline.generator import generate_answer

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/query")
def query_rag(request: Query):
    results = retrieve_docs(request.question)
    context = " ".join(results["documents"][0])
    answer = generate_answer(request.question, context)
    return {"answer": answer, "sources": results["ids"][0]}
