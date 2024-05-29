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
    BASE = {
        "chain_id": 8453,
        "name": "Base",
        "rpc_url": "https://mainnet.base.org",
        "explorer_url": "https://basescan.org"
    }
    ETH_SEPOLIA = {
        "chain_id": 11155111,
        "name": "Sepolia Testnet",
        "rpc_url": "https://rpc.sepolia.org",
        "explorer_url": "https://sepolia.etherscan.io"
    }
    HOLESKY = {
        "chain_id": 17000,
        "name": "Holešky Testnet",
        "rpc_url": "https://rpc.holesky.eth",
        "explorer_url": "https://holesky.etherscan.io"
    }

    def __init__(self, params):
        self.chain_id = params["chain_id"]
        self.rpc_url = params["rpc_url"]
        self.explorer_url = params["explorer_url"]
        self.name = params["name"]

    @classmethod
    def custom_chain(cls, chain_id: int, rpc_url: str, explorer_url: str, name: str) -> Enum:
        """
        Create a custom chain with the specified chain ID, RPC URL, explorer URL, and name.

        Args:
            chain_id (int): The chain ID for the custom chain.
            rpc_url (str): The RPC URL for the custom chain.
            explorer_url (str): The explorer URL for the custom chain.
            name (str): The name of the custom chain.

        Returns:
            Enum: An instance of the Chains enum with the custom chain.
        """
        custom_params = {
            "chain_id": chain_id,
            "rpc_url": rpc_url,
            "explorer_url": explorer_url,
            "name": name
        }
        custom_chain = cls(custom_params)
        return custom_chain
