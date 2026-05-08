from typing import Optional

from app.database import products
from app.ranking import calculate_ranking_score


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
        product_copy["ranking_score"] = calculate_ranking_score(product, query)
        results.append(product_copy)

    results.sort(key=lambda item: item["ranking_score"], reverse=True)

    total_results = len(results)
    paginated_results = results[offset: offset + limit]

    return {
        "query": query,
        "total_results": total_results,
        "limit": limit,
        "offset": offset,
        "results": paginated_results,
    }