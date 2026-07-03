import json
from stores import zara

# Load products
with open("products.json", "r", encoding="utf-8") as f:
    products = json.load(f)["products"]

# Load previous state
try:
    with open("state.json", "r", encoding="utf-8") as f:
        state = json.load(f)
except:
    state = {}

print("=" * 40)
print("Universal Stock Tracker")
print("=" * 40)

for product in products:

    url = product["url"]

    if "zara.com" in url:
        result = zara.check(product)
    else:
        continue

    current = result["status"]
    previous = state.get(url)

    print(f"Previous: {previous}")
    print(f"Current : {current}")

    if previous != current:
        print("🔔 STOCK STATUS CHANGED!")

    state[url] = current

# Save latest state
with open("state.json", "w", encoding="utf-8") as f:
    json.dump(state, f, indent=4)
