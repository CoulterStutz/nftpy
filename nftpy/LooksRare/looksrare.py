from enum import Enum
from ..errors import APIKeyNotSpecifiedOnMainnetError, RateLimitExceededError, InvalidLooksRareAPIRequest, \
    APIKeyRequiredForPostError
from termcolor import colored
import requests

class LooksRareChain(Enum):
    MAINNET = "https://api.looksrare.org/api/"
    SEPOLIA = "https://api-sepolia.looksrare.org/api/"


class LooksRareAPI:
    def __init__(self, chain: LooksRareChain, api_key: str = None, suppress_warnings: bool = False, version: int = 2):
        self._chain = chain
        self._api_key = api_key
        self._version = version
        if self._chain == LooksRareChain.MAINNET and self._version == 2:
            if self._api_key is None:
                raise APIKeyNotSpecifiedOnMainnetError()
        elif self._chain == LooksRareChain.SEPOLIA:
            if self._api_key is not None and suppress_warnings is False:
                print(colored("[NFTPY]: Warning! API key isn't needed for the Sepolia Network!", 'yellow'))

    def get_account_by_address(self, address: str):
        url = f"{self._chain.value}v1/account/{address}"
        headers = {"Accept": "application/json"}

        response = requests.get(url, headers=headers)

        if response.status_code == 429:
            raise RateLimitExceededError()
        if response.status_code == 400:
            raise InvalidLooksRareAPIRequest()

        if not response.ok:
            response.raise_for_status()

        return response.json()

    def get_collection_by_address(self, address: str):
        url = f"{self._chain.value}v1/collections/{address}"
        headers = {"Accept": "application/json"}

        response = requests.get(url, headers=headers)

        if response.status_code == 429:
            raise RateLimitExceededError()
        if response.status_code == 400:
            raise InvalidLooksRareAPIRequest()

        if not response.ok:
            response.raise_for_status()

        return response.json()

    def get_collection_stats(self, address: str):
        url = f"{self._chain.value}v1/collections/stats?collection={address}"
        headers = {"Accept": "application/json"}

        response = requests.get(url, headers=headers)

        if response.status_code == 429:
            raise RateLimitExceededError()
        if response.status_code == 400:
            raise InvalidLooksRareAPIRequest()

        if not response.ok:
            response.raise_for_status()

        return response.json()

    def get_lre_eligible_collections(self):
        url = f"{self._chain.value}v1/collections/lre-eligible"
        headers = {"Accept": "application/json"}

        response = requests.get(url, headers=headers)

        if response.status_code == 429:
            raise RateLimitExceededError()
        if response.status_code == 400:
            raise InvalidLooksRareAPIRequest()

        if not response.ok:
            response.raise_for_status()

        return response.json()

    def get_collection_token(self, collection_address: str, token_id: str):
        url = f"{self._chain.value}v1/collections/{collection_address}/tokens/{token_id}"
        headers = {"Accept": "application/json"}

        response = requests.get(url, headers=headers)

        if response.status_code == 429:
            raise RateLimitExceededError()
        if response.status_code == 400:
            raise InvalidLooksRareAPIRequest()

        if not response.ok:
            response.raise_for_status()

        return response.json()

    def refresh_token_metadata(self, collection_address: str, token_id: str):
        if self._version == 1 and self._api_key is None:
            raise APIKeyRequiredForPostError()

        url = f"{self._chain.value}v1/tokens/refresh/{collection_address}/{token_id}"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-API-KEY": self._api_key
        }

        response = requests.post(url, headers=headers)

        if response.status_code == 429:
            raise RateLimitExceededError()
        if response.status_code == 400:
            raise InvalidLooksRareAPIRequest()

        if not response.ok:
            response.raise_for_status()

        return response.json()