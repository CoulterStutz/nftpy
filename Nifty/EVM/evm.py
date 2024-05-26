from enum import Enum
from web3 import Web3

class EVM(Enum):
    ETH = 1            # Ethereum Mainnet
    BSC = 56           # Binance Smart Chain
    POLYGON = 137      # Polygon (formerly Matic)
    AVALANCHE = 43114  # Avalanche C-Chain
    FANTOM = 250       # Fantom Opera
    ARBITRUM = 42161   # Arbitrum One
    OPTIMISM = 10      # Optimism
    MOONBEAM = 1284    # Moonbeam
    KLAYTN = 8217      # Klaytn
    CELO = 42220       # Celo
    HECO = 128         # Huobi ECO Chain
    CRONOS = 25        # Cronos
    METIS = 1088       # Metis Andromeda
    BOBA = 288         # Boba Network
    RSK = 30           # Rootstock (RSK)
    XDAI = 100         # Gnosis Chain (formerly xDai)

class ABI(Enum):
    ERC721 = json.load(open('EVM/erc721.json'))
    ERC1155 = json.load(open('EVM/erc1155.json'))

network_urls = {
    EVM.ETH: "https://eth.llamarpc.com",
    EVM.BSC: "https://bsc-dataseed.binance.org/",
    EVM.POLYGON: "https://polygon-rpc.com/",
    EVM.AVALANCHE: "https://api.avax.network/ext/bc/C/rpc",
    EVM.FANTOM: "https://rpc.ftm.tools/",
    EVM.ARBITRUM: "https://arb1.arbitrum.io/rpc",
    EVM.OPTIMISM: "https://mainnet.optimism.io",
    EVM.MOONBEAM: "https://rpc.api.moonbeam.network",
    EVM.KLAYTN: "https://public-node-api.klaytnapi.com/v1/cypress",
    EVM.CELO: "https://forno.celo.org",
    EVM.HECO: "https://http-mainnet.hecochain.com",
    EVM.CRONOS: "https://evm-cronos.crypto.org",
    EVM.METIS: "https://andromeda.metis.io/?owner=1088",
    EVM.BOBA: "https://mainnet.boba.network",
    EVM.RSK: "https://public-node.rsk.co",
    EVM.XDAI: "https://rpc.xdaichain.com/"
}

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