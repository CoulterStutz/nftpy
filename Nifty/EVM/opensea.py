import requests

class OpenSea:
    def __init__(self, api_key: str, collection_slug: str):
        self.api_key = api_key
        self.collection_slug = collection_slug
        self.base_url = "https://api.opensea.io/api/v1"

    def get_collection(self):
        url = f"https://api.opensea.io/api/v2/collections/{self.collection_slug}"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_collection_stats(self):
        url = f"{self.base_url}/collection/{self.collection_slug}/stats"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_events_by_nft(self, chain, address, identifier, event_type=None, only_opensea=False, auction_type=None, occurred_before=None, occurred_after=None, cursor=None, limit=50):
        url = f"https://api.opensea.io/api/v2/events/chain/{chain}/contract/{address}/nfts/{identifier}"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        params = {
            "event_type": event_type,
            "only_opensea": str(only_opensea).lower(),
            "auction_type": auction_type,
            "occurred_before": occurred_before,
            "occurred_after": occurred_after,
            "cursor": cursor,
            "limit": limit
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_events_by_collection(self, event_type=None, occurred_before=None, occurred_after=None, cursor=None, limit=None):
        url = f"{self.base_url}/events"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        params = {
            "collection_slug": self.collection_slug
        }
        if event_type:
            params["event_type"] = event_type
        if occurred_before:
            params["occurred_before"] = occurred_before
        if occurred_after:
            params["occurred_after"] = occurred_after
        if cursor:
            params["cursor"] = cursor
        if limit:
            params["limit"] = limit

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
