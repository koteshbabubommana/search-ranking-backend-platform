from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    category: str
    price: float
    rating: float
    popularity: int
    ranking_score: float | None = None