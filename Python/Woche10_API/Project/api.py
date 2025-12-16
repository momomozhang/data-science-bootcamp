import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon"


def fetch_data(name):
    url = f"{BASE_URL}/{name.lower()}"
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.json()
    return None
