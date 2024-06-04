from .rarible import Rarible, RaribleChain

class RaribleCollection:
    """
    A class built for collection specific interactions.
    """
    def __init__(self, api_key, collection_id, chain: RaribleChain = RaribleChain.ETHEREUM):
        self._api_key = api_key
        self._collection_id = collection_id
        self._chain = chain
        self._api = Rarible(chain=chain)

    def get_items_by_collection(self):
        """
        Get items in the specific collection.

        Returns:
            dict: Items in the specified collection.
        """
        return self._api.get_items_by_collection(self._collection_id)

    def query_traits(self):
        """
        Query traits of items in the specific collection.

        Returns:
            dict: Traits of items in the specified collection.
        """
        return self._api.query_traits(self._collection_id)

    def get_ownerships_by_collection(self):
        """
        Get ownerships in the specific collection.

        Returns:
            dict: Ownerships in the specified collection.
        """
        return self._api.get_ownerships_by_collection(self._collection_id)

    def get_collection_by_id(self):
        """
        Get details of the specific collection.

        Returns:
            dict: Details of the collection.
        """
        return self._api.get_collection_by_id(self._collection_id)

    def generate_token_id(self, minter: str):
        """
        Generate a unique token ID for a new item in the collection.

        Args:
            minter (str): The address of the minter.

        Returns:
            dict: The generated token ID.
        """
        return self._api.generate_token_id(self._collection_id, minter)

    def refresh_collection_items_meta(self):
        """
        Refresh metadata for all items within the collection.

        Returns:
            dict: Result of the refresh operation.
        """
        return self._api.refresh_collection_items_meta(self._collection_id)

    def reset_collection_meta(self):
        """
        Reset metadata for the specific collection.

        Returns:
            dict: Result of the reset operation.
        """
        return self._api.reset_collection_meta(self._collection_id)

    def get_collection_stats(self):
        """
        Get statistical data for the specific collection.

        Returns:
            dict: Statistical data of the collection.
        """
        return self._api.get_collection_stats(self._collection_id)

    def get_floor_price(self):
        """
        Get the floor price for the collection.

        Returns:
            dict: Floor price of the collection.
        """
        return self._api.get_floor_price(self._collection_id)

    def get_collection_id(self):
        """
        Get the collection ID.

        Returns:
            str: The collection ID.
        """
        return self._collection_id

    def get_chain(self):
        """
        Get the blockchain network.

        Returns:
            RaribleChain: The blockchain network.
        """
        return self._chain