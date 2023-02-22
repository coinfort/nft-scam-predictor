import base64
import enum

import requests
from config import settings
from entities.nft.metadata import NftMetaplexMetadata, NftUriMetadata
from result import Err, Ok, Result
from solana.publickey import PublicKey
from solana.rpc.api import Client as SolanaClient
from solana_utils.metaplex.metadata import (get_metadata_account,
                                            parse_metadata_bytes)


class Endpoint(enum.Enum):
    ChainStack = settings.CHAINSTACK_NODE_URL
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
    def nft_metadata(self, token_id: str) -> Result[NftMetaplexMetadata, Exception]:
        mint_pk = PublicKey(token_id)
        account = get_metadata_account(mint_pk)
        info = self.client.get_account_info(account)
        data = base64.b64decode(info["result"]["value"]["data"][0])
        metadata = parse_metadata_bytes(data)
        return metadata

    @try_except_handler
    def nft_uri_metadata(self, uri: str) -> Result[NftUriMetadata, Exception]:
        data = requests.get(uri).json()

        metadata = NftUriMetadata(
            image=data.get("image"),
            description=data.get("description"),
            external_uri=data.get("external_url")
        )

        return metadata

    def __repr__(self):
        return f"{self.__class__.__name__}(url={self.url})"


__all__ = [
    "Endpoint",
    "SolanaRpcClient"
]
