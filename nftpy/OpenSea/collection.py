from .opensea import OpenSea, OpenSeaChain

class OpenSeaCollection:
    """
    A class built for collection specific interactions.
    """
    def __init__(self, api_key, collection_slug, chain: OpenSeaChain = OpenSeaChain.ETHEREUM):
        self._api_key = api_key
        self._collection_slug = collection_slug
        self._chain = chain
        self._api = OpenSea(api_key=api_key, chain=chain)

    def get_collection_stats(self):
        """
        Get statistics for the collection.

        Returns:
            dict: A dictionary containing collection statistics.
        """
        return self._api.get_collection_stats(self._collection_slug)

    def get_collection(self):
        """
        Get details of the collection.

        Returns:
            dict: A dictionary containing collection details.
        """
        return self._api.get_collection(self._collection_slug)

    def list_nfts_by_collection(self, cursor: str = None, limit: int = 50):
        """
        List NFTs in the collection.

        Args:
            cursor (str, optional): Cursor for pagination.
            limit (int, optional): Number of results to return (default is 50).

        Returns:
            dict: A dictionary containing the NFTs.
        """
        return self._api.list_nfts_by_collection(self._collection_slug, chain=self._chain, cursor=cursor, limit=limit)

    def get_traits(self):
        """
        Get traits of the collection.

        Returns:
            dict: A dictionary containing collection traits.
        """
        return self._api.get_traits(self._collection_slug)

    def get_all_listings_on_collection(self, cursor: str = None, limit: int = 50):
        """
        Get all listings of the collection.

        Args:
            cursor (str, optional): Cursor for pagination.
            limit (int, optional): Number of results to return (default is 50).

        Returns:
            dict: A dictionary containing the listings.
        """
        return self._api.get_all_listings_on_collection(self._collection_slug, chain=self._chain, cursor=cursor, limit=limit)

    def get_collection_slug(self):
        """
        Get the collection slug.

        Returns:
            str: The collection slug.
        """
        return self._collection_slug

    def get_chain(self):
        """
        Get the blockchain network.

        Returns:
            OpenSeaChain: The blockchain network.
        """
        return self._chain
