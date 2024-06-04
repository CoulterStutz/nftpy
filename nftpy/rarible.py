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

    def get_collection_by_id(self, collection_id: str):
        """
        Get collection details by collection ID.

        Args:
            collection_id (str): The ID of the collection.

        Returns:
            dict: Details of the collection.
        """
        url = f"{self.base_url}/collections/{collection_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def generate_token_id(self, collection_id: str, minter: str):
        """
        Generate a unique token ID for a new item in a collection.

        Args:
            collection_id (str): The ID of the collection.
            minter (str): The address of the minter.

        Returns:
            dict: The generated token ID.
        """
        url = f"{self.base_url}/collections/{collection_id}/generateTokenId"
        params = {"minter": minter}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def refresh_collection_items_meta(self, collection_id: str):
        """
        Refresh metadata for all items within a collection.

        Args:
            collection_id (str): The ID of the collection.

        Returns:
            dict: Result of the refresh operation.
        """
        url = f"{self.base_url}/collections/{collection_id}/refresh"
        response = requests.post(url)
        response.raise_for_status()
        return response.json()

    def reset_collection_meta(self, collection_id: str):
        """
        Reset metadata for a specific collection.

        Args:
            collection_id (str): The ID of the collection.

        Returns:
            dict: Result of the reset operation.
        """
        url = f"{self.base_url}/collections/{collection_id}/reset"
        response = requests.post(url)
        response.raise_for_status()
        return response.json()

    def get_collections_by_owner(self, owner: str):
        """
        Get collections owned by a specific owner.

        Args:
            owner (str): The address of the owner.

        Returns:
            dict: Collections owned by the specified owner.
        """
        url = f"{self.base_url}/collections/owner/{owner}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_all_collections(self):
        """
        Get a list of all collections.

        Returns:
            dict: All collections.
        """
        url = f"{self.base_url}/collections"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_collection_ranking_by_volume(self, period: str = "DAY", size: int = 10):
        """
        Get collection ranking by trading volume.

        Args:
            period (str, optional): The period to filter by (DAY, WEEK, MONTH, etc.). Default is "DAY".
            size (int, optional): The number of collections to retrieve. Default is 10.

        Returns:
            dict: Ranking of collections by volume.
        """
        url = f"{self.base_url}/nft/collections/ranking/volume"
        params = {"period": period, "size": size}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_transactions(self, start_date: str = None, end_date: str = None, cursor: str = None, limit: int = 100):
        """
        Get a list of transactions with optional filters.

        Args:
            start_date (str, optional): The start date for filtering transactions.
            end_date (str, optional): The end date for filtering transactions.
            cursor (str, optional): Cursor for pagination.
            limit (int, optional): Number of transactions to retrieve. Default is 100.

        Returns:
            dict: List of transactions.
        """
        url = f"{self.base_url}/nft/transactions"
        params = {"startDate": start_date, "endDate": end_date, "cursor": cursor, "limit": limit}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_collection_stats(self, collection_id: str):
        """
        Get statistical data for a specific collection.

        Args:
            collection_id (str): The ID of the collection.

        Returns:
            dict: Statistical data of the collection.
        """
        url = f"{self.base_url}/nft/collections/{collection_id}/stats"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_sellers(self, size: int = 10):
        """
        Get top sellers.

        Args:
            size (int, optional): Number of top sellers to retrieve. Default is 10.

        Returns:
            dict: List of top sellers.
        """
        url = f"{self.base_url}/nft/sellers"
        params = {"size": size}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_buyers(self, size: int = 10):
        """
        Get top buyers.

        Args:
            size (int, optional): Number of top buyers to retrieve. Default is 10.

        Returns:
            dict: List of top buyers.
        """
        url = f"{self.base_url}/nft/buyers"
        params = {"size": size}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_listed(self, period: str = "DAY"):
        """
        Get listed items based on various filters.

        Args:
            period (str, optional): The period to filter by (DAY, WEEK, MONTH, etc.). Default is "DAY".

        Returns:
            dict: Listed items.
        """
        url = f"{self.base_url}/nft/listed"
        params = {"period": period}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_gmv(self, period: str = "DAY"):
        """
        Get gross merchandise volume data.

        Args:
            period (str, optional): The period to filter by (DAY, WEEK, MONTH, etc.). Default is "DAY".

        Returns:
            dict: Gross merchandise volume data.
        """
        url = f"{self.base_url}/nft/gmv"
        params = {"period": period}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_floor_price(self, collection_id: str):
        """
        Get the floor price for a collection.

        Args:
            collection_id (str): The ID of the collection.

        Returns:
            dict: Floor price of the collection.
        """
        url = f"{self.base_url}/nft/collections/{collection_id}/floorPrice"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_domain_info(self, domain: str):
        """
        Get information about a specific domain.

        Args:
            domain (str): The domain to lookup.

        Returns:
            dict: Information about the domain.
        """
        url = f"{self.base_url}/domains/{domain}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def validate_signature(self, data: dict):
        """
        Validate a provided signature.

        Args:
            data (dict): The data containing the signature and related information.

        Returns:
            dict: Result of the validation.
        """
        url = f"{self.base_url}/signature/validate"
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def get_signature_input(self, data: dict):
        """
        Get input data used to create a signature.

        Args:
            data (dict): The data containing the signature and related information.

        Returns:
            dict: The input data used for the signature.
        """
        url = f"{self.base_url}/signature/input"
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def encode_data(self, data: dict):
        """
        Encode data for use in blockchain transactions.

        Args:
            data (dict): The data to encode.

        Returns:
            dict: The encoded data.
        """
        url = f"{self.base_url}/encode"
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def get_usd_rate(self, currency: str):
        """
        Get the exchange rate between a specified currency and USD.

        Args:
            currency (str): The currency to get the exchange rate for.

        Returns:
            dict: The exchange rate information.
        """
        url = f"{self.base_url}/rates/{currency}/usd"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_all_currencies(self):
        """
        Get all supported currencies and their exchange rates.

        Returns:
            dict: All supported currencies and their exchange rates.
        """
        url = f"{self.base_url}/currencies"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_user_balance(self, user: str, currency: str):
        """
        Get the balance of a specific user for a given currency.

        Args:
            user (str): The user to get the balance for.
            currency (str): The currency to get the balance in.

        Returns:
            dict: The user's balance.
        """
        url = f"{self.base_url}/balances/{user}/{currency}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

