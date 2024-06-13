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
