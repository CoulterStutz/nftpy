from enum import Enum

class ABI(Enum):
    ERC721 = [
        {
            "constant": True,
            "inputs": [{"name": "_owner", "type": "address"}],
            "name": "balanceOf",
            "outputs": [{"name": "balance", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": True,
            "inputs": [{"name": "_tokenId", "type": "uint256"}],
            "name": "ownerOf",
            "outputs": [{"name": "owner", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": False,
            "inputs": [
                {"name": "_from", "type": "address"},
                {"name": "_to", "type": "address"},
                {"name": "_tokenId", "type": "uint256"}
            ],
            "name": "transferFrom",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "constant": False,
            "inputs": [
                {"name": "_from", "type": "address"},
                {"name": "_to", "type": "address"},
                {"name": "_tokenId", "type": "uint256"}
            ],
            "name": "safeTransferFrom",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "constant": False,
            "inputs": [
                {"name": "_from", "type": "address"},
                {"name": "_to", "type": "address"},
                {"name": "_tokenId", "type": "uint256"},
                {"name": "_data", "type": "bytes"}
            ],
            "name": "safeTransferFrom",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "constant": False,
            "inputs": [
                {"name": "_approved", "type": "address"},
                {"name": "_tokenId", "type": "uint256"}
            ],
            "name": "approve",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "constant": False,
            "inputs": [
                {"name": "_operator", "type": "address"},
                {"name": "_approved", "type": "bool"}
            ],
            "name": "setApprovalForAll",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "constant": True,
            "inputs": [{"name": "_tokenId", "type": "uint256"}],
            "name": "getApproved",
            "outputs": [{"name": "operator", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": True,
            "inputs": [
                {"name": "_owner", "type": "address"},
                {"name": "_operator", "type": "address"}
            ],
            "name": "isApprovedForAll",
            "outputs": [{"name": "approved", "type": "bool"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": True,
            "inputs": [{"name": "_tokenId", "type": "uint256"}],
            "name": "tokenURI",
            "outputs": [{"name": "uri", "type": "string"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "anonymous": False,
            "inputs": [
                {"indexed": True, "name": "from", "type": "address"},
                {"indexed": True, "name": "to", "type": "address"},
                {"indexed": True, "name": "tokenId", "type": "uint256"}
            ],
            "name": "Transfer",
            "type": "event"
        },
        {
            "anonymous": False,
            "inputs": [
                {"indexed": True, "name": "owner", "type": "address"},
                {"indexed": True, "name": "approved", "type": "address"},
                {"indexed": True, "name": "tokenId", "type": "uint256"}
            ],
            "name": "Approval",
            "type": "event"
        },
        {
            "anonymous": False,
            "inputs": [
                {"indexed": True, "name": "owner", "type": "address"},
                {"indexed": True, "name": "operator", "type": "address"},
                {"indexed": False, "name": "approved", "type": "bool"}
            ],
            "name": "ApprovalForAll",
            "type": "event"
        }
    ]

    ERC1155 = [
        {
            "constant": True,
            "inputs": [
                {"name": "_owner", "type": "address"},
                {"name": "_id", "type": "uint256"}
            ],
            "name": "balanceOf",
            "outputs": [{"name": "balance", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": True,
            "inputs": [
                {"name": "_owners", "type": "address[]"},
                {"name": "_ids", "type": "uint256[]"}
            ],
            "name": "balanceOfBatch",
            "outputs": [{"name": "balances", "type": "uint256[]"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": False,
            "inputs": [
                {"name": "_from", "type": "address"},
                {"name": "_to", "type": "address"},
                {"name": "_id", "type": "uint256"},
                {"name": "_value", "type": "uint256"},
                {"name": "_data", "type": "bytes"}
            ],
            "name": "safeTransferFrom",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "constant": False,
            "inputs": [
                {"name": "_from", "type": "address"},
                {"name": "_to", "type": "address"},
                {"name": "_ids", "type": "uint256[]"},
                {"name": "_values", "type": "uint256[]"},
                {"name": "_data", "type": "bytes"}
            ],
            "name": "safeBatchTransferFrom",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "constant": False,
            "inputs": [
                {"name": "_operator", "type": "address"},
                {"name": "_approved", "type": "bool"}
            ],
            "name": "setApprovalForAll",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "constant": True,
            "inputs": [
                {"name": "_owner", "type": "address"},
                {"name": "_operator", "type": "address"}
            ],
            "name": "isApprovedForAll",
            "outputs": [{"name": "approved", "type": "bool"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "anonymous": False,
            "inputs": [
                {"indexed": True, "name": "operator", "type": "address"},
                {"indexed": True, "name": "from", "type": "address"},
                {"indexed": True, "name": "to", "type": "address"},
                {"indexed": True, "name": "id", "type": "uint256"},
                {"indexed": False, "name": "value", "type": "uint256"}
            ],
            "name": "TransferSingle",
            "type": "event"
        },
        {
            "anonymous": False,
            "inputs": [
                {"indexed": True, "name": "operator", "type": "address"},
                {"indexed": True, "name": "from", "type": "address"},
                {"indexed": True, "name": "to", "type": "address"},
                {"indexed": True, "name": "ids", "type": "uint256[]"},
                {"indexed": False, "name": "values", "type": "uint256[]"}
            ],
            "name": "TransferBatch",
            "type": "event"
        },
        {
            "anonymous": False,
            "inputs": [
                {"indexed": True, "name": "account", "type": "address"},
                {"indexed": True, "name": "operator", "type": "address"},
                {"indexed": False, "name": "approved", "type": "bool"}
            ],
            "name": "ApprovalForAll",
            "type": "event"
        },
        {
            "anonymous": False,
            "inputs": [
                {"indexed": False, "name": "value", "type": "uint256"},
                {"indexed": True, "name": "id", "type": "uint256"}
            ],
            "name": "URI",
            "type": "event"
        }
    ]
