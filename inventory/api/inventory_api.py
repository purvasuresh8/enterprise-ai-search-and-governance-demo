from fastapi import FastAPI
from pydantic import BaseModel

from inventory.ai.support_agent import SupportAgent
from inventory.ai.evaluation_agent import EvaluationAgent

app = FastAPI(
    title="Generative AI Customer Support Platform",
    version="1.0.0"
)

support_agent = SupportAgent()
evaluation_agent = EvaluationAgent()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def health():
    return {
        "status": "healthy",
        "service": "genai-customer-support"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    answer = support_agent.generate_response(
        request.message
    )

    return {
        "question": request.message,
        "answer": answer
    }


@app.post("/evaluate")
def evaluate(request: ChatRequest):

    answer = support_agent.generate_response(
        request.message
    )

    scores = evaluation_agent.evaluate(
        request.message,
        answer
    )

    return {
        "answer": answer,
        "evaluation": scores
    }
    