from enum import Enum

from analyzer.model import NftScamClassifierModel
from entities import NftMetadata
from services.nft import nft_metadata_repository
from solana_utils.rpc import SolanaRpcClient


class NftScamResponse(Enum):
    NOT_SCAM = "good"
    SCAM = "scam"
    WRONG_INPUT = "invalid input"


def check_nft_token(
        model: NftScamClassifierModel,
        client: SolanaRpcClient,
        token_id: str
) -> NftScamResponse:
    metaplex_metadata = client.nft_metadata(token_id)
    if metaplex_metadata.is_err():
        return NftScamResponse.WRONG_INPUT

    uri_metadata = client.nft_uri_metadata(metaplex_metadata.ok().data.uri)
    if uri_metadata.is_err():
        return NftScamResponse.WRONG_INPUT

    description = uri_metadata.ok().description
    if description is None:
        return NftScamResponse.WRONG_INPUT

    metadata = NftMetadata(
        token_id=token_id,
        metaplex_metadata=metaplex_metadata.ok(),
        uri_metadata=uri_metadata.ok()
    )

    exists = nft_metadata_repository.exists(token_id=token_id, meta_hash=metadata.sha256())

    if not exists:
        nft_metadata_repository.save_nft_metadata(metadata)

    is_scam = model.check_scam([description])[0]
    return NftScamResponse.SCAM if is_scam else NftScamResponse.NOT_SCAM
