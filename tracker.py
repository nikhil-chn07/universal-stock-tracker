import json
import requests

with open("products.json", "r", encoding="utf-8") as f:
    products = json.load(f)["products"]

headers = {
    "User-Agent": "Mozilla/5.0"
}

for product in products:

    print("=" * 50)
    print(product["name"])

    response = requests.get(
        product["url"],
        headers=headers,
        timeout=30
    )

    print("Status:", response.status_code)
    print("Length:", len(response.text))

    print("\nFIRST 1000 CHARACTERS:\n")
    print(response.text[:1000])
