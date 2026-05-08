from app.search import search_products


def test_search_laptop():
    results = search_products(query="laptop")

    assert len(results["results"]) > 0
    assert results["results"][0]["category"] == "Electronics"


def test_search_books():
    results = search_products(query="book")

    assert results["total_results"] >= 1


def test_rating_filter():
    results = search_products(
        query="book",
        min_rating=4.8
    )

    for item in results["results"]:
        assert item["rating"] >= 4.8