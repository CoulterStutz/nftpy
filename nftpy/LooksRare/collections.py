class CollectionInformation:
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

class CollectionStats:
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
        change_3m = data.get('change3m')
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
