from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Enterprise Search API",
    version="1.0.0",
    description="Enterprise Search Service"
)

app.include_router(router)


@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "enterprise-search"
    }