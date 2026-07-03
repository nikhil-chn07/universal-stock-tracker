import json

with open("products.json", "r", encoding="utf-8") as f:
    products = json.load(f)["products"]

print("=" * 40)
print("Universal Stock Tracker")
print("=" * 40)

print(f"Loaded {len(products)} products")
