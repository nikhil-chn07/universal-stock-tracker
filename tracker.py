import json
import re
import requests

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}


def load_products():
    with open("products.json", "r", encoding="utf-8") as f:
        return json.load(f)["products"]


def download_page(url):
    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()
    return response.text


def extract_metadata(html):

    product_name = re.search(r'"productName"\s*:\s*"([^"]+)"', html)
    product_ref = re.search(r'"productRef"\s*:\s*"([^"]+)"', html)
    catentry = re.search(r'"catentryId"\s*:\s*(\d+)', html)

    return {
        "product_name": product_name.group(1) if product_name else None,
        "product_ref": product_ref.group(1) if product_ref else None,
        "catentry_id": catentry.group(1) if catentry else None,
    }


products = load_products()

for product in products:

    print("=" * 50)
    print(product["name"])
    print("=" * 50)

    html = download_page(product["url"])

    metadata = extract_metadata(html)

    print("Product Name :", metadata["product_name"])
    print("Product Ref  :", metadata["product_ref"])
    print("Catentry ID  :", metadata["catentry_id"])
