import json
from stores import zara

with open("products.json", "r", encoding="utf-8") as f:
    products = json.load(f)["products"]

print("=" * 40)
print("Universal Stock Tracker")
print("=" * 40)

for product in products:

    if "zara.com" in product["url"]:
        result = zara.check(product)
        print(result)

    else:
        print("Store not supported")
