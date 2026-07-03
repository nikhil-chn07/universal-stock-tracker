import requests
import json

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}

STORE_ID = 11744


def build_availability_url(product_id):
    return (
        f"https://www.zara.com/itxrest/1/catalog/store/"
        f"{STORE_ID}/product/id/{product_id}/availability"
    )


def check(product):

    print("=" * 50)
    print("Checking Zara")
    print("=" * 50)

    # TODO: This will be extracted automatically later
    product_id = 529513633

    api = build_availability_url(product_id)

    print("API:", api)

    response = requests.get(
        api,
        headers=HEADERS,
        timeout=30
    )

    print("Status Code:", response.status_code)

    if response.status_code != 200:
        return {"status": "API Error"}

    data = response.json()

    print("\n===== RAW RESPONSE =====")
    print(json.dumps(data, indent=4))
    print("========================\n")

    in_stock = False

    if "skusAvailability" in data:
        for item in data["skusAvailability"]:

            sku = item.get("sku")
            availability = item.get("availability")

            print(f"SKU: {sku}")
            print(f"Availability: {availability}")
            print("-" * 30)

            if availability == "in_stock":
                in_stock = True

    if in_stock:
        print("🟢 AT LEAST ONE VARIANT IS IN STOCK")
        return {"status": "IN STOCK"}

    print("🔴 ALL VARIANTS ARE OUT OF STOCK")
    return {"status": "OUT OF STOCK"}
