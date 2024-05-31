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
        "rpc_url": "https://rpc.holesky.eth",
        "explorer_url": "https://holesky.etherscan.io"
    }

    ETH_GOERLI = {
        "chain_id": 5,
        "name": "Goerli Testnet",
        "rpc_url": "https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID",
        "explorer_url": "https://goerli.etherscan.io"
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
        "rpc_url": "https://rpc-mumbai.maticvigil.com/",
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

    ARBITRUM_GOERLI = {
        "chain_id": 421613,
        "name": "Arbitrum Goerli",
        "rpc_url": "https://goerli-rollup.arbitrum.io/rpc",
        "explorer_url": "https://goerli.arbiscan.io"
    }

    ARBITRUM_RINKEBY = {
        "chain_id": 421611,
        "name": "Arbitrum Rinkeby",
        "rpc_url": "https://rinkeby.arbitrum.io/rpc",
        "explorer_url": "https://rinkeby-explorer.arbitrum.io"
    }

    # OPTIMISM TESTNETS

    OPTIMISM_GOERLI = {
        "chain_id": 420,
        "name": "Optimism Goerli",
        "rpc_url": "https://goerli.optimism.io",
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