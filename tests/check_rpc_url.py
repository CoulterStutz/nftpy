import time
from web3 import Web3
from nftpy import Chains
from nftpy.errors import InvalidRPCURL


def check_rpc_urls():
    """
    Check the RPC URLs for all chains in the Chains enum.

    Returns:
        str: A success message if all RPC URLs are valid.

    Raises:
        InvalidRPCURL: If any RPC URL is invalid.
    """
    connections = []
    for chain in Chains:
        try:
            conn = Web3(Web3.HTTPProvider(chain.rpc_url))
            if not conn.is_connected():
                raise InvalidRPCURL(chain.rpc_url, chain.name)
            connections.append((chain.value, conn))
        except Exception as e:
            return f"Invalid RPC URL provided for {chain.name}! {chain.rpc_url}. Error: {str(e)}"

    return "All RPC URLs are valid!"


# Running the check
result = check_rpc_urls()
print(result)

# Raise an error if the check fails to ensure GitHub workflows can catch it
if result != "All RPC URLs are valid!":
    raise Exception(result)
