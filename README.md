# NFTPy
[![PyPi](https://img.shields.io/badge/PyPi-1.0.2-green?labelColor=026ab5&style=flat-square&logo=pypi&logoColor=ffffff&link=https://pypi.org/project/NFTPy/)](https://pypi.org/project/NFTPy/)
[![Python](https://img.shields.io/badge/Python-3.7,%203.8,%203.9,%203.10,%203.11,%203.12-green?labelColor=026ab5&style=flat-square&logo=pypi&logoColor=ffffff&link=https://pypi.org/project/NFTPy/)](https://pypi.org/project/NFTPy/)

A Python package designed to facilitate the integration and adoption of NFT (ERC721, ERC1155) tokens in software applications.

## Features

#### EVM Interaction with NFT Tokens
![Ethereum](https://img.shields.io/badge/Ethereum%20Based%20Networks-3C3C3D?style=for-the-badge&logo=Ethereum&logoColor=white)

NFTPy enables interaction with the Ethereum Virtual Machine (EVM) through RPC to retrieve contract details and token holders. It provides a direct communication pathway between the client and the blockchain. Currently, transactional methods are not supported but will be implemented in future updates. The following methods are available:

- **get_balance**: Retrieve the balance of NFTs for a given address.
- **get_token_uri**: Fetch the metadata URI of a specific token.
- **get_owner**: Determine the owner of a specific token.
- **get_approved**: Get the approved address for a specific ERC721 token.
- **is_approved_for_all**: Check if an address is approved for all tokens owned by another address (ERC721).
- **get_token_metadata**: Get the metadata for a specific ERC721 token.
- **get_token_balance**: Get the balance of a specific ERC1155 token for a specific wallet address.
- **get_tokens_balance**: Gets the balance of a specific list of tokens.
- **is_approved_for_all_erc1155**: Check if an address is approved for all tokens owned by another address (ERC1155).

#### Built-in OpenSea Interface
![OpenSea Support](https://img.shields.io/badge/OpenSea-%232081E2.svg?style=for-the-badge&logo=opensea&logoColor=white)

NFTPy includes a built-in interface for interacting with OpenSea via an API key. This allows for in-package queries to OpenSea, enabling access to pricing information and other OpenSea-specific data. The OpenSea interface can be configured to focus on a single collection or query multiple collections. The available methods include:

- **get_collection_stats**: Obtain statistics for a collection.
- **list_events_by_nft**: List events related to a specific NFT.
- **get_collection**: Fetch details of a specific collection.
- **get_contract**: Retrieve details of a specific contract.
- **get_nft**: Get details of a specific NFT.
- **list_nfts_by_account**: List NFTs owned by a specific account.
- **list_nfts_by_collection**: List NFTs in a specific collection.
- **list_nfts_by_contract**: List NFTs under a specific contract.
- **get_payment_token**: Get details of a specific payment token.
- **get_traits**: Get traits of a specific collection.
- **get_all_listings_on_collection**: Get all listings of a specific collection.


# Example Usage
### Interacting on-chain with a collection | NFTPy.EVM.NFT
Using NFTPy.EVM.NFT we are going to be querying the Pixelmon NFT collection on Ethereum mainnet!
We will first start off by creating our class. We are going to define our class with three arguments:
- contract_address: The address of the contract you are trying to query.
- abi: The ABI of the contract you are trying to query. The EVM.ABI class provides presets for our ABI. You can also paste an ABI into the field.
- network: This dictates what RPC URL to use and sets a preset that works best with the network.
- rpc_url: If you do not want to use a preset and instead want to use a custom RPC, define it using this field.

```python
import NFTPy.EVM as EVM
Pixelmon = EVM.NFT("0x32973908FaeE0Bf825A343000fE412ebE56F802A", abi=EVM.ABI.ERC721, network=EVM.Chains.ETH)
#                   Contract Address                                ABI              Network To Query (Ethereum)
```
Now that we have created our NFT object, we can query it. We will start with getting the metadata of a token. I am just putting a random token as the argument.
```python
print(Pixelmon.get_token_metadata(5580))
```
After running this we should see an output resembling this
```json
{
  "name": "Pixelmon #5580",
  "image_url": "https://pixelmon-training-rewards.s3-accelerate.amazonaws.com/0/Moler.jpg",
  "external_url": "https://pixelmon.club/",
  "reward_bitmask": 6,
  "attributes": [
    {"trait_type": "Species", "value": "Moler"},
    {"trait_type": "Origin", "value": "Earth"},
    {"trait_type": "Rarity", "value": "Uncommon"},
    {"trait_type": "Evolution", "value": "Evolution 1"},
    {"trait_type": "Hatched On", "display_type": "date", "value": 1672272943}
  ],
  "animation_url": "https://pixelmon-training-rewards.s3-accelerate.amazonaws.com/6/Moler.mp4"
}

```

We can do a lot more with this. For example:
- Fetching the token URI
- Getting the owner of the token
- Getting the total balance of tokens for an address
- Getting the approved address and so much more.
```python
print(Pixelmon.get_token_uri(5580))
print(Pixelmon.get_owner(5580))
print(Pixelmon.get_balance("0x5AF7875766D1a50d144DF63E581c0764f6573487"))
print(Pixelmon.get_approved(5580))
```

For ERC1155 tokens, you can query balances for multiple token IDs and check approvals:
```python
erc1155_nft = EVM.NFT(contract_address='0xYourERC1155ContractAddress', network=EVM.Chains.ETH, abi=EVM.ABI.ERC1155)
wallet_address = '0xYourWalletAddress'
token_id = 1
token_ids = [1, 2, 3, 4, 5]

# Get the balance of a specific token owned by the wallet
token_balance = erc1155_nft.get_token_balance(wallet_address, token_id)
print(f'Token ID {token_id} Balance: {token_balance}')

# Get the balance of multiple tokens owned by the wallet
tokens_balance = erc1155_nft.get_tokens(wallet_address, token_ids)
print(f'Tokens Balance: {tokens_balance}')

# Check if an address is approved for all tokens (ERC1155)
is_approved_erc1155 = erc1155_nft.is_approved_for_all_erc1155(wallet_address, '0xOperatorAddress')
print(f'Is Approved For All (ERC1155): {is_approved_erc1155}')
```
### Interacting with OpenSea API | NFTPy.OpenSea
We will first start by creating our class with the following arguments:
- api_key: Your OpenSea API key.
- chain: The blockchain network (e.g., Ethereum, Polygon).
- collection_slug: The slug of the collection you want to query (the last part of the url when browsing the collection on opensea) This assigns the interface to a specific collection. If you are using the interface to view multiple collections then you should leave this blank

**Please Note**: When defining the chain, it should be done with NFTPy.OpenSea.Chain as the api requires a special format for chain definition
```python
from NFTPy import OpenSea, OpenSeaChain
opensea = OpenSea(api_key='your-opensea-api-key', chain=OpenSeaChain.POLYGON, collection_slug='your-collection-slug')
```
If we want to query the stats of the NFT collection we can run the following command. If you did not define a collection slug when initializing the interface you will need to define it inside this function
```python
opensea.get_collection_stats()
```
After running that, we should see an output resembling this:
```json
{
  "stats": {
    "one_day_volume": 12.34,
    "one_day_change": 0.56,
    "one_day_sales": 78,
    "one_day_average_price": 0.16,
    "total_volume": 1234.56,
    "total_sales": 7890,
    "total_supply": 10000,
    "count": 10000,
    "num_owners": 2345,
    "average_price": 0.123,
    "num_reports": 0,
    "market_cap": 4567.89,
    "floor_price": 0.123
  }
}
```
We can do a lot more with this. For example:
- Fetching details of a collection
- Getting details of a specific NFT
- Listing events related to a specific NFT
- Listing NFTs owned by an account

```python
print(opensea.get_collection('your-collection-slug'))  # Fetch details of a collection
print(opensea.get_nft('0xYourContractAddress', '1'))  # Get details of a specific NFT
print(opensea.list_events_by_nft('0xYourContractAddress', '1'))  # List events related to a specific NFT
print(opensea.list_nfts_by_account('0xYourWalletAddress'))  # List NFTs owned by an account
```

# Coming Soon
## Chain Integration
- ![Solana](https://img.shields.io/badge/Solana-00FF94?style=for-the-badge&logo=Solana&logoColor=white)
- ![Tron](https://img.shields.io/badge/Tron-FF0600?style=for-the-badge&logo=Tron&logoColor=white)
- ![Tezos](https://img.shields.io/badge/Tezos-2C7DF7?style=for-the-badge&logo=Tezos&logoColor=white)