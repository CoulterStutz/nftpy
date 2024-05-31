import time
from threading import Thread
from web3 import Web3
from web3.exceptions import TransactionNotFound
from .abi import ABI
from .chains import Chains
from ..errors import *

class NFTWallet:
    """
    A class to interact with NFTs on various EVM Based networks from a wallet.

    Args:
        private_key (str, optional): The private key of the wallet for full access.
        address (str, optional): The address of the wallet for read-only access.
        chains (list[Chains], optional): A list of blockchain networks to connect to.
        rpc_url (str, optional): Custom RPC URL to connect to.
    """
    def __init__(self, private_key: str = None, address: str = None, chains: list = None, rpc_url: str = None):
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
        def connect(chain, connections):
            conn = Web3(Web3.HTTPProvider(chain.rpc_url))
            if not conn.is_connected():
                raise InvalidRPCURL(chain.rpc_url, chain.name)
            connections.append((chain, conn))

        connections = []
        threads = []

        if not self.chains and not self._rpc_url:
            for chain in Chains:
                thread = Thread(target=connect, args=(chain, connections))
                threads.append(thread)
                thread.start()
        elif self.chains and not self._rpc_url:
            for chain in self.chains:
                thread = Thread(target=connect, args=(chain, connections))
                threads.append(thread)
                thread.start()
        elif self.chains and self._rpc_url:
            for chain in self.chains:
                thread = Thread(target=connect, args=(chain, connections))
                threads.append(thread)
                thread.start()
        elif not self.chains and self._rpc_url:
            conn = Web3(Web3.HTTPProvider(self._rpc_url))
            if not conn.is_connected():
                raise InvalidRPCURL(self._rpc_url)
            connections.append((None, conn))

        for thread in threads:
            thread.join()

        return connections

    def get_balance_wei(self, chain=None) -> dict:
        """
        Get the balance of the wallet in Wei.

        Args:
            chain (Chains, optional): The specific chain to get the balance from if not defined in wallet

        Returns:
            dict: A dictionary with the chain symbol as key and the balance as value.
        """
        balances = {}
        if chain:
            conn = Web3(Web3.HTTPProvider(chain.rpc_url))
            if conn.is_connected():
                balance = conn.eth.get_balance(self._address)
                balances[chain.symbol] = balance
            else:
                raise InvalidRPCURL(chain.rpc_url, chain.name)
        else:
            for chain, conn in self._connections:
                symbol = chain.symbol if chain else "Balance"
                balance = conn.eth.get_balance(self._address)
                balances[symbol] = balance
        return balances

    def get_balance(self, chain=None) -> dict:
        """
        Get the balance of the wallet in Ether.

        Args:
            chain (Chains, optional): The specific chain to get the balance from if not defined in wallet

        Returns:
            dict: A dictionary with the chain symbol as key and the balance as value.
        """
        balances = {}
        if chain:
            conn = Web3(Web3.HTTPProvider(chain.rpc_url))
            if conn.is_connected():
                balance = conn.eth.get_balance(self._address)
                balances[chain.symbol] = Web3.from_wei(balance, 'ether')
            else:
                raise InvalidRPCURL(chain.rpc_url, chain.name)
        else:
            for chain, conn in self._connections:
                symbol = chain.symbol if chain else "Balance"
                balance = conn.eth.get_balance(self._address)
                balances[symbol] = Web3.from_wei(balance, 'ether')
        return {"Balances": balances}

    def get_gas_price_wei(self, chain=None) -> dict:
        """
        Get the current gas price in Wei.

        Args:
            chain (Chains, optional): The specific chain to get the gas price from.

        Returns:
            dict: A dictionary with the chain symbol as key and the gas price as value.
        """
        gas_prices = {}
        if chain:
            conn = Web3(Web3.HTTPProvider(chain.rpc_url))
            if conn.is_connected():
                gas_price = conn.eth.gas_price
                gas_prices[chain.symbol] = gas_price
            else:
                raise InvalidRPCURL(chain.rpc_url, chain.name)
        else:
            for chain, conn in self._connections:
                gas_price = conn.eth.gas_price
                gas_prices[chain.symbol] = gas_price
        return gas_prices

    def get_gas_price_gwei(self, chain=None) -> dict:
        """
        Get the current gas price in Gwei.

        Args:
            chain (Chains, optional): The specific chain to get the gas price from.

        Returns:
            dict: A dictionary with the chain symbol as key and the gas price as value.
        """
        gas_prices = {}
        if chain:
            conn = Web3(Web3.HTTPProvider(chain.rpc_url))
            if conn.is_connected():
                gas_price = conn.eth.gas_price
                gas_prices[chain.symbol] = Web3.from_wei(gas_price, 'gwei')
            else:
                raise InvalidRPCURL(chain.rpc_url, chain.name)
        else:
            for chain, conn in self._connections:
                gas_price = conn.eth.gas_price
                gas_prices[chain.symbol] = Web3.from_wei(gas_price, 'gwei')
        return gas_prices

    def transfer_nft(self, to: str, contract_address: str, amount: int, gas_limit: int, gas_price_gwei: int = None,
                     gas_price_wei: int = None, abi: ABI = None, abi_str: str = None,
                     chain = None, token_id: int = None) -> dict:
        """
        Transfer an NFT to another wallet.

        Args:
            to (str): The recipient wallet address.
            contract_address (str): The contract address of the NFT.
            amount (int): The amount of NFTs to transfer.
            gas_limit (int): The gas limit for the transaction.
            gas_price_gwei (int, optional): The gas price in Gwei.
            gas_price_wei (int, optional): The gas price in Wei.
            abi (ABI, optional): The ABI from the ABI class.
            abi_str (str, optional): The ABI as a string.
            chain (Chains, optional): The specific chain to perform the transfer on.
            token_id (int, optional): The token ID of the NFT to transfer.

        Returns:
            dict: A dictionary with the transaction hash and explorer URL.
        """
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

        nonce = conn.eth.get_transaction_count(self._address)
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
            if chain.explorer_url != None:
                return {
                    'transaction_hash': tx_hash.hex(),
                    'explorer_url': f"{chain.explorer_url}/tx/{tx_hash.hex()}"
                }
            else:
                return {
                    'transaction_hash': tx_hash.hex(),
                }
        except ValueError as e:
            if 'gas' in str(e):
                raise TransactionGasError()
            elif 'balance' in str(e):
                raise TransactionBalanceError()
            else:
                raise e

    def wait_until_transaction_processes(self, tx_hash, chain) -> bool:
        """
        Wait until a transaction is processed.

        Args:
            tx_hash (str or bytes): The transaction hash.
            chain (Chains): The specific chain to check the transaction on.

        Returns:
            bool: True if the transaction is processed, False otherwise.
        """
        if isinstance(tx_hash, str):
            tx_hash = Web3.to_bytes(hexstr=tx_hash)

        conn = Web3(Web3.HTTPProvider(chain.rpc_url))
        if not conn.is_connected():
            raise InvalidRPCURL(chain.rpc_url, chain.name)

        while True:
            try:
                receipt = conn.eth.get_transaction_receipt(tx_hash)
                if receipt is not None and receipt.status == 1:
                    return True
            except TransactionNotFound:
                pass
            time.sleep(1)

    def get_transaction_count(self, chain=None) -> dict:
        """
        Get the number of transactions sent from the address.

        Args:
            chain (Chains, optional): The specific chain to get the transaction count from.

        Returns:
            dict: A dictionary with the chain symbol as key and the transaction count as value.
        """
        counts = {}
        if chain:
            conn = Web3(Web3.HTTPProvider(chain.rpc_url))
            if conn.is_connected():
                count = conn.eth.get_transaction_count(self._address)
                counts[chain.symbol] = count
            else:
                raise InvalidRPCURL(chain.rpc_url, chain.name)
        else:
            for chain, conn in self._connections:
                count = conn.eth.get_transaction_count(self._address)
                counts[chain.symbol] = count
        return counts

    def estimate_gas(self, to: str, value: int, data: bytes = b'', chain=None) -> dict:
        """
        Estimate the gas required for a transaction.

        Args:
            to (str): The recipient address.
            value (int): The value to send in Wei.
            data (bytes, optional): The data to include in the transaction.
            chain (Chains, optional): The specific chain to estimate the gas on.

        Returns:
            dict: A dictionary with the chain symbol as key and the gas estimate as value.
        """
        estimates = {}
        if chain:
            conn = Web3(Web3.HTTPProvider(chain.rpc_url))
            if conn.is_connected():
                estimate = conn.eth.estimate_gas({'to': to, 'value': value, 'data': data})
                estimates[chain.symbol] = estimate
            else:
                raise InvalidRPCURL(chain.rpc_url, chain.name)
        else:
            for chain, conn in self._connections:
                estimate = conn.eth.estimate_gas({'to': to, 'value': value, 'data': data})
                estimates[chain.symbol] = estimate
        return estimates

    def is_synced(self, chain=None) -> dict:
        """
        Check if the blockchain is synced for RPC debugging!

        Args:
            chain (Chains, optional): The specific chain to check the sync status on.

        Returns:
            dict: A dictionary with the chain symbol as key and the sync status as value.
        """
        sync_status = {}
        if chain:
            conn = Web3(Web3.HTTPProvider(chain.rpc_url))
            if conn.is_connected():
                synced = not conn.eth.syncing
                sync_status[chain.symbol] = synced
            else:
                raise InvalidRPCURL(chain.rpc_url, chain.name)
        else:
            for chain, conn in self._connections:
                synced = not conn.eth.syncing
                sync_status[chain.symbol] = synced
        return sync_status

    def get_latest_block(self, chain=None) -> dict:
        """
        Get the latest block details.

        Args:
            chain (Chains, optional): The specific chain to get the latest block from.

        Returns:
            dict: A dictionary with the chain symbol as key and the latest block details as value.
        """
        blocks = {}
        if chain:
            conn = Web3(Web3.HTTPProvider(chain.rpc_url))
            if conn.is_connected():
                block = conn.eth.get_block('latest')
                blocks[chain.symbol] = block
            else:
                raise InvalidRPCURL(chain.rpc_url, chain.name)
        else:
            for chain, conn in self._connections:
                block = conn.eth.get_block('latest')
                blocks[chain.symbol] = block
        return blocks
