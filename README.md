# nftpy
[![PyPi](https://img.shields.io/badge/PyPi-1.2.1-green?labelColor=026ab5&style=flat-square&logo=pypi&logoColor=ffffff&link=https://pypi.org/project/nftpy/)](https://pypi.org/project/nftpy/)
[![Python](https://img.shields.io/badge/Python-3.7,%203.8,%203.9,%203.10,%203.11,%203.12-green?labelColor=026ab5&style=flat-square&logo=pypi&logoColor=ffffff&link=https://pypi.org/project/nftpy/)](https://pypi.org/project/nftpy/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/nftpy?label=PyPI%20Downloads)
![License](https://img.shields.io/github/license/CoulterStutz/nftpy?label=License&color=brightgreen)

A Python package designed to facilitate the integration and adoption of NFT (ERC721, ERC1155) tokens in software applications.

### Changes in 1.2
#### NFT Exchanges added
- Rarible | 1.2.0
  - Support for Eth
  - Support for Polygon interactions
- Mintable | 1.2.1
  - Support for Eth
  - Support for Polygon interactions
- Foundation | 1.2.2
  - Support for Eth
  - Support for Polygon interactions
- LooksRare | 1.2.3
  - Support for Eth interactions
- X2Y2 | 1.2.4
  - Support for Eth interactions
- SuperRare | 1.2.5
  - Support for Eth interactions
- Treasureland | 1.2.7
  - Support for Eth
  - Support for BSC interactions
- Decentraland | 1.2.8
  - Support for Eth interactions
- Zapper | 1.2.9
  - Support for Eth
  - Support for Polygon interactions


## Features

#### EVM Interaction with NFT Tokens
![Ethereum](https://img.shields.io/badge/Ethereum%20Based%20Networks-3C3C3D?style=for-the-badge&logo=Ethereum&logoColor=white)

nftpy enables interaction with the Ethereum Virtual Machine (EVM) through RPC to retrieve contract details and token holders. It provides a direct communication pathway between the client and the blockchain. Currently, transactional methods are not supported but will be implemented in future updates. The following methods are available:

- **get_balance**: Retrieve the balance of NFTs for a given address.
- **get_token_uri**: Fetch the metadata URI of a specific token.
- **get_owner**: Determine the owner of a specific token.
- **get_approved**: Get the approved address for a specific ERC721 token.
- **is_approved_for_all**: Check if an address is approved for all tokens owned by another address (ERC721).
- **get_token_metadata**: Get the metadata for a specific ERC721 token.
- **get_token_balance**: Get the balance of a specific ERC1155 token for a specific wallet address.
- **get_tokens_balance**: Gets the balance of a specific list of tokens.
- **is_approved_for_all_erc1155**: Check if an address is approved for all tokens owned by another address (ERC1155).

#### EVM Wallet Interaction
nftpy includes comprehensive features for interacting with Ethereum wallets, including querying balances, fetching gas prices, and transferring NFTs. The wallet interface supports both read-only and transactional operations.

**Wallet Features:**
- **get_balance**: Retrieve the balance of NFTs for a given address in Ether.
- **get_balance_wei**: Retrieve the balance of NFTs for a given address in Wei.
- **get_gas_price_wei**: Fetch the current gas price in Wei.
- **get_gas_price_gwei**: Fetch the current gas price in Gwei.
- **transfer_nft**: Transfer an NFT from the wallet to another address.
- **wait_until_transaction_processes**: Delays the program until the transaction has fully processed in the blockchain
- **get_transaction_count**: Get the number of transactions sent from the wallet.
- **estimate_gas**: Estimate the gas required for a transaction.
- **is_synced**: Check if the blockchain is synced.
- **get_latest_block**: Get the latest block on the blockchain.

#### Built-in OpenSea Interface
![OpenSea Support](https://img.shields.io/badge/OpenSea-%232081E2.svg?style=for-the-badge&logo=opensea&logoColor=white)

nftpy includes a built-in interface for interacting with OpenSea via an API key. This allows for in-package queries to OpenSea, enabling access to pricing information and other OpenSea-specific data. The OpenSea interface can be configured to focus on a single collection or query multiple collections. The available methods include:

**OpenSea Class:**
- *get_collection_stats*: Obtain statistics for a collection.
- *get_collection*: Fetch details of a specific collection.
- *get_nft*: Get details of a specific NFT.
- *list_events_by_nft*: List events related to a specific NFT.
- *list_nfts_by_account*: List NFTs owned by a specific account.

**OpenSeaCollection Class:**
- *get_collection_details*: Fetch details of a specific collection.
- *get_nfts*: List NFTs in a specific collection.

**OpenSeaWallet Class:**
- *get_balance*: Check the balance of the wallet.
- *get_nfts*: Retrieve all NFTs owned by the wallet.

#### Built-in Rarible Interface
![Rarible Support](https://img.shields.io/badge/Rarible-000000?style=for-the-badge&logo=Rarible&logoColor=white)

nftpy includes a comprehensive interface for interacting with Rarible via an API key. This allows for in-package queries to Rarible, enabling access to NFT information, market data, and more. The available methods include:

**Rarible Class:**
- *get_item_by_id*: Fetch details of a specific item by its ID.
- *get_items_by_ids*: Fetch details of multiple items by their IDs.
- *get_item_royalties_by_id*: Retrieve royalty information for a specific item by its ID.
- *get_items_by_owner*: Fetch items owned by a specific address.
- *validate_signature*: Validate a signature for a given data set.
- *get_signature_input*: Get input data required for generating a signature.
- *encode_data*: Encode data for the Rarible protocol.
- *get_usd_rate*: Get the USD exchange rate for a specific currency.
- *get_all_currencies*: Fetch all supported currencies.
- *get_user_balance*: Retrieve the balance of a specific user in a specified currency.


#### Custom Chain Support
nftpy allows the creation of custom chains with specific chain IDs, RPC URLs, explorer URLs, and names. This feature enhances flexibility by enabling the addition of blockchain networks that are not predefined in the library.

**Creating a Custom Chain:**
```python
from nftpy.EVM import Chain

custom_chain = Chain(
        name = "Ethereum",
        symbol = "ETH",
        chain_id = 1,
        rpc_url = "https://eth.llamarpc.com",
        explorer_url = "https://etherscan.io",
        testnet = False
)
```

# Example Usage
### Interacting on-chain with a collection | nftpy.EVM.NFT
Using nftpy.EVM.NFT we are going to be querying the Pixelmon NFT collection on Ethereum mainnet!
We will first start off by creating our class. We are going to define our class with three arguments:
- contract_address: The address of the contract you are trying to query.
- abi: The ABI of the contract you are trying to query. The EVM.ABI class provides presets for our ABI. You can also paste an ABI into the field.
- network: This dictates what RPC URL to use and sets a preset that works best with the network.
- rpc_url: If you do not want to use a preset and instead want to use a custom RPC, define it using this field.

```python
import nftpy.EVM as EVM
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

### Interacting with a Wallet | nftpy.NFTWallet

Creating an instance of `NFTWallet` requires either a private key for full access or just an address for read-only access. You can also specify multiple chains to connect to different networks simultaneously.

```python
from nftpy import *

# Initialize the wallet with a private key and specify chains
wallet = NFTWallet(private_key="0x9015a0eb4c1ceab5f5544ac6e0a75eabb37d7dec26f1dfcb09adb43632330736", chains=[Chains.ETH_SEPOLIA])

# Get the balance of the wallet in Ether
print(wallet.get_balance()) 
# Output: {"Balances": {'Sepolia Testnet': Decimal('0.8341469847291797')}}

# Get the balance of the wallet in Wei
print(wallet.get_balance_wei()) 
# Output: {"Balances": {'Sepolia Testnet': 834146984729179700}}

# Get the current gas price in Wei
print(wallet.get_gas_price_wei()) 
# Output: {'Sepolia Testnet': 20000000000}

# Get the current gas price in Gwei
print(wallet.get_gas_price_gwei()) 
# Output: {'Sepolia Testnet': Decimal('20')}

# Transfer an NFT to another wallet
to_wallet = "0xa693190103733280E23055BE70C838d9b6708b9a"
contract = "0x725Ea5eEA79F1515e34A921b83D4307b325cC8b9"
gas_price = wallet.get_gas_price_gwei()["Sepolia Testnet"]
gas_limit = 65000   # Disclaimer! Gas Limit set for Sepolia, WILL fail on other networks

# Transfer the NFT and get the transaction hash and explorer URL
print(wallet.transfer_nft(to=to_wallet, contract_address=contract, amount=1, gas_limit=gas_limit,
                          gas_price_gwei=gas_price, abi=ABI.OPENSEA_ERC1155, token_id=1))
# Output: {'transaction_hash': '0x18a076a4a30c1cc014b1620aa907db06a04e8a709bda47e9beed2233a23f532f', 'explorer_url': 'https://sepolia.etherscan.io/tx/0x18a076a4a30c1cc014b1620aa907db06a04e8a709bda47e9beed2233a23f532f'}
```
#### Waiting For The Transaction To Process
After we get the transaction hash, we can have the program delay until the transaction processes on the blockchain.
```python
# Wait until the transaction is processed
transaction_hash = "0xcd74c93bbf42cae24f329c45da995bde7e1c89ea848855d04db516c6460eda02"
print(wallet.wait_until_transaction_processes(transaction_hash, chain=Chains.ETH_SEPOLIA))
# Output: True | When the transaction fully processes on the blockchain
```

#### Read-Only Wallets
When using a read-only address (i.e., only providing an address and not a private key), you can still interact with the blockchain to query information, but you will not be able to perform transactions. This is useful for monitoring wallets and retrieving data without the need for sensitive credentials.
```python
from nftpy import *

# Initialize the wallet with an address and specify chains
readonly_wallet = NFTWallet(address="0xYourReadOnlyWalletAddress", chains=[Chains.ETH_SEPOLIA])

# Get the balance of the wallet in Ether
print(readonly_wallet.get_balance()) 
# Output: {"Balances": {'Sepolia Testnet': Decimal('0.123456789012345678')}}

# Get the balance of the wallet in Wei
print(readonly_wallet.get_balance_wei()) 
# Output: {"Balances": {'Sepolia Testnet': 123456789012345678}}

# Get the current gas price in Wei
print(readonly_wallet.get_gas_price_wei()) 
# Output: {'Sepolia Testnet': 20000000000}
```

### Interacting with OpenSea API | nftpy.OpenSea

We will first start by creating our class with the following arguments:
- *api_key*: Your OpenSea API key.
- *chain*: The blockchain network (e.g., Ethereum, Polygon).

**Please Note**: When defining the chain, it should be done with ```nftpy.OpenSea.OpenSeaChain``` as the API requires a special format for chain definition.

```python
from nftpy import OpenSea, OpenSeaChain
opensea = OpenSea(api_key='your-opensea-api-key', chain=OpenSeaChain.POLYGON)
```

#### Fetching Collection Statistics

To query the stats of an NFT collection, use the following method:

```python
opensea.get_collection_stats('your-collection-slug')
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

#### Fetching Collection Details

To fetch details of a collection, use the following method:

```python
opensea.get_collection('your-collection-slug')
```

#### Fetching NFT Details

To get details of a specific NFT, use the following method:
```python
opensea.get_nft('0xYourContractAddress', '1')
```
#### Listing Events by NFT

To list events related to a specific NFT, use the following method:

```python
opensea.list_events_by_nft('0xYourContractAddress', '1')
```

#### Listing NFTs by Account

To list NFTs owned by a specific account, use the following method:

```python
opensea.list_nfts_by_account('0xYourWalletAddress')
```

#### Managing Collections

To manage a collection, create an instance of the *OpenSeaCollection* class:

```python
from nftpy import OpenSeaCollection

collection = OpenSeaCollection(collection_name='your-collection-name', api_key='your-api-key')
```

#### Getting Collection Details

To get details of a specific collection, use the following method:
```python
details = collection.get_collection_details()
```
#### Listing NFTs in a Collection

To list all NFTs within a collection, use the following method:
```python
nfts = collection.get_nfts()
```
### Managing Wallets

To manage a wallet, create an instance of the *OpenSeaWallet* class:

```python
from nftpy import OpenSeaWallet
wallet = OpenSeaWallet(address='your-wallet-address', api_key='your-api-key')
```
#### Checking Wallet Balance

To check the balance of the wallet, use the following method:

```python
balance = wallet.get_balance()
```
#### Fetching Wallet NFTs

To retrieve all NFTs owned by the wallet, use the following method:
```python
nfts = wallet.get_nfts()
```
### Interacting with Rarible API | nftpy.Rarible

We will first start by creating our class with the following arguments:
- *api_key*: Your Rarible API key.
- *chain*: The blockchain network (e.g., Ethereum, Polygon).

**Please Note**: When defining the chain, it should be done with *nftpy.Rarible.RaribleChain* as the API requires a special format for chain definition.
```python
from nftpy import Rarible, RaribleChain
rarible = Rarible(api_key='your-rarible-api-key', chain=RaribleChain.ETHEREUM)
```
#### Fetching Item by ID

To fetch details of a specific item by its ID, use the following method:
```python
rarible.get_item_by_id('item_id')
```
#### Fetching Items by IDs

To fetch details of multiple items by their IDs, use the following method:
```python
rarible.get_items_by_ids(['item_id1', 'item_id2'])
```
#### Fetching Item Royalties by ID

To retrieve royalty information for a specific item by its ID, use the following method:
```python
rarible.get_item_royalties_by_id('item_id')
```
#### Fetching Items by Owner

To fetch items owned by a specific address, use the following method:

```python
rarible.get_items_by_owner('owner_address')
```
#### Validating Signature

To validate a signature for a given data set, use the following method:

```python
rarible.validate_signature(data={'your': 'data'})
```

#### Getting Signature Input

To get input data required for generating a signature, use the following method:

```python
rarible.get_signature_input(data={'your': 'data'})
```

#### Encoding Data

To encode data for the Rarible protocol, use the following method:

```python
rarible.encode_data(data={'your': 'data'})
```

#### Getting USD Exchange Rate

To get the USD exchange rate for a specific currency, use the following method:

```python
rarible.get_usd_rate('currency')
```
#### Fetching All Currencies

To fetch all supported currencies, use the following method:
```python
rarible.get_all_currencies()
```
#### Fetching User Balance

To retrieve the balance of a specific user in a specified currency, use the following method:
```python
rarible.get_user_balance('user_address', 'currency')
```
# Coming Soon

## Marketplace Integration
![Mintable](https://img.shields.io/badge/Mintable-00BFFF?style=for-the-badge&logo=Mintable&logoColor=white)
![Foundation](https://img.shields.io/badge/Foundation-000000?style=for-the-badge&logo=Foundation&logoColor=white)
![LooksRare](https://img.shields.io/badge/LooksRare-000000?style=for-the-badge&logo=LooksRare&logoColor=white)
![X2Y2](https://img.shields.io/badge/X2Y2-000000?style=for-the-badge&logo=X2Y2&logoColor=white)
![SuperRare](https://img.shields.io/badge/SuperRare-000000?style=for-the-badge&logo=SuperRare&logoColor=white)
![Treasureland](https://img.shields.io/badge/Treasureland-FF9800?style=for-the-badge&logo=Treasureland&logoColor=white)
![Decentraland](https://img.shields.io/badge/Decentraland-F15A24?style=for-the-badge&logo=Decentraland&logoColor=white)
![Zapper](https://img.shields.io/badge/Zapper-6741FF?style=for-the-badge&logo=Zapper&logoColor=white)
![BakerySwap](https://img.shields.io/badge/BakerySwap-FDBE34?style=for-the-badge&logo=BakerySwap&logoColor=white)
![AirNFTs](https://img.shields.io/badge/AirNFTs-00A3FF?style=for-the-badge&logo=AirNFTs&logoColor=white)
![PancakeSwap](https://img.shields.io/badge/PancakeSwap-7FCBE6?style=for-the-badge&logo=PancakeSwap&logoColor=white)
![Binance NFT](https://img.shields.io/badge/Binance%20NFT-F0B90B?style=for-the-badge&logo=Binance&logoColor=white)
![NFTb](https://img.shields.io/badge/NFTb-0000FF?style=for-the-badge&logo=NFTb&logoColor=white)
![DODO](https://img.shields.io/badge/DODO-FFFF00?style=for-the-badge&logo=DODO&logoColor=black)


## Chain Integration | Coming in 2.0
![Solana](https://img.shields.io/badge/Solana-00FF94?style=for-the-badge&logo=Solana&logoColor=white)
![Tron](https://img.shields.io/badge/Tron-FF0600?style=for-the-badge&logo=Tron&logoColor=white)
![Tezos](https://img.shields.io/badge/Tezos-2C7DF7?style=for-the-badge&logo=Tezos&logoColor=white)