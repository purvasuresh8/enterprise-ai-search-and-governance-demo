from fastapi import FastAPI

from governance.engine.middleware import (
    GovernanceMiddleware
)

app = FastAPI(
    title="AI Governance Service",
    version="1.0.0"
)

middleware = GovernanceMiddleware()


@app.get("/")
def health():

    return {
        "status": "healthy",
        "service": "governance"
    }


@app.post("/validate")
def validate(
    user: str,
    prompt: str
):

    return middleware.inspect(
        user=user,
        prompt=prompt
    )