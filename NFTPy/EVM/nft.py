import json
from .chains import Chains
from .abi import ABI
from enum import Enum
from web3 import Web3

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