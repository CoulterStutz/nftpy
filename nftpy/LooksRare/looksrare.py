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