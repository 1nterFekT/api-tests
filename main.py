from src.products_controller import *

categories = get_product_categories()

print("Getting all product categories:")
for category in categories:
    print("\b", category)

print("\nGetting products without limits:")
print("\b", len(get_products()))

print("\nGetting products without limit=10:")
print("\b", len(get_products(limit=10)))

print("\nSearch products with 'phone' query:")
print("\b", len(search_products(query="phone")))


print("\nGetting products by categories:")
for category in categories:
    print("\b", f"{category}: {len(get_products_by_category(category=category))}")
