class NFTException(Exception):
    """Base class for exceptions in the NFT class."""
    pass

class InvalidRPCURL(NFTException):
    """Raised when an invalid RPC URL is provided."""
    def __init__(self, url, chain=None):
        super().__init__()

class ContractFunctionFailed(NFTException):
    """Raised when a contract function call fails."""
    def __init__(self, function_name):
        super().__init__()

class TransactionGasError(NFTException):
    """Raised when a transaction fails due to insufficient gas."""
    pass

class TransactionBalanceError(NFTException):
    """Raised when a transaction fails due to insufficient balance."""
    pass

class OpenSeaException(Exception):
    """Base class for exceptions in the OpenSea class."""
    pass

class MissingSlug(OpenSeaException):
    """Raised when a collection slug is required but not provided."""
    def __init__(self):
        super().__init__()

class MissingChain(OpenSeaException):
    """Raised when a chain is required but not provided."""
    def __init__(self):
        super().__init__()

class APIRequestFailed(OpenSeaException):
    """Raised when an API request fails."""
    def __init__(self, status_code):
        super().__init__()
