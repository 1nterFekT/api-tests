from src.products_controller import get_products_by_category


def test_get_products_by_category(shared_categories):
    for category in shared_categories:
        products = get_products_by_category(category=category)

        for product in products:
            assert product["category"] == category
