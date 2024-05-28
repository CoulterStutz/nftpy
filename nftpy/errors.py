class NFTException(Exception):
    """Base class for exceptions in NFT class."""
    pass

class InvalidRPCURL(NFTException):
    """Raised when an invalid RPC URL is provided."""
    def __init__(self, url, chain=None):
        if chain is None:
            self.message = f"Invalid RPC URL provided! {url}"
        else:
            self.message = f"Invalid RPC URL provided for {chain}! {url}"
        super().__init__(self.message)

class ContractFunctionFailed(NFTException):
    """Raised when a contract function call fails."""
    def __init__(self, function_name):
        self.message = f"Contract function '{function_name}' call failed."
        super().__init__(self.message)

class TransactionGasError(NFTException):
    """Raised when a transaction fails due to insufficient gas."""
    def __init__(self):
        self.message = "Transaction failed due to insufficient gas."
        super().__init__(self.message)

class TransactionBalanceError(NFTException):
    """Raised when a transaction fails due to insufficient balance."""
    def __init__(self):
        self.message = "Transaction failed due to insufficient balance."
        super().__init__(self.message)

    class WalletReadOnlyError(NFTException):
        """Raised when a transaction fails due to insufficient balance."""

        def __init__(self):
            self.message = "Transaction failed due to insufficient balance."
            super().__init__(self.message)

class NoCredentialsProvidedError(NFTException):
    """Raised when neither private_key nor address is provided."""
    def __init__(self):
        self.message = "Either private_key or address must be provided. Using address will grant you with a read only interface. Transactions can be made by supplying a private key"
        super().__init__(self.message)

class OpenSeaException(Exception):
    """Base class for exceptions in OpenSea class."""
    pass

class MissingSlugError(OpenSeaException):
    """Raised when a collection slug is required but not provided."""
    def __init__(self):
        self.message = "Collection slug must be provided."
        super().__init__(self.message)

class MissingChainError(OpenSeaException):
    """Raised when a chain is required but not provided."""
    def __init__(self):
        self.message = "Chain must be provided."
        super().__init__(self.message)

class APIRequestFailedError(OpenSeaException):
    """Raised when an API request fails."""
    def __init__(self, status_code):
        self.message = f"API request failed with status code {status_code}."
        super().__init__(self.message)
