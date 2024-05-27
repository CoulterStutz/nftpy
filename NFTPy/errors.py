class NFTException(Exception):
    """Base class for exceptions in NFT class."""
    pass

class InvalidRPCURL(NFTException):
    """Raised when an invalid RPC URL is provided."""
    def __init__(self):
        self.message = "Invalid RPC URL provided."
        super().__init__(self.message)

class ContractFunctionFailed(NFTException):
    """Raised when a contract function call fails."""
    def __init__(self, function_name):
        self.message = f"Contract function '{function_name}' call failed."
        super().__init__(self.message)

class OpenSeaException(Exception):
    """Base class for exceptions in OpenSea class."""
    pass

class MissingSlug(OpenSeaException):
    """Raised when a collection slug is required but not provided."""
    def __init__(self):
        self.message = "Collection slug must be provided."
        super().__init__(self.message)

class MissingChain(OpenSeaException):
    """Raised when a chain is required but not provided."""
    def __init__(self):
        self.message = "Chain must be provided."
        super().__init__(self.message)

class APIRequestFailed(OpenSeaException):
    """Raised when an API request fails."""
    def __init__(self, status_code):
        self.message = f"API request failed with status code {status_code}."
        super().__init__(self.message)