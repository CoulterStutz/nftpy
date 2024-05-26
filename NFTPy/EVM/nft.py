import json
from .chains import Chains
from enum import Enum
from web3 import Web3

class ABI(Enum):
    ERC721 = json.load(open('erc721.json'))
    ERC1155 = json.load(open('erc1155.json'))

class NFT:
    def __init__(self, contract_address: str, network:Chains = Chains.ETH, rpc_url: str = None, abi: ABI = ABI.ERC721):
        self.contract_address = contract_address
        self.network = network
        self.abi = abi.value
        if rpc_url is None:
            self.web3 = Web3(Web3.HTTPProvider(self.network.rpc_url))
        else:
            self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.abi)

    def get_balance(self, wallet_address: str) -> int:
        return self.contract.functions.balanceOf(wallet_address).call()

    def get_token_uri(self, token_id: int) -> str:
        return self.contract.functions.tokenURI(token_id).call()

    def get_owner(self, token_id: int) -> str:
        return self.contract.functions.ownerOf(token_id).call()
        
    def get_tokens(self, wallet_address: str) -> int:
        """
        Get the balance of ERC-721 tokens for a specific wallet address.

        Parameters:
        wallet_address (str): The address of the wallet to check the balance for.

        Returns:
        int: The balance of tokens.
        """
        return self.contract.functions.balanceOf(wallet_address).call()
