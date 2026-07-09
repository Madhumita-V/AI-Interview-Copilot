from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
@app.get("/")
def home():
    return {
        "name": "Madhumita",
        "project": "AI Interview Copilot",
        "status": "Learning FastAPI"
    }

@app.get("/hello/{name}")
def hello(name: str):
    return {
        "message": f"Hello {name}!"
    }

@app.get("/new")
def new():
    return {
    "project": "AI Interview Copilot",
    "version": "1.0",
    "developer": "Madhumita"
    }


class InterviewAnswer(BaseModel):
    name: str
    answer: str

@app.post("/answer")
def submit_answer(data: InterviewAnswer):
    return {
        "message": "Answer received!",
        "name": data.name,
        "answer": data.answer
    }
