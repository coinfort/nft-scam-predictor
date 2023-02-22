import typing as tp

import requests
from solana.rpc.api import Client

from .model import NftScamModel
from .check_state import Response
from .metaplex import metadata
from .database.utils import write_metadata_to_bd


def check_nft_token(model: NftScamModel, token_address: str) -> Response:
    metadata_dict = {}
    description = nft_description(token_address, metadata_dict)
    write_metadata_to_bd(token_address, metadata_dict)

    if description is None:  # Todo: Fix this behavior
        return Response.WRONG_INPUT

    is_scam = model.check_scam([description])[0]
    return Response.SCAM if is_scam else Response.NOT_SCAM


def nft_description(token_address: str, metadata_dict: dict) -> tp.Optional[str]:
    try:
        data = nft_metadata(token_address, metadata_dict)
        if data is None:
            metadata_dict["Title"] = None
            metadata_dict["Description"] = None
            metadata_dict["Symbol"] = None
            metadata_dict["TokenUri"] = None
            metadata_dict["Image"] = None
            return None
        metadata_dict["Title"] = data.get("name")
        metadata_dict["Description"] = data.get("description")
        metadata_dict["Symbol"] = data.get("symbol")
        metadata_dict["TokenUri"] = data.get("uri")
        metadata_dict["Image"] = data.get("image")

        data = requests.get(data["uri"]).json()
        return data["description"]
    except Exception as _:
        return None


def nft_metadata(token_address: str, metadata_dict: dict) -> tp.Dict[str, tp.Any]:
    mainnet_api_url = "http://api.mainnet-beta.solana.com"
    client = Client(mainnet_api_url)
    data = metadata.get_metadata(client, token_address)

    metadata_dict["UpdateAuthority"] = data.get("update_authority")
    metadata_dict["Mint"] = data.get("mint")
    metadata_dict["IsMutable"] = data.get("is_mutable")
    metadata_dict["TokenType"] = data.get("type")
    metadata_dict["ExternalUri"] = data.get("external_url")
    collection = data.get("collection")
    if collection is not None:
        metadata_dict["CollectionID"] = collection.get('key')
        metadata_dict["IsCollectionVerified"] = collection.get('verified')
    else:
        metadata_dict["CollectionID"] = None
        metadata_dict["IsCollectionVerified"] = None

    return data["data"]

__all__ = ["check_nft_token"]
