import random
import time
import requests

# Random delay settings (seconds)
MIN_DELAY = 10
MAX_DELAY = 60

delay = random.randint(MIN_DELAY, MAX_DELAY)
print(f"Waiting {delay} seconds before checking...")
time.sleep(delay)

print("=================================")
print(" Universal Stock Tracker")
print("=================================")

response = requests.get(
    "https://www.google.com",
    timeout=30,
    headers={
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0.0.0 Safari/537.36"
        )
    },
)

print("Status Code:", response.status_code)

if response.status_code == 200:
    print("Internet Working ✅")
else:
    print("Something went wrong")
