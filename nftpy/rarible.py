from enum import En

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

    def get_items_by_creator(self, creator: str):
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

    def get_items_by_collection(self, collection: str):
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
    def query_traits(self, collection: str):
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

    def get_lazy_item_by_id(self, item_id: str):
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
    def burn_lazy_item(self, item_id: str):
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

    def get_ownership_by_id(self, ownership_id: str):
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

    def get_ownerships_by_ids(self, ownership_ids: list):
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

    def get_ownerships_by_collection(self, collection: str):
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

    def get_ownerships_by_item(self, item_id: str):
        """
        Get ownerships for a specific item.

        Args:
            item_id (str): The ID of the item.

        Returns:
            dict: Ownerships of the specified item.
        """
        url = f"https://api.rarible.org/v0.1/ownerships/byItem"
        params = {"itemId": item_id}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_collections_with_owned_items(self, owner: str):
        """
        Get collections with items owned by a specific owner.

        Args:
            owner (str): The address of the owner.

        Returns:
            dict: Collections with items owned by the specified owner.
        """
        url = f"https://api.rarible.org/v0.1/ownerships/collectionsWithOwnedItems"
        params = {"owner": owner}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_order_by_id(self, order_id: str):
        """
        Get order details by order ID.

        Args:
            order_id (str): The ID of the order.

        Returns:
            dict: Details of the order.
        """
        url = f"https://api.rarible.org/v0.1/orders/{order_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_order_by_id(self, order_id: str):
        """
        Get order details by order ID.

        Args:
            order_id (str): The ID of the order.

        Returns:
            dict: Details of the order.
        """
        url = f"https://api.rarible.org/v0.1/orders/{order_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_validated_order_by_id(self, order_id: str):
        """
        Get validated order details by order ID.

        Args:
            order_id (str): The ID of the validated order.

        Returns:
            dict: Details of the validated order.
        """
        url = f"https://api.rarible.org/v0.1/orders/{order_id}/validated"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_orders_by_ids(self, order_ids: list):
        """
        Get multiple orders details by their IDs.

        Args:
            order_ids (list): A list of order IDs.

        Returns:
            dict: Details of the orders.
        """
        url = f"https://api.rarible.org/v0.1/orders/byIds"
        params = {"ids": ",".join(order_ids)}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_orders_by_ids(self, order_ids: list):
        """
        Get multiple orders details by their IDs.

        Args:
            order_ids (list): A list of order IDs.

        Returns:
            dict: Details of the orders.
        """
        url = f"https://api.rarible.org/v0.1/orders/byIds"
        params = {"ids": ",".join(order_ids)}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_orders_all(self):
        """
        Get all orders.

        Returns:
            dict: Details of all orders.
        """
        url = f"https://api.rarible.org/v0.1/orders/all"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_all_sync(self):
        url = f"{self.base_url}/orders/all/sync"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_sell_orders_by_maker(self, maker: str):
        """
        Get sell orders by maker.

        Args:
            maker (str): The address of the maker.

        Returns:
            dict: Details of the sell orders by the specified maker.
        """
        url = f"{self.base_url}/orders/sell/byMaker"
        params = {"maker": maker}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_sell_orders_by_item(self, item_id: str):
        """
        Get sell orders by item.

        Args:
            item_id (str): The ID of the item.

        Returns:
            dict: Details of the sell orders for the specified item.
        """
        url = f"{self.base_url}/orders/sell/byItem"
        params = {"itemId": item_id}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
