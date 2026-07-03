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

    print("Status:", response.status_code)

    if response.status_code != 200:
        return {"status": "API Error"}

    data = response.json()

    print("\nStock Status")

    found = False

    for item in data["skusAvailability"]:
        print(item)

        if item["availability"] == "in_stock":
            found = True

    if found:
        print("\n🟢 STOCK AVAILABLE!")
        return {"status": "IN STOCK"}

    print("\n🔴 OUT OF STOCK")
    return {"status": "OUT OF STOCK"}
