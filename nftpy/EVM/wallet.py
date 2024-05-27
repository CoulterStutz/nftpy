from web3 import Web3
from .abi import ABI
from .chains import Chains
from ..errors import *


class NFTWallet:
    def __init__(self, private_key, chains: list[Chains] = None, rpc_url: str = None):
        self._private_key = private_key
        self.chains = chains or []
        self._rpc_url = rpc_url
        self._address = self._get_address_from_private_key()
        self._connections = self._connect_to_chains()

    def _get_address_from_private_key(self):
        account = Web3().eth.account.privateKeyToAccount(self._private_key)
        return account.address

    def _connect_to_chains(self):
        connections = []
        if not self.chains and not self._rpc_url:
            for chain in Chains:
                conn = Web3(Web3.HTTPProvider(chain.rpc_url))
                if not conn.isConnected():
                    raise InvalidRPCURL(url=chain.rpc_url, chain=chain.name)
                connections.append((chain, conn))
        elif self.chains and not self._rpc_url:
            for chain in self.chains:
                conn = Web3(Web3.HTTPProvider(chain.rpc_url))
                if not conn.isConnected():
                    raise InvalidRPCURL(url=chain.rpc_url, chain=chain.name)
                connections.append((chain, conn))
        elif self.chains and self._rpc_url:
            for chain in self.chains:
                conn = Web3(Web3.HTTPProvider(self._rpc_url))
                if not conn.isConnected():
                    raise InvalidRPCURL(url=self._rpc_url, chain=chain.name)
                connections.append((chain, conn))
        elif not self.chains and self._rpc_url:
            conn = Web3(Web3.HTTPProvider(self._rpc_url))
            if not conn.isConnected():
                raise InvalidRPCURL(url=self._rpc_url)
            connections.append((None, conn))
        return connections

    def get_balance(self, chain: Chains = None) -> dict:
        balances = {}
        if chain:
            conn = Web3(Web3.HTTPProvider(chain.rpc_url))
            if conn.isConnected():
                balance = conn.eth.get_balance(self._address)
                balances[chain.name] = Web3.fromWei(balance, 'ether')
            else:
                raise InvalidRPCURL(url=chain.rpc_url, chain=chain.name)
        else:
            for chain, conn in self._connections:
                symbol = chain.name if chain else "Balance"
                balance = conn.eth.get_balance(self._address)
                balances[symbol] = Web3.fromWei(balance, 'ether')
        return balances

    def get_transaction_history(self, limit: int = 10, chain: Chains = None) -> dict:
        history = {}
        if chain:
            conn = Web3(Web3.HTTPProvider(chain.rpc_url))
            if conn.isConnected():
                transactions = conn.eth.get_transaction_by_address(self._address, limit)
                history[chain.name] = transactions
            else:
                raise InvalidRPCURL(url=chain.rpc_url, chain=chain.name)
        else:
            for chain, conn in self._connections:
                if conn.isConnected():
                    transactions = conn.eth.get_transaction_by_address(self._address, limit)
                    history[chain.name] = transactions
                else:
                    raise InvalidRPCURL(url=chain.rpc_url, chain=chain.name)
        return history

    def get_gas_price(self, chain: Chains = None) -> dict:
        gas_prices = {}
        if chain:
            conn = Web3(Web3.HTTPProvider(chain.rpc_url))
            if conn.isConnected():
                gas_price = conn.eth.gas_price
                gas_prices[chain.name] = gas_price
            else:
                raise InvalidRPCURL(url=chain.rpc_url, chain=chain.name)
        else:
            for chain, conn in self._connections:
                gas_price = conn.eth.gas_price
                gas_prices[chain.name] = gas_price
        return gas_prices
