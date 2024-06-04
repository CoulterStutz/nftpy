from .rarible import Rarible, RaribleChain


class RaribleWallet:
    """
    A class built for wallet specific interactions on Rareable.
    """
    def __init__(self, api_key, wallet: str, chain: RaribleChain = RaribleChain.ETHEREUM):
        self._api_key = api_key
        self._wallet = wallet
        self._chain = chain
        self._api = Rarible(api_key=api_key, chain=chain)

    def get_owned_items(self):
        """
        Get items owned by the wallet owner.

        Returns:
            dict: Items owned by the specified owner.
        """
        return self._api.get_items_by_owner(self._wallet)

    def get_collections_with_owned_items(self):
        """
        Get collections with items owned by the wallet owner.

        Returns:
            dict: Collections with items owned by the specified owner.
        """
        return self._api.get_collections_with_owned_items(self._wallet)

    def get_user_balance(self, currency: str):
        """
        Get the balance of the wallet owner for a given currency.

        Args:
            currency (str): The currency to get the balance in.

        Returns:
            dict: The user's balance.
        """
        return self._api.get_user_balance(self._wallet, currency)

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
            RaribleChain: The blockchain network.
        """
        return self._chain