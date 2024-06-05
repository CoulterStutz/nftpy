import requests
from enum import Enum


class MintableChain(Enum):
    MAINNET = 1
    RINKEBY = 4


class Mintable:
    def __init__(self, api_key, chain: MintableChain):
        self.api_key = api_key
        self.chain = chain
        self.base_url = "https://api.mintable.app/v1"

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}"
        }

    def search_nfts_for_sale(self, query_params=None):
        url = f"{self.base_url}/marketplace/search"
        headers = self._get_headers()
        response = requests.get(url, headers=headers, params=query_params)
        response.raise_for_status()
        return response.json()

    def fetch_single_nft_for_sale(self, nft_id):
        url = f"{self.base_url}/marketplace/{nft_id}"
        headers = self._get_headers()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
