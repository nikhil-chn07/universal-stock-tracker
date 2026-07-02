import json
import requests

# Load products
with open("products.json", "r", encoding="utf-8") as f:
    products = json.load(f)["products"]

print("=" * 40)
print("Universal Stock Tracker")
print("=" * 40)

headers = {
    "User-Agent": "Mozilla/5.0"
}

for product in products:

    print("\n------------------------------")
    print("Product:", product["name"])

    try:
        response = requests.get(
            product["url"],
            headers=headers,
            timeout=30
        )

        print("Status Code:", response.status_code)

        if response.status_code == 200:
            print("✅ Downloaded Successfully")
            print("Page Length:", len(response.text))
        else:
            print("❌ Failed")

    except Exception as e:
        print("Error:", e)
