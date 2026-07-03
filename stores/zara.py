import requests

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

    print("Checking Zara...")

    product_id = 529513633

    api = build_availability_url(product_id)

    response = requests.get(
        api,
        headers=HEADERS,
        timeout=30
    )

    data = response.json()

    print("\nStock Status")

    for item in data["skusAvailability"]:
        print(
            f'SKU {item["sku"]} -> {item["availability"]}'
        )

    return {
        "status": "OK"
    }
