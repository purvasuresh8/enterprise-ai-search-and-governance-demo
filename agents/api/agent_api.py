from fastapi import FastAPI
from agents.orchestrator import AgentOrchestrator

app = FastAPI(
    title="Enterprise Agent Platform",
    version="1.0.0"
)

orchestrator = AgentOrchestrator()


@app.get("/")
def health():

    return {
        "status": "healthy"
    }


@app.get("/ask")
def ask(query: str):

    return orchestrator.route(query)