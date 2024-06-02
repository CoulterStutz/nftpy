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

    def get_orders_by_ids(self, order_ids: list):
        url = f"{self.base_url}/orders/byIds"
        params = {"ids": ",".join(order_ids)}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_orders_all(self):
        url = f"{self.base_url}/orders/all"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_all_sync(self):
        url = f"{self.base_url}/orders/all/sync"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_sell_orders_by_maker(self, maker: str):
        url = f"{self.base_url}/orders/sell/byMaker"
        params = {"maker": maker}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_sell_orders_by_item(self, item_id: str):
        url = f"{self.base_url}/orders/sell/byItem"
        params = {"itemId": item_id}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_sell_orders(self, status: str = None, maker: str = None, collection: str = None, token: str = None,
                        origin: str = None):
        """
        Get sell orders with optional filters.

        Args:
            status (str, optional): The status of the orders to filter by.
            maker (str, optional): The address of the maker to filter by.
            collection (str, optional): The collection to filter by.
            token (str, optional): The token address to filter by.
            origin (str, optional): The origin address to filter by.

        Returns:
            dict: Details of the sell orders.
        """
        url = f"{self.base_url}/orders/sell"
        params = {}
        if status:
            params["status"] = status
        if maker:
            params["maker"] = maker
        if collection:
            params["collection"] = collection
        if token:
            params["token"] = token
        if origin:
            params["origin"] = origin
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_order_bids_by_maker(self, maker: str):
        """
        Get order bids by maker.

        Args:
            maker (str): The address of the maker.

        Returns:
            dict: Details of the order bids by the specified maker.
        """
        url = f"{self.base_url}/orders/bids/byMaker"
        params = {"maker": maker}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_order_bids_by_item(self, item_id: str):
        """
        Get order bids by item.

        Args:
            item_id (str): The ID of the item.

        Returns:
            dict: Details of the order bids for the specified item.
        """
        url = f"{self.base_url}/orders/bids/byItem"
        params = {"itemId": item_id}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_order_floor_bids_by_collection(self, collection: str):
        """
        Get order floor bids by collection.

        Args:
            collection (str): The ID of the collection.

        Returns:
            dict: Details of the floor bids for the specified collection.
        """
        url = f"{self.base_url}/orders/bids/floorByCollection"
        params = {"collection": collection}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_amm_order_trade_info(self, order_id: str):
        """
        Get AMM order trade information by order ID.

        Args:
            order_id (str): The ID of the order.

        Returns:
            dict: Trade information of the specified AMM order.
        """
        url = f"{self.base_url}/orders/amm/tradeInfo/{order_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_order_fees(self, order_id: str):
        """
        Get fees for a specific order.

        Args:
            order_id (str): The ID of the order.

        Returns:
            dict: Fee details of the specified order.
        """
        url = f"{self.base_url}/orders/{order_id}/fees"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
