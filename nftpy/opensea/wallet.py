from .opensea import OpenSea, OpenSeaChain

class OpenSeaWallet:
    """
    A class built for wallet specific interactions.
    """
    def __init__(self, api_key, wallet: str, chain: OpenSeaChain = OpenSeaChain.ETHEREUM):
        self._api_key = api_key
        self._wallet = wallet
        self._chain = chain
        self._api = OpenSea(api_key=api_key, chain=chain)

    def list_nfts_by_account(self, cursor: str = None, limit: int = 50):
        """
        List NFTs owned by the wallet.

        Args:
            cursor (str, optional): Cursor for pagination.
            limit (int, optional): Number of results to return (default is 50).

        Returns:
            dict: A dictionary containing the NFTs.
        """
        return self._api.list_nfts_by_account(self._wallet, chain=self._chain, cursor=cursor, limit=limit)

    def get_wallet(self):
        """
        Get the wallet address.

        Returns:
            str: The wallet address.
        """
        return self._wallet

    def get_chain(self):
        """
        Get the blockchain network.

        Returns:
            OpenSeaChain: The blockchain network.
        """
        return self._chain
