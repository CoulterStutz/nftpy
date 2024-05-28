import json
import requests
from .chains import Chains
from .abi import ABI
from enum import Enum
from web3 import Web3
from ..errors import *


class NFT:
    def __init__(self, contract_address: str, network: Chains = Chains.ETH, rpc_url: str = None, abi: ABI = ABI.ERC721):
        """
        Creates an Object Interface for interaction with a contract on chain

        Args:
            contract_address (str): The address of the NFT contract.
            network (Chains): The blockchain network on which the contract is deployed (ex. Chains.ETH).
            rpc_url (str): Optional custom RPC URL. If not provided, the default URL for the network will be used.
            abi (ABI): The ABI of the contract.
        """
        self.contract_address = contract_address
        self.network = network
        self.abi = abi.value
        if rpc_url is None:
            self.web3 = Web3(Web3.HTTPProvider(self.network.rpc_url))
        else:
            self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.abi)

    def get_balance(self, wallet_address: str) -> int:
        """
        Get the balance of tokens owned by a specific wallet address.

        Args:
            wallet_address (str): The address of the wallet.

        Returns:
            int: The balance of tokens.
        """
        try:
            return self.contract.functions.balanceOf(wallet_address).call()
        except Exception as e:
            raise ContractFunctionFailedError('balanceOf') from e

    def get_token_uri(self, token_id: int) -> str:
        """
        Get the URI of a specific token.

        Args:
            token_id (int): The ID of the token.

        Returns:
            str: The URI of the token.
        """
        try:
            return self.contract.functions.tokenURI(token_id).call()
        except Exception as e:
            raise ContractFunctionFailedError('tokenURI') from e

    def get_owner(self, token_id: int) -> str:
        """
        Get the owner of a specific token.

        Args:
            token_id (int): The ID of the token.

        Returns:
            str: The address of the owner.
        """
        try:
            return self.contract.functions.ownerOf(token_id).call()
        except Exception as e:
            raise ContractFunctionFailedError('ownerOf') from e

    def get_approved(self, token_id: int) -> str:
        """
        Get the approved address for a specific ERC721 token.

        Args:
            token_id (int): The ID of the token.

        Returns:
            str: The address that is approved for the token.
        """
        try:
            return self.contract.functions.getApproved(token_id).call()
        except Exception as e:
            raise ContractFunctionFailedError('getApproved') from e

    def is_approved_for_all(self, owner_address: str, operator_address: str) -> bool:
        """
        Check if an address is approved for all tokens owned by another address (ERC721).

        Args:
            owner_address (str): The address of the token owner.
            operator_address (str): The address of the operator.

        Returns:
            bool: True if the operator is approved for all tokens, False otherwise.
        """
        try:
            return self.contract.functions.isApprovedForAll(owner_address, operator_address).call()
        except Exception as e:
            raise ContractFunctionFailedError('isApprovedForAll') from e

    def get_token_metadata(self, token_id: int) -> dict:
        """
        Get the metadata for a specific ERC721 token.
        This assumes the tokenURI returns a URL that points to a JSON metadata file.

        Args:
            token_id (int): The ID of the token.

        Returns:
            dict: The metadata of the token.
        """
        try:
            token_uri = self.get_token_uri(token_id)
            response = requests.get(token_uri)
            return response.json()
        except Exception as e:
            raise ContractFunctionFailedError('get_token_metadata') from e

    def get_tokens_balance(self, wallet_address: str, token_ids: list) -> dict:
        """
        Get the balance of multiple ERC1155 tokens for a specific wallet address.

        Args:
            wallet_address (str): The address of the wallet.
            token_ids (list): A list of token IDs.

        Returns:
            dict: A dictionary where the key is the token ID and the value is the balance.
        """
        try:
            balances = self.contract.functions.balanceOfBatch([wallet_address] * len(token_ids), token_ids).call()
            return {token_id: balance for token_id, balance in zip(token_ids, balances)}
        except Exception as e:
            raise ContractFunctionFailedError('balanceOfBatch') from e

    def is_approved_for_all_erc1155(self, owner_address: str, operator_address: str) -> bool:
        """
        Check if an address is approved for all tokens owned by another address (ERC1155).

        Args:
            owner_address (str): The address of the token owner.
            operator_address (str): The address of the operator.

        Returns:
            bool: True if the operator is approved for all tokens, False otherwise.
        """
        try:
            return self.contract.functions.isApprovedForAll(owner_address, operator_address).call()
        except Exception as e:
            raise ContractFunctionFailedError('isApprovedForAll') from e

    def get_token_balance(self, wallet_address: str, token_id: int) -> int:
        """
        Get the balance of a specific ERC1155 token for a specific wallet address.

        Args:
            wallet_address (str): The address of the wallet.
            token_id (int): The ID of the token.

        Returns:
            int: The balance of the token.
        """
        try:
            return self.contract.functions.balanceOf(wallet_address, token_id).call()
        except Exception as e:
            raise ContractFunctionFailedError('balanceOf') from e
