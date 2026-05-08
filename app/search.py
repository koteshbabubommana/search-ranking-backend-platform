from typing import Optional

products = [
    {"id": 1, "name": "Apple MacBook Pro", "category": "Electronics", "price": 1899, "rating": 4.8, "popularity": 95},
    {"id": 2, "name": "Dell XPS 13 Laptop", "category": "Electronics", "price": 1299, "rating": 4.6, "popularity": 88},
    {"id": 3, "name": "Sony Wireless Headphones", "category": "Electronics", "price": 299, "rating": 4.7, "popularity": 91},
    {"id": 4, "name": "Nike Running Shoes", "category": "Fashion", "price": 140, "rating": 4.5, "popularity": 84},
    {"id": 5, "name": "Adidas Training Shoes", "category": "Fashion", "price": 120, "rating": 4.4, "popularity": 79},
    {"id": 6, "name": "Python Programming Book", "category": "Books", "price": 45, "rating": 4.9, "popularity": 76},
    {"id": 7, "name": "System Design Interview Book", "category": "Books", "price": 55, "rating": 4.8, "popularity": 89},
]


def calculate_ranking_score(product: dict, query: str) -> float:
    name_match_score = 1.0 if query.lower() in product["name"].lower() else 0.0
    rating_score = product["rating"] / 5
    popularity_score = product["popularity"] / 100

    final_score = (
        (name_match_score * 0.5)
        + (rating_score * 0.3)
        + (popularity_score * 0.2)
    )

    return round(final_score, 4)


def search_products(
    query: str,
    category: Optional[str] = None,
    min_rating: Optional[float] = None,
    max_price: Optional[float] = None,
    limit: int = 10,
    offset: int = 0,
):
    results = []

    for product in products:

        if query.lower() not in product["name"].lower():
            continue

        if category and product["category"].lower() != category.lower():
            continue

        if min_rating and product["rating"] < min_rating:
            continue

        if max_price and product["price"] > max_price:
            continue

        product_copy = product.copy()

        product_copy["ranking_score"] = calculate_ranking_score(
            product,
            query,
        )

        results.append(product_copy)

    results.sort(
        key=lambda item: item["ranking_score"],
        reverse=True,
    )

    total_results = len(results)

    paginated_results = results[offset: offset + limit]

    return {
        "query": query,
        "total_results": total_results,
        "limit": limit,
        "offset": offset,
        "results": paginated_results,
    }