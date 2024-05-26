import json
from enum import Enum
from web3 import Web3
from chains import EVM

class ABI(Enum):
    ERC721 = json.load(open('EVM/erc721.json'))
    ERC1155 = json.load(open('EVM/erc1155.json'))

class NFT:
    def __init__(self, contract_address:str, network:EVM=EVM.ETH, rpc_url:str=None, abi:ABI=ABI.ERC721):
        self.contract_address = contract_address
        self.network = network
        self.abi = abi
        if rpc_url is None:
            self.web3 = Web3(Web3.HTTPProvider(network_urls[network]))
        else:
            self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        self.contract = self.web3.contract(self.contract_address, abi=abi)

    def get_balance(self, wallet_address:str) -> int:
        return self.contract.functions.balanceOf(wallet_address).call()
