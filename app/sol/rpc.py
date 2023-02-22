import base64
import enum

import requests
from result import Err, Ok, Result
from sol.datatypes import MetaplexMetadata, UriMetadata
from sol.metaplex.metadata import get_metadata_account, parse_metadata_bytes
from solana.publickey import PublicKey
from solana.rpc.api import Client as SolanaClient


class Endpoint(enum.Enum):
    ChainStack = "https://nd-209-102-701.p2pify.com/6081256af612c08bf51b0c0ab56924db"  # TODO: Extract to `.env `file
    Ankr = "https://rpc.ankr.com/solana"
    Mainnet = "https://api.mainnet-beta.solana.com"
    Testnet = "https://api.testnet.solana.com"
    Devnet = "https://api.devnet.solana.com"


def try_except_handler(func):
    """
    Wraps function invocation into try - except block.

    :param func Function for wrapping
    :return: Err if an exception occurs otherwise Ok
    """

    def wrapper(*args, **kwargs):
        try:
            data = func(*args, **kwargs)
            return Ok(data)
        except Exception as e:
            return Err(e)

    return wrapper


class SolanaRpcClient:
    def __init__(self, url: str):
        self.url = url
        self.client = SolanaClient(endpoint=url)

    @staticmethod
    def from_endpoint(endpoint: Endpoint = Endpoint.Mainnet) -> "SolanaRpcClient":
        return SolanaRpcClient(endpoint.value)

    @try_except_handler
    def nft_metadata(self, token_id: str) -> Result[MetaplexMetadata, Exception]:
        mint_pk = PublicKey(token_id)
        account = get_metadata_account(mint_pk)
        info = self.client.get_account_info(account)
        data = base64.b64decode(info["result"]["value"]["data"][0])
        metadata = parse_metadata_bytes(data)
        return metadata

    @try_except_handler
    def nft_uri_metadata(self, uri: str) -> Result[UriMetadata, Exception]:
        data = requests.get(uri).json()

        metadata = UriMetadata(
            image=data.get("image"),
            description=data.get("description"),
            external_url=data.get("external_url")
        )
        return metadata

    def __repr__(self):
        return f"{self.__class__.__name__}(url={self.url})"


__all__ = [
    "Endpoint",
    "SolanaRpcClient"
]
