import requests
from enum import Enum
from ..errors import APIRequestFailedError, MissingChainError, MissingSlugError


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
    """
    A class to interact with the OpenSea API.

    Args:
        api_key (str): The API key for accessing OpenSea.
        chain (OpenSeaChain, optional): The blockchain network to interact with.
        collection_slug (str, optional): The slug of the collection to focus on.
    """

    def __init__(self, api_key: str, chain: OpenSeaChain = None, collection_slug: str = None):
        self.api_key = api_key
        self.chain = chain
        self.collection_slug = collection_slug
        self.base_url = "https://api.opensea.io/api/v2"

    def get_collection_stats(self, collection_slug: str = None):
        """
        Get statistics for a collection.

        Args:
            collection_slug (str, optional): The slug of the collection.

        Returns:
            dict: A dictionary containing collection statistics.

        Raises:
            MissingSlugError: If no collection slug is provided.
            APIRequestFailedError: If the API request fails.
        """
        collection_slug = collection_slug or self.collection_slug
        if collection_slug is None:
            raise MissingSlugError()
        url = f"{self.base_url}/collection/{collection_slug}/stats"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise APIRequestFailedError(response.status_code)

    def list_events_by_nft(self, address: str, token_id: str, chain: OpenSeaChain = None, event_type: str = None,
                           only_opensea: bool = False, auction_type: str = None, occurred_before: str = None,
                           occurred_after: str = None, cursor: str = None, limit: int = 50):
        """
        List events related to a specific NFT.

        Args:
            address (str): The contract address of the NFT.
            token_id (str): The token ID of the NFT.
            chain (OpenSeaChain, optional): The blockchain network.
            event_type (str, optional): The type of event.
            only_opensea (bool, optional): Whether to include only OpenSea events.
            auction_type (str, optional): The type of auction.
            occurred_before (str, optional): Events occurred before this date.
            occurred_after (str, optional): Events occurred after this date.
            cursor (str, optional): Cursor for pagination.
            limit (int, optional): Number of results to return (default is 50).

        Returns:
            dict: A dictionary containing the events.

        Raises:
            MissingChainError: If no chain is provided.
            APIRequestFailedError: If the API request fails.
        """
        chain = chain or self.chain
        if chain is None:
            raise MissingChainError()
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
            raise APIRequestFailedError(response.status_code)

    def get_collection(self, collection_slug: str = None):
        """
        Get details of a collection.

        Args:
            collection_slug (str, optional): The slug of the collection.

        Returns:
            dict: A dictionary containing collection details.

        Raises:
            MissingSlugError: If no collection slug is provided.
            APIRequestFailedError: If the API request fails.
        """
        collection_slug = collection_slug or self.collection_slug
        if collection_slug is None:
            raise MissingSlugError()
        url = f"{self.base_url}/collection/{collection_slug}"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise APIRequestFailedError(response.status_code)

    def get_contract(self, address: str, chain: OpenSeaChain = None):
        """
        Get details of a specific contract.

        Args:
            address (str): The contract address.
            chain (OpenSeaChain, optional): The blockchain network.

        Returns:
            dict: A dictionary containing contract details.

        Raises:
            MissingChainError: If no chain is provided.
            APIRequestFailedError: If the API request fails.
        """
        chain = chain or self.chain
        if chain is None:
            raise MissingChainError()
        url = f"{self.base_url}/chain/{chain.value}/contract/{address}"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise APIRequestFailedError(response.status_code)

    def get_nft(self, address: str, token_id: str, chain: OpenSeaChain = None):
        """
        Get details of a specific NFT.

        Args:
            address (str): The contract address of the NFT.
            token_id (str): The token ID of the NFT.
            chain (OpenSeaChain, optional): The blockchain network.

        Returns:
            dict: A dictionary containing NFT details.

        Raises:
            MissingChainError: If no chain is provided.
            APIRequestFailedError: If the API request fails.
        """
        chain = chain or self.chain
        if chain is None:
            raise MissingChainError()
        url = f"{self.base_url}/chain/{chain.value}/contract/{address}/nfts/{token_id}"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise APIRequestFailedError(response.status_code)

    def list_nfts_by_account(self, address: str, chain: OpenSeaChain = None, cursor: str = None, limit: int = 50):
        """
        List NFTs owned by a specific account.

        Args:
            address (str): The account address.
            chain (OpenSeaChain, optional): The blockchain network.
            cursor (str, optional): Cursor for pagination.
            limit (int, optional): Number of results to return (default is 50).

        Returns:
            dict: A dictionary containing the NFTs.

        Raises:
            MissingChainError: If no chain is provided.
            APIRequestFailedError: If the API request fails.
        """
        chain = chain or self.chain
        if chain is None:
            raise MissingChainError()
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
            raise APIRequestFailedError(response.status_code)

    def list_nfts_by_collection(self, collection_slug: str = None, chain: OpenSeaChain = None, cursor: str = None,
                                limit: int = 50):
        """
        List NFTs in a specific collection.

        Args:
            collection_slug (str, optional): The slug of the collection.
            chain (OpenSeaChain, optional): The blockchain network.
            cursor (str, optional): Cursor for pagination.
            limit (int, optional): Number of results to return (default is 50).

        Returns:
            dict: A dictionary containing the NFTs.

        Raises:
            MissingSlugError: If no collection slug is provided.
            MissingChainError: If no chain is provided.
            APIRequestFailedError: If the API request fails.
        """
        collection_slug = collection_slug or self.collection_slug
        chain = chain or self.chain
        if collection_slug is None:
            raise MissingSlugError()
        if chain is None:
            raise MissingChainError()
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
            raise APIRequestFailedError(response.status_code)

    def list_nfts_by_contract(self, contract_address: str, chain: OpenSeaChain = None, cursor: str = None,
                              limit: int = 50):
        """
        List NFTs under a specific contract.

        Args:
            contract_address (str): The contract address.
            chain (OpenSeaChain, optional): The blockchain network.
            cursor (str, optional): Cursor for pagination.
            limit (int, optional): Number of results to return (default is 50).

        Returns:
            dict: A dictionary containing the NFTs.

        Raises:
            MissingChainError: If no chain is provided.
            APIRequestFailedError: If the API request fails.
        """
        chain = chain or self.chain
        if chain is None:
            raise MissingChainError()
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
            raise APIRequestFailedError(response.status_code)

    def get_payment_token(self, address: str, chain: OpenSeaChain = None):
        """
        Get details of a specific payment token.

        Args:
            address (str): The address of the payment token.
            chain (OpenSeaChain, optional): The blockchain network.

        Returns:
            dict: A dictionary containing payment token details.

        Raises:
            MissingChainError: If no chain is provided.
            APIRequestFailedError: If the API request fails.
        """
        chain = chain or self.chain
        if chain is None:
            raise MissingChainError()
        url = f"{self.base_url}/chain/{chain.value}/payment_token/{address}"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise APIRequestFailedError(response.status_code)

    def get_traits(self, collection_slug: str = None):
        """
        Get traits of a specific collection.

        Args:
            collection_slug (str, optional): The slug of the collection.

        Returns:
            dict: A dictionary containing collection traits.

        Raises:
            MissingSlugError: If no collection slug is provided.
            APIRequestFailedError: If the API request fails.
        """
        collection_slug = collection_slug or self.collection_slug
        if collection_slug is None:
            raise MissingSlugError()
        url = f"{self.base_url}/collection/{collection_slug}/traits"
        headers = {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise APIRequestFailedError(response.status_code)

    def get_all_listings_on_collection(self, collection_slug: str = None, chain: OpenSeaChain = None,
                                       cursor: str = None, limit: int = 50):
        """
        Get all listings of a specific collection.

        Args:
            collection_slug (str, optional): The slug of the collection.
            chain (OpenSeaChain, optional): The blockchain network.
            cursor (str, optional): Cursor for pagination.
            limit (int, optional): Number of results to return (default is 50).

        Returns:
            dict: A dictionary containing the listings.

        Raises:
            MissingSlugError: If no collection slug is provided.
            MissingChainError: If no chain is provided.
            APIRequestFailedError: If the API request fails.
        """
        collection_slug = collection_slug or self.collection_slug
        chain = chain or self.chain
        if collection_slug is None:
            raise MissingSlugError()
        if chain is None:
            raise MissingChainError()
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
            raise APIRequestFailedError(response.status_code)
