import pytest
from src.products_controller import search_products


@pytest.mark.parametrize("query", ["eyeshadow", "phone"])
def test_search_products(query):
    products = search_products(query=query)

    for product in products:
        assert (
            query in product["title"].lower()
            or query in product["description"].lower()
            or query in product["tags"]
        )
