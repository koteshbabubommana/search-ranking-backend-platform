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