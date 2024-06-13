class ListingReward:
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
        return (f"ListingReward(proof={self.proof}, looks_total={self.looks_total}, looks_24h={self.looks_24h}, date={self.date})")

class TradingReward:
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
        return (f"TradingReward(proof={self.proof}, looks_total={self.looks_total}, looks_24h={self.looks_24h}, volume_total={self.volume_total}, "
                f"volume_24h={self.volume_24h}, date={self.date})")

class Reward:
    def __init__(self, address, listing=None, trading=None):
        self.address = address
        self.listing = listing
        self.trading = trading

    @classmethod
    def from_dict(cls, data):
        address = data.get('address')
        listing = ListingReward.from_dict(data.get('listing')) if data.get('listing') else None
        trading = TradingReward.from_dict(data.get('trading')) if data.get('trading') else None
        return cls(address, listing, trading)

    def __repr__(self):
        return (f"Reward(address={self.address}, listing={self.listing}, trading={self.trading})")
