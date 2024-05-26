from enum import Enum
from web3 import Web3

class EVM(Enum):
    ETH = 0
    BSC = 1          # Binance Smart Chain
    POLYGON = 2      # Polygon (formerly Matic)
    AVALANCHE = 3    # Avalanche C-Chain
    FANTOM = 4       # Fantom Opera
    ARBITRUM = 5     # Arbitrum One
    OPTIMISM = 6     # Optimism
    MOONBEAM = 7     # Moonbeam
    KLAYTN = 8       # Klaytn
    CELO = 9         # Celo
    HECO = 10        # Huobi ECO Chain
    CRONOS = 11      # Cronos
    METIS = 12       # Metis Andromeda
    BOBA = 13        # Boba Network
    RSK = 14         # Rootstock (RSK)
    XDAI = 15        # Gnosis Chain (formerly xDai)


network_urls = {
    EVM.ETH: "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID",
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
    def __init__(self, contract_address, network:EVM=EVM.ETH, rpc_url:str=None):
        self.contract_address = contract_address
        self.network = network
        if rpc_url is None:
            self.web3 = Web3(Web3.HTTPProvider(network_urls[network]))
        else:
            self.web3 = Web3(Web3.HTTPProvider(rpc_url))

