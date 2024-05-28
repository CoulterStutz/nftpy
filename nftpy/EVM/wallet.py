from web3 import Web3
from .abi import ABI
from .chains import Chains
from ..errors import *

class NFTWallet:
    def __init__(self, private_key: str = None, address: str = None, chains: list[Chains] = None, rpc_url: str = None):
        if not private_key and not address:
            raise NoCredentialsProvidedError()
        self._private_key = private_key
        self._address = address or self._get_address_from_private_key()
        self.chains = chains or []
        self._rpc_url = rpc_url
        self._connections = self._connect_to_chains()

    def _get_address_from_private_key(self):
        account = Web3().eth.account.from_key(self._private_key)
        return account.address

    def _connect_to_chains(self):
        connections = []
        if not self.chains and not self._rpc_url:
            for chain in Chains:
                conn = Web3(Web3.HTTPProvider(chain.rpc_url))
                if not conn.is_connected():
                    raise InvalidRPCURL(chain.rpc_url, chain.name)
                connections.append((chain, conn))
        elif self.chains and not self._rpc_url:
            for chain in self.chains:
                conn = Web3(Web3.HTTPProvider(chain.rpc_url))
                if not conn.is_connected():
                    raise InvalidRPCURL(chain.rpc_url, chain.name)
                connections.append((chain, conn))
        elif self.chains and self._rpc_url:
            for chain in self.chains:
                conn = Web3(Web3.HTTPProvider(self._rpc_url))
                if not conn.is_connected():
                    raise InvalidRPCURL(self._rpc_url, chain.name)
                connections.append((chain, conn))
        elif not self.chains and self._rpc_url:
            conn = Web3(Web3.HTTPProvider(self._rpc_url))
            if not conn.is_connected():
                raise InvalidRPCURL(self._rpc_url)
            connections.append((None, conn))
        return connections

    def get_balance(self, chain: Chains = None) -> dict:
        balances = {}
        if chain:
            conn = Web3(Web3.HTTPProvider(chain.rpc_url))
            if conn.is_connected():
                balance = conn.eth.get_balance(self._address)
                balances[chain.name] = Web3.from_wei(balance, 'ether')
            else:
                raise InvalidRPCURL(chain.rpc_url, chain.name)
        else:
            for chain, conn in self._connections:
                symbol = chain.name if chain else "Balance"
                balance = conn.eth.get_balance(self._address)
                balances[symbol] = Web3.from_wei(balance, 'ether')
        return balances

    def get_gas_price(self, chain: Chains = None) -> dict:
        gas_prices = {}
        if chain:
            conn = Web3(Web3.HTTPProvider(chain.rpc_url))
            if conn.is_connected():
                gas_price = conn.eth.gas_price
                gas_prices[chain.name] = gas_price
            else:
                raise InvalidRPCURL(chain.rpc_url, chain.name)
        else:
            for chain, conn in self._connections:
                gas_price = conn.eth.gas_price
                gas_prices[chain.name] = gas_price
        return gas_prices

    def transfer_nft(self, to: str, contract_address: str, amount: int, gas_price: int, gas_limit: int, abi: ABI, chain: Chains = None) -> dict:
        if not self._private_key:
            raise WalletReadOnlyError()
        if chain is None and not self.chains:
            raise MissingChainError()
        chain = chain or self.chains[0]

        conn = Web3(Web3.HTTPProvider(chain.rpc_url))
        if not conn.is_connected():
            raise InvalidRPCURL(chain.rpc_url, chain.name)

        contract = conn.eth.contract(address=contract_address, abi=abi.value)

        nonce = conn.eth.get_transaction_count(self._address)
        tx = {
            'nonce': nonce,
            'to': contract_address,
            'value': 0,
            'gas': gas_limit,
            'gasPrice': gas_price,
            'data': contract.functions.transferFrom(self._address, to, amount).build_transaction({
                'gas': gas_limit,
                'gasPrice': gas_price
            })['data'],
        }

        signed_tx = conn.eth.account.sign_transaction(tx, private_key=self._private_key)

        try:
            tx_hash = conn.eth.send_raw_transaction(signed_tx.rawTransaction)
            return {
                'transaction_hash': tx_hash.hex(),
                'explorer_url': f"{chain.explorer_url}/tx/{tx_hash.hex()}"
            }
        except ValueError as e:
            if 'gas' in str(e):
                raise TransactionGasError()
            elif 'balance' in str(e):
                raise TransactionBalanceError()
            else:
                raise e
