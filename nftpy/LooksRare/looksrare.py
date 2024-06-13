from enum import Enum
from ..errors import APIKeyNotSpecifiedOnMainnetError
from termcolor import colored

class LooksRareChain(Enum):
    MAINNET = "https://api.looksrare.org/api/"
    SEPOLIA = "https://api-sepolia.looksrare.org/api/"

class LooksRareAPI:
    def __init__(self, chain:LooksRareChain, api_key:str=None, suppress_warnings:bool=False, version:int=2):
        self._chain = chain
        self._api_key = api_key
        self._version = version
        if self._chain == LooksRareChain.MAINNET:
            if self._api_key is None and self._version == 2:
                raise APIKeyNotSpecifiedOnMainnetError()
        elif self._chain == LooksRareChain.SEPOLIA:
            if self._api_key is not None and suppress_warnings is False:
                print(colored("[NFTPY]: Warning! API key isn't needed for the Sepolia Network!", 'yellow'))

