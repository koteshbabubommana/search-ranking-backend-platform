from typing import Optional
import time

from fastapi import FastAPI

from app.search import search_products

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Search Ranking Backend Platform Running"
    }


@app.get("/search")
def search(
    query: str,
    category: Optional[str] = None,
    min_rating: Optional[float] = None,
    max_price: Optional[float] = None,
    limit: int = 10,
    offset: int = 0,
):
    start_time = time.time()

    results = search_products(
        query=query,
        category=category,
        min_rating=min_rating,
        max_price=max_price,
        limit=limit,
        offset=offset,
    )

    response_time = round((time.time() - start_time) * 1000, 2)

    return {
        "response_time_ms": response_time,
        "data": results,
    }