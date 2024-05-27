from web3 import Web3
from .abi import ABI
from .chains import Chains
from ..errors import *


class NFTWallet:
    def __init__(self, private_key, chain:Chains=None, rpc_url:str=None):
        self._private_key = private_key
        self.chain = chain
        self._rpc_url = rpc_url
        self._connections = []

        self._connect_to_chains()

    def _connect_to_chains(self):
        if self.chain == None and self._rpc_url == None:
            for x in Chains:
                conn = Web3(Web3.HTTPProvider(x.rpc_url))
                if not conn.is_connected():
                    raise InvalidRPCURL(url=x.rpc_url, chain=x.name)
                else:
                    self._connections.append(conn)
        elif self.chain != None and self._rpc_url == None:
            conn = Web3(Web3.HTTPProvider(self.chain.rpc_url))
            if not conn.is_connected():
                raise InvalidRPCURL(url=self.chain.rpc_url, chain=self.chain.name)
            else:
                self._connections.append(conn)
        elif self.chain != None and self._rpc_url != None:
            conn = Web3(Web3.HTTPProvider(self._rpc_url))
            if not conn.is_connected():
                raise InvalidRPCURL(url=self._rpc_url, chain=self.chain.name)
            else:
                self._connections.append(conn)
        elif self.chain == None and self._rpc_url != None:
            conn = Web3(Web3.HTTPProvider(self._rpc_url))
            if not conn.is_connected():
                raise InvalidRPCURL(url=self._rpc_url)
            else:
                self._connections.append(conn)