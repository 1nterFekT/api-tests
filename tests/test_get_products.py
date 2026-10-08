from src.products_controller import get_products


def test_without_limits():
    assert len(get_products()) > 0


def test_with_limits():
    assert len(get_products(limit=10)) == 10
