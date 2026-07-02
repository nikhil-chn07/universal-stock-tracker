import requests

URL = input("Paste Zara product URL:\n").strip()

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}

print("\nDownloading page...")

response = requests.get(URL, headers=HEADERS, timeout=30)

print("Status Code:", response.status_code)
print("Page Length:", len(response.text))

with open("zara_page.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Saved page as zara_page.html")
