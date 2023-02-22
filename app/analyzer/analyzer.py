from enum import Enum

from ..sol.rpc import SolanaRpcClient
from .model import NftScamModel


class NFTScamResponse(Enum):
    NOT_SCAM = "good"
    SCAM = "scam"
    WRONG_INPUT = "invalid_input"


def check_nft_token(
        model: NftScamModel,
        client: SolanaRpcClient,
        token_address: str
) -> NFTScamResponse:
    result = client.nft_metadata(token_address)
    if result.is_err():
        return NFTScamResponse.WRONG_INPUT

    metadata = client.nft_uri_metadata(result.ok().data.uri)
    if metadata.is_err():
        return NFTScamResponse.WRONG_INPUT

    description = metadata.ok().description
    if description is None:
        return NFTScamResponse.WRONG_INPUT

    is_scam = model.check_scam([description])[0]
    return NFTScamResponse.SCAM if is_scam else NFTScamResponse.NOT_SCAM
