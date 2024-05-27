from enum import Enum

class Chains(Enum):
    ETH = {
        "chain_id": 1,
        "name": "Ethereum Mainnet",
        "rpc_url": "https://eth.llamarpc.com",
        "explorer_url": "https://etherscan.io"
    }
    BSC = {
        "chain_id": 56,
        "name": "Binance Smart Chain",
        "rpc_url": "https://bsc-dataseed.binance.org/",
        "explorer_url": "https://bscscan.com"
    }
    POLYGON = {
        "chain_id": 137,
        "name": "Polygon (Matic)",
        "rpc_url": "https://polygon-rpc.com/",
        "explorer_url": "https://polygonscan.com"
    }
    AVALANCHE = {
        "chain_id": 43114,
        "name": "Avalanche C-Chain",
        "rpc_url": "https://api.avax.network/ext/bc/C/rpc",
        "explorer_url": "https://snowtrace.io"
    }
    FANTOM = {
        "chain_id": 250,
        "name": "Fantom Opera",
        "rpc_url": "https://rpc.ftm.tools/",
        "explorer_url": "https://ftmscan.com"
    }
    ARBITRUM = {
        "chain_id": 42161,
        "name": "Arbitrum One",
        "rpc_url": "https://arb1.arbitrum.io/rpc",
        "explorer_url": "https://arbiscan.io"
    }
    OPTIMISM = {
        "chain_id": 10,
        "name": "Optimism",
        "rpc_url": "https://mainnet.optimism.io",
        "explorer_url": "https://optimistic.etherscan.io"
    }
    MOONBEAM = {
        "chain_id": 1284,
        "name": "Moonbeam",
        "rpc_url": "https://rpc.api.moonbeam.network",
        "explorer_url": "https://moonscan.io"
    }
    CELO = {
        "chain_id": 42220,
        "name": "Celo",
        "rpc_url": "https://forno.celo.org",
        "explorer_url": "https://explorer.celo.org"
    }
    CRONOS = {
        "chain_id": 25,
        "name": "Cronos",
        "rpc_url": "https://evm-cronos.crypto.org",
        "explorer_url": "https://cronoscan.com"
    }
    METIS = {
        "chain_id": 1088,
        "name": "Metis Andromeda",
        "rpc_url": "https://andromeda.metis.io/?owner=1088",
        "explorer_url": "https://andromeda-explorer.metis.io"
    }
    BOBA = {
        "chain_id": 288,
        "name": "Boba Network",
        "rpc_url": "https://mainnet.boba.network",
        "explorer_url": "https://bobascan.com"
    }
    RSK = {
        "chain_id": 30,
        "name": "Rootstock (RSK)",
        "rpc_url": "https://public-node.rsk.co",
        "explorer_url": "https://explorer.rsk.co"
    }
    XDAI = {
        "chain_id": 100,
        "name": "Gnosis Chain (formerly xDai)",
        "rpc_url": "https://rpc.xdaichain.com/",
        "explorer_url": "https://blockscout.com/xdai/mainnet"
    }
    MUMBAI = {
        "chain_id": 80001,
        "name": "Mumbai",
        "rpc_url": "https://rpc-mumbai.maticvigil.com",
        "explorer_url": "https://mumbai.polygonscan.com"
    }
    GOERLI = {
        "chain_id": 5,
        "name": "Goerli",
        "rpc_url": "https://rpc.goerli.mudit.blog",
        "explorer_url": "https://goerli.etherscan.io"
    }
    BASE = {
        "chain_id": 8453,
        "name": "Base",
        "rpc_url": "https://mainnet.base.org",
        "explorer_url": "https://basescan.org"
    }
    BNB = {
        "chain_id": 97,
        "name": "BNB",
        "rpc_url": "https://data-seed-prebsc-1-s1.binance.org:8545/",
        "explorer_url": "https://testnet.bscscan.com"
    }
    SCROLL_ALPHA = {
        "chain_id": 534353,
        "name": "Scroll Alpha",
        "rpc_url": "https://alpha-rpc.scroll.io/l2",
        "explorer_url": "https://blockscout.scroll.io"
    }

    # ADD CUSTOM CHAINS HERE

    @property
    def chain_id(self):
        return self.value["chain_id"]

    @property
    def name(self):
        return self.value["name"]

    @property
    def rpc_url(self):
        return self.value["rpc_url"]

    @property
    def explorer_url(self):
        return self.value["explorer_url"]
