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

class ContractFunctionFailedError(NFTException):
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
        self.message = "Either private_key or address must be provided. Using address will grant you with a read-only interface. Transactions can be made by supplying a private key."
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
        self.message = "Chain or RPC URL must be provided."
        super().__init__(self.message)

class APIRequestFailedError(OpenSeaException):
    """Raised when an API request fails."""
    def __init__(self, status_code):
        self.message = f"API request failed with status code {status_code}."
        super().__init__(self.message)

class RaribleException(Exception):
    """Base class for exceptions in Rarible class."""
    pass

class MissingCollectionIdError(RaribleException):
    """Raised when a collection ID is required but not provided."""
    def __init__(self):
        self.message = "Collection ID must be provided."
        super().__init__(self.message)

class MissingItemIdError(RaribleException):
    """Raised when an item ID is required but not provided."""
    def __init__(self):
        self.message = "Item ID must be provided."
        super().__init__(self.message)

class APIRequestFailedError(RaribleException):
    """Raised when an API request fails."""
    def __init__(self, status_code):
        self.message = f"API request failed with status code {status_code}."
        super().__init__(self.message)

class LooksRareException(Exception):
    """Base class for exceptions in LooksRare class."""
    pass

class APIKeyNotSpecifiedOnMainnetError(LooksRareException):
    def __init__(self):
        self.message = "LooksRareAPI requires an API key for mainnet operation"
        super().__init__(self.message)

class RateLimitExceededError(LooksRareException):
    def __init__(self, message="LooksRare API Rate limit exceeded. Please try again later."):
        self.message = message
        super().__init__(self.message)

class APIKeyRequiredForPostError(LooksRareException):
    def __init__(self, message="LooksRare API key is required for POST requests on v1."):
        self.message = message
        super().__init__(self.message)

class InvalidLooksRareAPIRequest(LooksRareException):
    def __init__(self, message="Invalid request to the LooksRare API."):
        self.message = message
        super().__init__(self.message)