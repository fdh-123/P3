from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

@app.post("/ask")
async def answer_question(question: str, context: str):
    result = qa_pipeline(question=question, context=context)
    return {"answer": result["answer"]}