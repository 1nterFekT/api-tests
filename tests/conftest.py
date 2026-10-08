import pytest
from src.products_controller import get_product_categories


@pytest.fixture(scope="class")
def shared_categories():
    return get_product_categories()