class RaribleCollection:
    """
    A class built for collection specific interactions.
    """
    def __init__(self, api_key, collection_id, chain: RaribleChain = RaribleChain.ETHEREUM):
        self.api_key = api_key
        self.collection_id = collection_id
        self.chain = chain
        self.api = Rarible(chain=chain)

    def get_items_by_collection(self):
        """
        Get items in the specific collection.

        Returns:
            dict: Items in the specified collection.
        """
        return self.api.get_items_by_collection(self.collection_id)

    def query_traits(self):
        """
        Query traits of items in the specific collection.

        Returns:
            dict: Traits of items in the specified collection.
        """
        return self.api.query_traits(self.collection_id)

    def get_ownerships_by_collection(self):
        """
        Get ownerships in the specific collection.

        Returns:
            dict: Ownerships in the specified collection.
        """
        return self.api.get_ownerships_by_collection(self.collection_id)

    def get_collection_by_id(self):
        """
        Get details of the specific collection.

        Returns:
            dict: Details of the collection.
        """
        return self.api.get_collection_by_id(self.collection_id)

    def generate_token_id(self, minter: str):
        """
        Generate a unique token ID for a new item in the collection.

        Args:
            minter (str): The address of the minter.

        Returns:
            dict: The generated token ID.
        """
        return self.api.generate_token_id(self.collection_id, minter)

    def refresh_collection_items_meta(self):
        """
        Refresh metadata for all items within the collection.

        Returns:
            dict: Result of the refresh operation.
        """
        return self.api.refresh_collection_items_meta(self.collection_id)

    def reset_collection_meta(self):
        """
        Reset metadata for the specific collection.

        Returns:
            dict: Result of the reset operation.
        """
        return self.api.reset_collection_meta(self.collection_id)

    def get_collection_stats(self):
        """
        Get statistical data for the specific collection.

        Returns:
            dict: Statistical data of the collection.
        """
        return self.api.get_collection_stats(self.collection_id)

    def get_floor_price(self):
        """
        Get the floor price for the collection.

        Returns:
            dict: Floor price of the collection.
        """
        return self.api.get_floor_price(self.collection_id)

class RaribleWallet:
    """
    A class built for wallet specific interactions.
    """
    def __init__(self, api_key, wallet: str, chain: RaribleChain = RaribleChain.ETHEREUM):
        self.api_key = api_key
        self.wallet = wallet
        self.chain = chain
        self.api = Rarible(chain=chain)

    def get_items_by_owner(self):
        """
        Get items owned by the wallet owner.

        Returns:
            dict: Items owned by the specified owner.
        """
        return self.api.get_items_by_owner(self._wallet)

    def get_collections_with_owned_items(self):
        """
        Get collections with items owned by the wallet owner.

        Returns:
            dict: Collections with items owned by the specified owner.
        """
        return self.api.get_collections_with_owned_items(self._wallet)

    def get_user_balance(self, currency: str):
        """
        Get the balance of the wallet owner for a given currency.

        Args:
            currency (str): The currency to get the balance in.

        Returns:
            dict: The user's balance.
        """
        return self.api.get_user_balance(self._wallet, currency)
