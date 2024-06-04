from enum import Enum
import requests

from ..errors import MissingItemIdError, MissingChainError, APIRequestFailedError, MissingCollectionIdError

class RaribleChain(Enum):
    ETHEREUM = "ETHEREUM"
    POLYGON = "POLYGON"

class Rarible:
    def __init__(self, api_key: str, chain: RaribleChain):
        self.api_key = api_key
        self.chain = chain
        self.base_url = "https://api.rarible.org/v0.1"

    def _get_headers(self):
        return {
            "Accept": "application/json",
            "X-API-KEY": self.api_key
        }

    def get_item_by_id(self, item_id: str):
        if not item_id:
            raise MissingItemIdError()
        url = f"{self.base_url}/items/{item_id}"
        response = requests.get(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_items_by_ids(self, item_ids: list):
        if not item_ids:
            raise MissingItemIdError()
        url = f"{self.base_url}/items/byIds"
        params = {"ids": ",".join(item_ids)}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        response.raise_for_status()
        return response.json()

    def get_item_royalties_by_id(self, item_id: str):
        if not item_id:
            raise MissingItemIdError()
        url = f"{self.base_url}/items/{item_id}/royalties"
        response = requests.get(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_items_by_owner(self, owner: str):
        if not owner:
            raise ValueError("Owner address must be provided.")
        url = f"{self.base_url}/items/byOwner"
        params = {"owner": owner}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_items_by_creator(self, creator: str):
        if not creator:
            raise ValueError("Creator address must be provided.")
        url = f"{self.base_url}/items/byCreator"
        params = {"creator": creator}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_items_by_collection(self, collection: str):
        if not collection:
            raise MissingCollectionIdError()
        url = f"{self.base_url}/items/byCollection"
        params = {"collection": collection}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def query_traits(self, collection: str):
        if not collection:
            raise MissingCollectionIdError()
        url = f"{self.base_url}/items/traits"
        params = {"collection": collection}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_lazy_item_by_id(self, item_id: str):
        if not item_id:
            raise MissingItemIdError()
        url = f"{self.base_url}/items/{item_id}/lazy"
        response = requests.get(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def burn_lazy_item(self, item_id: str):
        if not item_id:
            raise MissingItemIdError()
        url = f"{self.base_url}/items/{item_id}/lazy/burn"
        response = requests.post(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_ownership_by_id(self, ownership_id: str):
        if not ownership_id:
            raise ValueError("Ownership ID must be provided.")
        url = f"{self.base_url}/ownerships/{ownership_id}"
        response = requests.get(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_ownerships_by_ids(self, ownership_ids: list):
        if not ownership_ids:
            raise ValueError("Ownership IDs must be provided.")
        url = f"{self.base_url}/ownerships/byIds"
        params = {"ids": ",".join(ownership_ids)}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_ownerships_by_collection(self, collection: str):
        if not collection:
            raise MissingCollectionIdError()
        url = f"{self.base_url}/ownerships/byCollection"
        params = {"collection": collection}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_ownerships_by_item(self, item_id: str):
        if not item_id:
            raise MissingItemIdError()
        url = f"{self.base_url}/ownerships/byItem"
        params = {"itemId": item_id}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_collections_with_owned_items(self, owner: str):
        if not owner:
            raise ValueError("Owner address must be provided.")
        url = f"{self.base_url}/ownerships/collectionsWithOwnedItems"
        params = {"owner": owner}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_orders_by_ids(self, order_ids: list):
        if not order_ids:
            raise ValueError("Order IDs must be provided.")
        url = f"{self.base_url}/orders/byIds"
        params = {"ids": ",".join(order_ids)}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_orders_all(self):
        url = f"{self.base_url}/orders/all"
        response = requests.get(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_all_sync(self):
        url = f"{self.base_url}/orders/all/sync"
        response = requests.get(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_sell_orders_by_maker(self, maker: str):
        if not maker:
            raise ValueError("Maker address must be provided.")
        url = f"{self.base_url}/orders/sell/byMaker"
        params = {"maker": maker}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_sell_orders_by_item(self, item_id: str):
        if not item_id:
            raise MissingItemIdError()
        url = f"{self.base_url}/orders/sell/byItem"
        params = {"itemId": item_id}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_sell_orders(self, status: str = None, maker: str = None, collection: str = None, token: str = None,
                        origin: str = None):
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
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_order_bids_by_maker(self, maker: str):
        if not maker:
            raise ValueError("Maker address must be provided.")
        url = f"{self.base_url}/orders/bids/byMaker"
        params = {"maker": maker}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_order_bids_by_item(self, item_id: str):
        if not item_id:
            raise MissingItemIdError()
        url = f"{self.base_url}/orders/bids/byItem"
        params = {"itemId": item_id}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_order_floor_bids_by_collection(self, collection: str):
        if not collection:
            raise MissingCollectionIdError()
        url = f"{self.base_url}/orders/bids/floorByCollection"
        params = {"collection": collection}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_amm_order_trade_info(self, order_id: str):
        if not order_id:
            raise ValueError("Order ID must be provided.")
        url = f"{self.base_url}/orders/amm/tradeInfo/{order_id}"
        response = requests.get(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_order_fees(self, order_id: str):
        if not order_id:
            raise ValueError("Order ID must be provided.")
        url = f"{self.base_url}/orders/{order_id}/fees"
        response = requests.get(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_collection_by_id(self, collection_id: str):
        if not collection_id:
            raise MissingCollectionIdError()
        url = f"{self.base_url}/collections/{collection_id}"
        response = requests.get(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def generate_token_id(self, collection_id: str, minter: str):
        if not collection_id:
            raise MissingCollectionIdError()
        if not minter:
            raise ValueError("Minter address must be provided.")
        url = f"{self.base_url}/collections/{collection_id}/generateTokenId"
        params = {"minter": minter}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def refresh_collection_items_meta(self, collection_id: str):
        if not collection_id:
            raise MissingCollectionIdError()
        url = f"{self.base_url}/collections/{collection_id}/refresh"
        response = requests.post(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def reset_collection_meta(self, collection_id: str):
        if not collection_id:
            raise MissingCollectionIdError()
        url = f"{self.base_url}/collections/{collection_id}/reset"
        response = requests.post(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_collections_by_owner(self, owner: str):
        if not owner:
            raise ValueError("Owner address must be provided.")
        url = f"{self.base_url}/collections/owner/{owner}"
        response = requests.get(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_all_collections(self):
        url = f"{self.base_url}/collections"
        response = requests.get(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_collection_ranking_by_volume(self, period: str = "DAY", size: int = 10):
        url = f"{self.base_url}/nft/collections/ranking/volume"
        params = {"period": period, "size": size}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_transactions(self, start_date: str = None, end_date: str = None, cursor: str = None, limit: int = 100):
        url = f"{self.base_url}/nft/transactions"
        params = {"startDate": start_date, "endDate": end_date, "cursor": cursor, "limit": limit}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_collection_stats(self, collection_id: str):
        if not collection_id:
            raise MissingCollectionIdError()
        url = f"{self.base_url}/nft/collections/{collection_id}/stats"
        response = requests.get(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_sellers(self, size: int = 10):
        url = f"{self.base_url}/nft/sellers"
        params = {"size": size}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_buyers(self, size: int = 10):
        url = f"{self.base_url}/nft/buyers"
        params = {"size": size}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_listed(self, period: str = "DAY"):
        url = f"{self.base_url}/nft/listed"
        params = {"period": period}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_gmv(self, period: str = "DAY"):
        url = f"{self.base_url}/nft/gmv"
        params = {"period": period}
        response = requests.get(url, headers=self._get_headers(), params=params)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_floor_price(self, collection_id: str):
        if not collection_id:
            raise MissingCollectionIdError()
        url = f"{self.base_url}/nft/collections/{collection_id}/floorPrice"
        response = requests.get(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_domain_info(self, domain: str):
        if not domain:
            raise ValueError("Domain must be provided.")
        url = f"{self.base_url}/domains/{domain}"
        response = requests.get(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def validate_signature(self, data: dict):
        url = f"{self.base_url}/signature/validate"
        response = requests.post(url, headers=self._get_headers(), json=data)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_signature_input(self, data: dict):
        url = f"{self.base_url}/signature/input"
        response = requests.post(url, headers=self._get_headers(), json=data)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def encode_data(self, data: dict):
        url = f"{self.base_url}/encode"
        response = requests.post(url, headers=self._get_headers(), json=data)
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_usd_rate(self, currency: str):
        if not currency:
            raise ValueError("Currency must be provided.")
        url = f"{self.base_url}/rates/{currency}/usd"
        response = requests.get(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_all_currencies(self):
        url = f"{self.base_url}/currencies"
        response = requests.get(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()

    def get_user_balance(self, user: str, currency: str):
        if not user or not currency:
            raise ValueError("User and currency must be provided.")
        url = f"{self.base_url}/balances/{user}/{currency}"
        response = requests.get(url, headers=self._get_headers())
        if response.status_code != 200:
            raise APIRequestFailedError(response.status_code)
        return response.json()
