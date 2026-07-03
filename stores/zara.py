import requests

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}


def check(product):

    print("Checking Zara...")

    response = requests.get(
        product["url"],
        headers=HEADERS,
        timeout=30
    )

    print("Status Code :", response.status_code)
    print("Page Length :", len(response.text))

    return {
        "status": response.status_code,
        "length": len(response.text)
    }
