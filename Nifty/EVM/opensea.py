import requests

class OpenSea:
    def __init__(self, api_key: str, collection_slug: str):
        self.api_key = api_key
        self.collection_slug = collection_slug
        self.base_url = "https://api.opensea.io/api/v2/collections"

    def get_collection_stats(self):
        url = f"{self.base_url}/{self.collection_slug}/stats"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
