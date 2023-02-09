import typing as tp

import requests
from solana.rpc.api import Client

from .model import NftScamModel
from .check_state import Response
from .metaplex import metadata


def check_nft_token(model: NftScamModel, token_address: str) -> Response:
    description = nft_description(token_address)

    if description is None:  # Todo: Fix this behavior
        return Response.WRONG_INPUT

    is_scam = model.check_scam([description])[0]
    return Response.SCAM if is_scam else Response.NOT_SCAM


def nft_metadata(token_address: str) -> tp.Dict[str, tp.Any]:
    mainnet_api_url = "http://api.mainnet-beta.solana.com"
    client = Client(mainnet_api_url)
    data = metadata.get_metadata(client, token_address)["data"]
    return data


def nft_description(token_address: str) -> tp.Optional[str]:
    try:
        data = nft_metadata(token_address)
        data = requests.get(data["uri"]).json()
        return data["description"]
    except Exception as _:
        return None


__all__ = ["check_nft_token"]
