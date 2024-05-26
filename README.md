# NFTPy

A Python package designed to facilitate the integration and adoption of NFT (ERC721, ERC1155) tokens in software applications.

## Features

#### EVM Interaction with NFT Tokens
NFTPy enables interaction with the Ethereum Virtual Machine (EVM) through RPC to retrieve contract details and token holders. It provides a direct communication pathway between the client and the blockchain. Currently, transactional methods are not supported but will be implemented in future updates. The following methods are available:

- **get_balance**: Retrieve the balance of NFTs for a given address.
- **get_token_uri**: Fetch the metadata URI of a specific token.
- **get_owner**: Determine the owner of a specific token.
- **get_tokens**: List the token IDs and amounts owned by an address.

#### Built-in OpenSea Interface
NFTPy includes a built-in interface for interacting with OpenSea via an API key. This allows for in-package queries to OpenSea, enabling access to pricing information and other OpenSea-specific data. The OpenSea interface can be configured to focus on a single collection or query multiple collections. The available methods include:

- **get_collection**: Fetch details of a specific collection.
- **get_contract**: Retrieve details of a specific contract.
- **get_nft**: Get details of a specific NFT.
- **get_collection_stats**: Obtain statistics for a collection.
- **list_events_by_nft**: List events related to a specific NFT.
- **list_nfts_by_account**: List NFTs owned by a specific account.
- **list_nfts_by_collection**: List NFTs in a specific collection.
- **list_nfts_by_contract**: List NFTs under a specific contract.

### Coming Features
- Full Solana Integration
- Full Tron Integration
- Full Tezos Integration
- Interfaces for OpenSea Alternatives APIs
