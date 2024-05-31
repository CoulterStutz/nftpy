from enum import Enum

class Chain:
    def __init__(self, name:str, chain_id:int, rpc_url:str, symbol:str="ETH", explorer_url:str=None, testnet:bool=False):
        self.name = name
        self.symbol = symbol
        self.chain_id = chain_id
        self.rpc_url = rpc_url
        self.explorer_url = explorer_url
        self.testnet = testnet

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
    BASE = {
        "chain_id": 8453,
        "name": "Base",
        "rpc_url": "https://mainnet.base.org",
        "explorer_url": "https://basescan.org"
    }

    # ETH TESTNETS

    ETH_SEPOLIA = {
        "chain_id": 11155111,
        "name": "Sepolia Testnet",
        "rpc_url": "https://rpc.sepolia.org",
        "explorer_url": "https://sepolia.etherscan.io"
    }

    ETH_HOLESKY = {
        "chain_id": 17000,
        "name": "Holešky Testnet",
        "rpc_url": "https://ethereum-holesky.publicnode.com",
        "explorer_url": "https://holesky.beaconcha.in"
    }

    # BSC TESTNETS

    BSC_TESTNET = {
        "chain_id": 97,
        "name": "BSC Testnet",
        "rpc_url": "https://data-seed-prebsc-1-s1.binance.org:8545/",
        "explorer_url": "https://testnet.bscscan.com"
    }

    # POLYGON TESTNETS

    POLYGON_MUMBAI = {
        "chain_id": 80001,
        "name": "Polygon Mumbai Testnet",
        "rpc_url": "https://polygon-mumbai.api.onfinality.io/public",
        "explorer_url": "https://mumbai.polygonscan.com"
    }

    POLYGON_AMOY = {
        "chain_id": 80002,
        "name": "Polygon Amoy Testnet",
        "rpc_url": "https://rpc-amoy.polygon.technology",
        "explorer_url": "https://oklink.com/amoy"
    }

    POLYGON_CARDONA = {
        "chain_id": 2442,
        "name": "Polygon zkEVM Cardona Testnet",
        "rpc_url": "https://rpc.cardona.zkevm-rpc.com",
        "explorer_url": "https://cardona-zkevm.polygonscan.com"
    }

    # AVALANCHE TESTNETS

    AVALANCHE_FUJI = {
        "chain_id": 43113,
        "name": "Avalanche Fuji Testnet",
        "rpc_url": "https://api.avax-test.network/ext/bc/C/rpc",
        "explorer_url": "https://testnet.snowtrace.io"
    }

    # FANTOM TESTNETS

    FANTOM_TESTNET = {
        "chain_id": 4002,
        "name": "Fantom Testnet",
        "rpc_url": "https://rpc.testnet.fantom.network",
        "explorer_url": "https://testnet.ftmscan.com"
    }

    # ARBITRUM TESTNETS

    ARBITRUM_NOVA = {
        "chain_id": 421611,
        "name": "Arbitrum Nova",
        "rpc_url": "https://nova.arbitrum.io/rpc",
        "explorer_url": "https://nova.arbiscan.io"
    }

    # OPTIMISM TESTNETS

    OPTIMISM_GOERLI = {
        "chain_id": 420,
        "name": "Optimism Goerli",
        "rpc_url": "https://optimism-goerli.public.blastapi.io",
        "explorer_url": "https://goerli-explorer.optimism.io"
    }

    # CELO TESTNETS

    CELO_ALFAJORES = {
        "chain_id": 44787,
        "name": "Celo Alfajores Testnet",
        "rpc_url": "https://alfajores-forno.celo-testnet.org",
        "explorer_url": "https://alfajores-blockscout.celo-testnet.org"
    }

    CELO_BAKLAVA = {
        "chain_id": 62320,
        "name": "Celo Baklava Testnet",
        "rpc_url": "https://baklava-forno.celo-testnet.org",
        "explorer_url": "https://baklava-blockscout.celo-testnet.org"
    }

    # CRONOS TESTNETS

    CRONOS_TESTNET = {
        "chain_id": 338,
        "name": "Cronos Testnet",
        "rpc_url": "https://evm-t3.cronos.org",
        "explorer_url": "https://testnet.cronoscan.com"
    }

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