from abi import ABI
from chains import Chains

class NFTWallet:
    def __init__(self, private_key, chain:Chains=None):
        self.private_key = private_key
        self.chain = chain
        self.wallets = []

