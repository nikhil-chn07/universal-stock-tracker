import json

with open("products.json", "r") as f:
    products = json.load(f)["products"]

print("=" * 40)
print("Universal Stock Tracker")
print("=" * 40)

for product in products:
    print()
    print("Product:", product["name"])
    print("Store:", product["store"])
    print("Size:", product["size"])
    print("URL:", product["url"])
