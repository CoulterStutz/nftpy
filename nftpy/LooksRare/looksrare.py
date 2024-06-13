from enum import Enum
from ..errors import APIKeyNotSpecifiedOnMainnetError, RateLimitExceededError, InvalidLooksRareAPIRequest, \
    APIKeyRequiredForPostError
from termcolor import colored
import requests

class LooksRareChain(Enum):
    MAINNET = "https://api.looksrare.org/api/"
    SEPOLIA = "https://api-sepolia.looksrare.org/api/"


class LooksRareAPI:
    def __init__(self, chain: LooksRareChain, api_key: str = None, suppress_warnings: bool = False, version: int = 2):
        self._chain = chain
        self._api_key = api_key
        self._version = version
        if self._chain == LooksRareChain.MAINNET and self._version == 2:
            if self._api_key is None:
                raise APIKeyNotSpecifiedOnMainnetError()
        elif self._chain == LooksRareChain.SEPOLIA:
            if self._api_key is not None and suppress_warnings is False:
                print(colored("[NFTPY]: Warning! API key isn't needed for the Sepolia Network!", 'yellow'))

    def get_account_by_address(self, address: str):
        url = f"{self._chain.value}v1/account/{address}"
        headers = {"Accept": "application/json"}

        response = requests.get(url, headers=headers)

        if response.status_code == 429:
            raise RateLimitExceededError()
        if response.status_code == 400:
            raise InvalidLooksRareAPIRequest()

        if not response.ok:
            response.raise_for_status()

        return response.json()

    def get_collection_by_address(self, address: str):
        url = f"{self._chain.value}v1/collections/{address}"
        headers = {"Accept": "application/json"}

        response = requests.get(url, headers=headers)

        if response.status_code == 429:
            raise RateLimitExceededError()
        if response.status_code == 400:
            raise InvalidLooksRareAPIRequest()

        if not response.ok:
            response.raise_for_status()

        return response.json()

    def get_collection_stats(self, address: str):
        url = f"{self._chain.value}v1/collections/stats?collection={address}"
        headers = {"Accept": "application/json"}

        response = requests.get(url, headers=headers)

        if response.status_code == 429:
            raise RateLimitExceededError()
        if response.status_code == 400:
            raise InvalidLooksRareAPIRequest()

        if not response.ok:
            response.raise_for_status()

        return response.json()

    def get_lre_eligible_collections(self):
        url = f"{self._chain.value}v1/collections/lre-eligible"
        headers = {"Accept": "application/json"}

        response = requests.get(url, headers=headers)

        if response.status_code == 429:
            raise RateLimitExceededError()
        if response.status_code == 400:
            raise InvalidLooksRareAPIRequest()

        if not response.ok:
            response.raise_for_status()

        return response.json()

    def get_collection_token(self, collection_address: str, token_id: str):
        url = f"{self._chain.value}v1/collections/{collection_address}/tokens/{token_id}"
        headers = {"Accept": "application/json"}

        response = requests.get(url, headers=headers)

        if response.status_code == 429:
            raise RateLimitExceededError()
        if response.status_code == 400:
            raise InvalidLooksRareAPIRequest()

        if not response.ok:
            response.raise_for_status()

        return response.json()

    def refresh_token_metadata(self, collection_address: str, token_id: str):
        if self._version == 1 and self._api_key is None:
            raise APIKeyRequiredForPostError()

        url = f"{self._chain.value}v1/tokens/refresh/{collection_address}/{token_id}"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-API-KEY": self._api_key
        }

        response = requests.post(url, headers=headers)

        if response.status_code == 429:
            raise RateLimitExceededError()
        if response.status_code == 400:
            raise InvalidLooksRareAPIRequest()

        if not response.ok:
            response.raise_for_status()

        return response.json()

    class _Account:
        def __init__(self, address, balance, nonce, is_operator, allowances, trading_data=None, profile=None, name=None, biography=None, website_link=None, instagram_link=None, twitter_link=None, is_verified=False):
            self.address = address
            self.balance = balance
            self.nonce = nonce
            self.is_operator = is_operator
            self.allowances = allowances
            self.trading_data = trading_data
            self.profile = profile
            self.name = name
            self.biography = biography
            self.website_link = website_link
            self.instagram_link = instagram_link
            self.twitter_link = twitter_link
            self.is_verified = is_verified

        @classmethod
        def from_dict(cls, data):
            address = data.get('address')
            balance = data.get('balance')
            nonce = data.get('nonce')
            is_operator = data.get('isOperator')
            allowances = data.get('allowances')
            trading_data = data.get('tradingData')
            profile = data.get('profile')
            name = data.get('name')
            biography = data.get('biography')
            website_link = data.get('websiteLink')
            instagram_link = data.get('instagramLink')
            twitter_link = data.get('twitterLink')
            is_verified = data.get('isVerified', False)
            return cls(address, balance, nonce, is_operator, allowances, trading_data, profile, name, biography, website_link, instagram_link, twitter_link, is_verified)

        def __repr__(self):
            return (f"Account(address={self.address}, balance={self.balance}, nonce={self.nonce}, is_operator={self.is_operator}, "
                    f"allowances={self.allowances}, trading_data={self.trading_data}, profile={self.profile}, name={self.name}, "
                    f"biography={self.biography}, website_link={self.website_link}, instagram_link={self.instagram_link}, "
                    f"twitter_link={self.twitter_link}, is_verified={self.is_verified})")

    class _CollectionInformation:
        def __init__(self, address, owner, setter=None, admin=None, name=None, description=None, symbol=None, collection_type=None,
                    website_link=None, facebook_link=None, twitter_link=None, instagram_link=None, telegram_link=None,
                    medium_link=None, discord_link=None, is_verified=False, is_explicit=False, logo_uri=None, banner_uri=None):
            self.address = address
            self.owner = owner
            self.setter = setter
            self.admin = admin
            self.name = name
            self.description = description
            self.symbol = symbol
            self.collection_type = collection_type
            self.website_link = website_link
            self.facebook_link = facebook_link
            self.twitter_link = twitter_link
            self.instagram_link = instagram_link
            self.telegram_link = telegram_link
            self.medium_link = medium_link
            self.discord_link = discord_link
            self.is_verified = is_verified
            self.is_explicit = is_explicit
            self.logo_uri = logo_uri
            self.banner_uri = banner_uri

        @classmethod
        def from_dict(cls, data):
            address = data.get('address')
            owner = data.get('owner')
            setter = data.get('setter')
            admin = data.get('admin')
            name = data.get('name')
            description = data.get('description')
            symbol = data.get('symbol')
            collection_type = data.get('type')
            website_link = data.get('websiteLink')
            facebook_link = data.get('facebookLink')
            twitter_link = data.get('twitterLink')
            instagram_link = data.get('instagramLink')
            telegram_link = data.get('telegramLink')
            medium_link = data.get('mediumLink')
            discord_link = data.get('discordLink')
            is_verified = data.get('isVerified', False)
            is_explicit = data.get('isExplicit', False)
            logo_uri = data.get('logoURI')
            banner_uri = data.get('bannerURI')
            return cls(address, owner, setter, admin, name, description, symbol, collection_type, website_link, facebook_link,
                       twitter_link, instagram_link, telegram_link, medium_link, discord_link, is_verified, is_explicit, logo_uri, banner_uri)

        def __repr__(self):
            return (f"CollectionInformation(address={self.address}, owner={self.owner}, setter={self.setter}, admin={self.admin}, "
                    f"name={self.name}, description={self.description}, symbol={self.symbol}, collection_type={self.collection_type}, "
                    f"website_link={self.website_link}, facebook_link={self.facebook_link}, twitter_link={self.twitter_link}, "
                    f"instagram_link={self.instagram_link}, telegram_link={self.telegram_link}, medium_link={self.medium_link}, "
                    f"discord_link={self.discord_link}, is_verified={self.is_verified}, is_explicit={self.is_explicit}, "
                    f"logo_uri={self.logo_uri}, banner_uri={self.banner_uri})")

    class _CollectionStats:
        def __init__(self, address, count_owners, total_supply, floor_price, floor_change_24h, floor_change_7d, floor_change_30d, market_cap,
                     volume_24h, average_24h, count_24h, change_24h, volume_7d, average_7d, count_7d, change_7d, volume_1m, average_1m,
                     count_1m, change_1m, volume_3m, average_3m, count_3m, change_3m, volume_6m, average_6m, count_6m, change_6m, volume_1y,
                     average_1y, count_1y, change_1y, volume_all, average_all, count_all):
            self.address = address
            self.count_owners = count_owners
            self.total_supply = total_supply
            self.floor_price = floor_price
            self.floor_change_24h = floor_change_24h
            self.floor_change_7d = floor_change_7d
            self.floor_change_30d = floor_change_30d
            self.market_cap = market_cap
            self.volume_24h = volume_24h
            self.average_24h = average_24h
            self.count_24h = count_24h
            self.change_24h = change_24h
            self.volume_7d = volume_7d
            self.average_7d = average_7d
            self.count_7d = count_7d
            self.change_7d = change_7d
            self.volume_1m = volume_1m
            self.average_1m = average_1m
            self.count_1m = count_1m
            self.change_1m = change_1m
            self.volume_3m = volume_3m
            self.average_3m = average_3m
            self.count_3m = count_3m
            self.change_3m = change_3m
            self.volume_6m = volume_6m
            self.average_6m = average_6m
            self.count_6m = count_6m
            self.change_6m = change_6m
            self.volume_1y = volume_1y
            self.average_1y = average_1y
            self.count_1y = count_1y
            self.change_1y = change_1y
            self.volume_all = volume_all
            self.average_all = average_all
            self.count_all = count_all

        @classmethod
        def from_dict(cls, data):
            address = data.get('address')
            count_owners = data.get('countOwners')
            total_supply = data.get('totalSupply')
            floor_price = data.get('floorPrice')
            floor_change_24h = data.get('floorChange24h')
            floor_change_7d = data.get('floorChange7d')
            floor_change_30d = data.get('floorChange30d')
            market_cap = data.get('marketCap')
            volume_24h = data.get('volume24h')
            average_24h = data.get('average24h')
            count_24h = data.get('count24h')
            change_24h = data.get('change24h')
            volume_7d = data.get('volume7d')
            average_7d = data.get('average7d')
            count_7d = data.get('count7d')
            change_7d = data.get('change7d')
            volume_1m = data.get('volume1m')
            average_1m = data.get('average1m')
            count_1m = data.get('count1m')
            change_1m = data.get('change1m')
            volume_3m = data.get('volume3m')
            average_3m = data.get('average3m')
            count_3m = data.get('count3m')
            change_3m = data.get('change_3m')
            volume_6m = data.get('volume6m')
            average_6m = data.get('average6m')
            count_6m = data.get('count6m')
            change_6m = data.get('change6m')
            volume_1y = data.get('volume1y')
            average_1y = data.get('average1y')
            count_1y = data.get('count1y')
            change_1y = data.get('change1y')
            volume_all = data.get('volumeAll')
            average_all = data.get('averageAll')
            count_all = data.get('countAll')
            return cls(address, count_owners, total_supply, floor_price, floor_change_24h, floor_change_7d, floor_change_30d, market_cap,
                       volume_24h, average_24h, count_24h, change_24h, volume_7d, average_7d, count_7d, change_7d, volume_1m, average_1m,
                       count_1m, change_1m, volume_3m, average_3m, count_3m, change_3m, volume_6m, average_6m, count_6m, change_6m,
                       volume_1y, average_1y, count_1y, change_1y, volume_all, average_all, count_all)

        def __repr__(self):
            return (f"CollectionStats(address={self.address}, count_owners={self.count_owners}, total_supply={self.total_supply}, "
                    f"floor_price={self.floor_price}, floor_change_24h={self.floor_change_24h}, floor_change_7d={self.floor_change_7d}, "
                    f"floor_change_30d={self.floor_change_30d}, market_cap={self.market_cap}, volume_24h={self.volume_24h}, "
                    f"average_24h={self.average_24h}, count_24h={self.count_24h}, change_24h={self.change_24h}, volume_7d={self.volume_7d}, "
                    f"average_7d={self.average_7d}, count_7d={self.count_7d}, change_7d={self.change_7d}, volume_1m={self.volume_1m}, "
                    f"average_1m={self.average_1m}, count_1m={self.count_1m}, change_1m={self.change_1m}, volume_3m={self.volume_3m}, "
                    f"average_3m={self.average_3m}, count_3m={self.count_3m}, change_3m={self.change_3m}, volume_6m={self.volume_6m}, "
                    f"average_6m={self.average_6m}, count_6m={self.count_6m}, change_6m={self.change_6m}, volume_1y={self.volume_1y}, "
                    f"average_1y={self.average_1y}, count_1y={self.count_1y}, change_1y={self.change_1y}, volume_all={self.volume_all}, "
                    f"average_all={self.average_all}, count_all={self.count_all})")

    class _Order:
        def __init__(self, order_id, maker, taker, strategy, currency, amount, price, nonce, start_time, end_time,
                     status, signature, intermediary=None, order_type=None, salt=None, extra_params=None):
            self.order_id = order_id
            self.maker = maker
            self.taker = taker
            self.strategy = strategy
            self.currency = currency
            self.amount = amount
            self.price = price
            self.nonce = nonce
            self.start_time = start_time
            self.end_time = end_time
            self.status = status
            self.signature = signature
            self.intermediary = intermediary
            self.order_type = order_type
            self.salt = salt
            self.extra_params = extra_params

        @classmethod
        def from_dict(cls, data):
            order_id = data.get('orderId')
            maker = data.get('maker')
            taker = data.get('taker')
            strategy = data.get('strategy')
            currency = data.get('currency')
            amount = data.get('amount')
            price = data.get('price')
            nonce = data.get('nonce')
            start_time = data.get('startTime')
            end_time = data.get('endTime')
            status = data.get('status')
            signature = data.get('signature')
            intermediary = data.get('intermediary')
            order_type = data.get('type')
            salt = data.get('salt')
            extra_params = data.get('extraParams')
            return cls(order_id, maker, taker, strategy, currency, amount, price, nonce, start_time, end_time, status,
                       signature, intermediary, order_type, salt, extra_params)

        def __repr__(self):
            return (
                f"Order(order_id={self.order_id}, maker={self.maker}, taker={self.taker}, strategy={self.strategy}, "
                f"currency={self.currency}, amount={self.amount}, price={self.price}, nonce={self.nonce}, "
                f"start_time={self.start_time}, end_time={self.end_time}, status={self.status}, signature={self.signature}, "
                f"intermediary={self.intermediary}, order_type={self.order_type}, salt={self.salt}, extra_params={self.extra_params})")

    class _Token:
        def __init__(self, id, collection_address, token_id, token_uri, image_uri, is_explicit, is_animated, flag, name,
                     description, collection):
            self.id = id
            self.collection_address = collection_address
            self.token_id = token_id
            self.token_uri = token_uri
            self.image_uri = image_uri
            self.is_explicit = is_explicit
            self.is_animated = is_animated
            self.flag = flag
            self.name = name
            self.description = description
            self.collection = collection

        @classmethod
        def from_dict(cls, data):
            id = data.get('id')
            collection_address = data.get('collectionAddress')
            token_id = data.get('tokenId')
            token_uri = data.get('tokenURI')
            image_uri = data.get('imageURI')
            is_explicit = data.get('isExplicit')
            is_animated = data.get('isAnimated')
            flag = data.get('flag')
            name = data.get('name')
            description = data.get('description')
            collection = data.get('collection')
            return cls(id, collection_address, token_id, token_uri, image_uri, is_explicit, is_animated, flag, name,
                       description, collection)

        def __repr__(self):
            return (
                f"Token(id={self.id}, collection_address={self.collection_address}, token_id={self.token_id}, token_uri={self.token_uri}, "
                f"image_uri={self.image_uri}, is_explicit={self.is_explicit}, is_animated={self.is_animated}, flag={self.flag}, "
                f"name={self.name}, description={self.description}, collection={self.collection})")

    class _ListingReward:
        def __init__(self, proof, looks_total, looks_24h, date):
            self.proof = proof
            self.looks_total = looks_total
            self.looks_24h = looks_24h
            self.date = date

        @classmethod
        def from_dict(cls, data):
            proof = data.get('proof')
            looks_total = data.get('looksTotal')
            looks_24h = data.get('looks24h')
            date = data.get('date')
            return cls(proof, looks_total, looks_24h, date)

        def __repr__(self):
            return (
                f"ListingReward(proof={self.proof}, looks_total={self.looks_total}, looks_24h={self.looks_24h}, date={self.date})")

    class _TradingReward:
        def __init__(self, proof, looks_total, looks_24h, volume_total, volume_24h, date):
            self.proof = proof
            self.looks_total = looks_total
            self.looks_24h = looks_24h
            self.volume_total = volume_total
            self.volume_24h = volume_24h
            self.date = date

        @classmethod
        def from_dict(cls, data):
            proof = data.get('proof')
            looks_total = data.get('looksTotal')
            looks_24h = data.get('looks24h')
            volume_total = data.get('volumeTotal')
            volume_24h = data.get('volume24h')
            date = data.get('date')
            return cls(proof, looks_total, looks_24h, volume_total, volume_24h, date)

        def __repr__(self):
            return (
                f"TradingReward(proof={self.proof}, looks_total={self.looks_total}, looks_24h={self.looks_24h}, volume_total={self.volume_total}, "
                f"volume_24h={self.volume_24h}, date={self.date})")
