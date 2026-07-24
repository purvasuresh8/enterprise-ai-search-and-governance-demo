from fastapi import APIRouter, Query
from search_engine import SearchEngine

router = APIRouter(prefix="/search", tags=["Search"])

search_engine = SearchEngine()


@router.get("/")
def search_documents(query: str = Query(..., min_length=2)):
    results = search_engine.search(query)

    return {
        "query": query,
        "count": len(results),
        "results": results
    }