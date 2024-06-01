from enum import Enum
import requests


class RaribleChain(Enum):
    ETHEREUM = "ETHEREUM"
    POLYGON = "POLYGON"

class Rarible:
    def __init__(self, chain: RaribleChain):
        self.chain = chain
        self.base_url = "https://api.rarible.org/v0.1"

    def get_item_by_id(self, item_id: str):
        """
        Get item details by item ID.

        Args:
            item_id (str): The ID of the item.

        Returns:
            dict: Details of the item.
        """
        url = f"{self.base_url}/items/{item_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_items_by_ids(self, item_ids: list):
        """
        Get multiple items details by their IDs.

        Args:
            item_ids (list): A list of item IDs.

        Returns:
            dict: Details of the items.
        """
        url = f"{self.base_url}/items/byIds"
        params = {"ids": ",".join(item_ids)}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_item_royalties_by_id(self, item_id: str):
        """
        Get royalties for an item by item ID.

        Args:
            item_id (str): The ID of the item.

        Returns:
            dict: Royalties information of the item.
        """
        url = f"{self.base_url}/items/{item_id}/royalties"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_items_by_owner(self, owner: str):
        """
        Get items owned by a specific owner.

        Args:
            owner (str): The address of the owner.

        Returns:
            dict: Items owned by the specified owner.
        """
        url = f"{self.base_url}/items/byOwner"
        params = {"owner": owner}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_items_by_creator(creator: str):
        """
        Get items created by a specific creator.

        Args:
            creator (str): The address of the creator.

        Returns:
            dict: Items created by the specified creator.
        """
        url = f"https://api.rarible.org/v0.1/items/byCreator"
        params = {"creator": creator}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_items_by_collection(collection: str):
        """
        Get items in a specific collection.

        Args:
            collection (str): The ID of the collection.

        Returns:
            dict: Items in the specified collection.
        """
        url = f"https://api.rarible.org/v0.1/items/byCollection"
        params = {"collection": collection}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    def query_traits(collection: str):
        """
        Query traits of items in a specific collection.

        Args:
            collection (str): The ID of the collection.

        Returns:
            dict: Traits of items in the specified collection.
        """
        url = f"https://api.rarible.org/v0.1/items/traits"
        params = {"collection": collection}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_lazy_item_by_id(item_id: str):
        """
        Get a lazy item by item ID.

        Args:
            item_id (str): The ID of the item.

        Returns:
            dict: Details of the lazy item.
        """
        url = f"https://api.rarible.org/v0.1/items/{item_id}/lazy"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    def burn_lazy_item(item_id: str):
        """
        Burn a lazy item by item ID.

        Args:
            item_id (str): The ID of the lazy item to burn.

        Returns:
            dict: Result of the burn operation.
        """
        url = f"https://api.rarible.org/v0.1/items/{item_id}/lazy/burn"
        response = requests.post(url)
        response.raise_for_status()
        return response.json()

    def get_ownership_by_id(ownership_id: str):
        """
        Get ownership details by ownership ID.

        Args:
            ownership_id (str): The ID of the ownership.

        Returns:
            dict: Details of the ownership.
        """
        url = f"https://api.rarible.org/v0.1/ownerships/{ownership_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_ownerships_by_ids(ownership_ids: list):
        """
        Get multiple ownerships details by their IDs.

        Args:
            ownership_ids (list): A list of ownership IDs.

        Returns:
            dict: Details of the ownerships.
        """
        url = f"https://api.rarible.org/v0.1/ownerships/byIds"
        params = {"ids": ",".join(ownership_ids)}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_ownerships_by_collection(collection: str):
        """
        Get ownerships in a specific collection.

        Args:
            collection (str): The ID of the collection.

        Returns:
            dict: Ownerships in the specified collection.
        """
        url = f"https://api.rarible.org/v0.1/ownerships/byCollection"
        params = {"collection": collection}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
