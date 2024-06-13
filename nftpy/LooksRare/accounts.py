class Account:
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
