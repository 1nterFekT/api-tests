import requests


def get_product_categories():
    response = requests.get("https://dummyjson.com/products/category-list")
    return response.json()


def get_products(limit: int = 0):
    response = requests.get(f"https://dummyjson.com/products?limit={limit}")
    return response.json()["products"]


def get_products_by_category(category: str, limit: int = 0):
    response = requests.get(
        f"https://dummyjson.com/products/category/{category}?limit={limit}"
    )

    return response.json()["products"]


def search_products(query: str, limit: int = 0):
    response = requests.get(
        f"https://dummyjson.com/products/search?q={query}&limit={limit}"
    )

    return response.json()["products"]
