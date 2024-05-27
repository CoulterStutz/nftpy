import requests
from enum import Enum
from errors import APIRequestFailed, MissingChain, MissingSlug

class OpenSeaChain(Enum):
    ETHEREUM = "ethereum"
    POLYGON = "polygon"
    KLAYTN = "klaytn"
    MUMBAI = "mumbai"
    GOERLI = "goerli"
    ARBITRUM = "arbitrum"
    OPTIMISM = "optimism"
    BASE = "base"
    BNB = "bnb"
    SCROLL_ALPHA = "scroll_alpha"

class OpenSea:
    def __init__(self, api_key: str, chain: OpenSeaChain = None, collection_slug: str = None):
        self.api_key = api_key
        self.chain = chain
        self.collection_slug = collection_slug
        self.base_url = "https://api.opensea.io/api/v2"

    def get_collection_stats(self, collection_slug: str = None):
        collection_slug = collection_slug or self.collection_slug
        if collection_slug is None:
            raise MissingSlug()
        url = f"{self.base_url}/collection/{collection_slug}/stats"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise APIRequestFailed(response.status_code)

    def list_events_by_nft(self, address: str, token_id: str, chain: OpenSeaChain = None, event_type: str = None, only_opensea: bool = False, auction_type: str = None, occurred_before: str = None, occurred_after: str = None, cursor: str = None, limit: int = 50):
        chain = chain or self.chain
        if chain is None:
            raise MissingChain()
        url = f"{self.base_url}/events/chain/{chain.value}/contract/{address}/nfts/{token_id}"
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
            raise APIRequestFailed(response.status_code)

    def get_collection(self, collection_slug: str = None):
        collection_slug = collection_slug or self.collection_slug
        if collection_slug is None:
            raise MissingSlug()
        url = f"{self.base_url}/collection/{collection_slug}"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise APIRequestFailed(response.status_code)

    def get_contract(self, address: str, chain: OpenSeaChain = None):
        chain = chain or self.chain
        if chain is None:
            raise MissingChain()
        url = f"{self.base_url}/chain/{chain.value}/contract/{address}"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise APIRequestFailed(response.status_code)

    def get_nft(self, address: str, token_id: str, chain: OpenSeaChain = None):
        chain = chain or self.chain
        if chain is None:
            raise MissingChain()
        url = f"{self.base_url}/chain/{chain.value}/contract/{address}/nfts/{token_id}"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise APIRequestFailed(response.status_code)

    def list_nfts_by_account(self, address: str, chain: OpenSeaChain = None, cursor: str = None, limit: int = 50):
        chain = chain or self.chain
        if chain is None:
            raise MissingChain()
        url = f"{self.base_url}/chain/{chain.value}/account/{address}/nfts"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        params = {
            "cursor": cursor,
            "limit": limit
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise APIRequestFailed(response.status_code)

    def list_nfts_by_collection(self, collection_slug: str = None, chain: OpenSeaChain = None, cursor: str = None, limit: int = 50):
        collection_slug = collection_slug or self.collection_slug
        chain = chain or self.chain
        if collection_slug is None:
            raise MissingSlug()
        if chain is None:
            raise MissingChain()
        url = f"{self.base_url}/chain/{chain.value}/collection/{collection_slug}/nfts"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        params = {
            "cursor": cursor,
            "limit": limit
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise APIRequestFailed(response.status_code)

    def list_nfts_by_contract(self, contract_address: str, chain: OpenSeaChain = None, cursor: str = None, limit: int = 50):
        chain = chain or self.chain
        if chain is None:
            raise MissingChain()
        url = f"{self.base_url}/chain/{chain.value}/contract/{contract_address}/nfts"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        params = {
            "cursor": cursor,
            "limit": limit
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise APIRequestFailed(response.status_code)

    def get_payment_token(self, address: str, chain: OpenSeaChain = None):
        chain = chain or self.chain
        if chain is None:
            raise MissingChain()
        url = f"{self.base_url}/chain/{chain.value}/payment_token/{address}"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise APIRequestFailed(response.status_code)

    def get_traits(self, collection_slug: str = None):
        collection_slug = collection_slug or self.collection_slug
        if collection_slug is None:
            raise MissingSlug()
        url = f"{self.base_url}/collection/{collection_slug}/traits"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise APIRequestFailed(response.status_code)

    def get_all_listings_on_collection(self, collection_slug: str = None, chain: OpenSeaChain = None, cursor: str = None, limit: int = 50):
        collection_slug = collection_slug or self.collection_slug
        chain = chain or self.chain
        if collection_slug is None:
            raise MissingSlug()
        if chain is None:
            raise MissingChain()
        url = f"{self.base_url}/chain/{chain.value}/collection/{collection_slug}/listings"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        params = {
            "cursor": cursor,
            "limit": limit
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise APIRequestFailed(response.status_code)
