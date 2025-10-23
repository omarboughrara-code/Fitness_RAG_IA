# rag_pipeline/query_translation.py
from langchain.retrievers.multi_query import MultiQueryRetriever

def expand_query(llm, retriever, query: str):
    """Use MultiQuery to generate multiple reformulations of the user query"""
    mqr = MultiQueryRetriever.from_llm(retriever=retriever, llm=llm)
    return mqr.get_relevant_documents(query)
