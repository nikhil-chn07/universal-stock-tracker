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

    # Temporary product ID
    product_id = 529513633

    api = build_availability_url(product_id)

    response = requests.get(
        api,
        headers=HEADERS,
        timeout=30
    )

    if response.status_code != 200:
        print("API Error:", response.status_code)
        return {"status": "API Error"}

    data = response.json()

    print()
    print("Raw API Response")
    print("-" * 40)

    for item in data["skusAvailability"]:
        print(item)

    return {
        "status": "OK"
    }
