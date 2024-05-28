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
        return {"Balances": balances}

    def get_gas_price_wei(self, chain: Chains = None) -> dict:
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

    def get_gas_price_gwei(self, chain: Chains = None) -> dict:
        gas_prices = {}
        if chain:
            conn = Web3(Web3.HTTPProvider(chain.rpc_url))
            if conn.is_connected():
                gas_price = conn.eth.gas_price
                gas_prices[chain.name] = Web3.from_wei(gas_price, 'gwei')
            else:
                raise InvalidRPCURL(chain.rpc_url, chain.name)
        else:
            for chain, conn in self._connections:
                gas_price = conn.eth.gas_price
                gas_prices[chain.name] = Web3.from_wei(gas_price, 'gwei')
        return gas_prices

    def transfer_nft(self, to: str, contract_address: str, amount: int, gas_price_gwei: int = None,
                     gas_price_wei: int = None, gas_limit: int, abi: ABI = None, abi_str: str = None,
                     chain: Chains = None, token_id: int = None) -> dict:
        if not self._private_key:
            raise WalletReadOnlyError()
        if chain is None and not self.chains:
            raise MissingChainError()
        chain = chain or self.chains[0]

        if gas_price_gwei is None and gas_price_wei is None:
            raise ValueError("Either gas_price_gwei or gas_price_wei must be provided.")

        gas_price = gas_price_wei if gas_price_wei is not None else Web3.to_wei(gas_price_gwei, 'gwei')

        conn = Web3(Web3.HTTPProvider(chain.rpc_url))
        if not conn.is_connected():
            raise InvalidRPCURL(chain.rpc_url, chain.name)

        if abi is not None:
            contract_abi = abi.value
        elif abi_str is not None:
            contract_abi = abi_str
        else:
            raise ValueError("Either abi or abi_str must be provided.")

        contract = conn.eth.contract(address=contract_address, abi=contract_abi)

        nonce = conn.eth.getTransactionCount(self._address)
        tx = {
            'nonce': nonce,
            'to': contract_address,
            'value': 0,
            'gas': gas_limit,
            'gasPrice': gas_price,
            'data': contract.functions.safeTransferFrom(self._address, to, token_id, amount, b'').build_transaction({
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
