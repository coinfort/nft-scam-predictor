from analyzer.model import NftScamClassifierModel
from entities import NftMetadata, NftMetaplexMetadata, NftUriMetadata
from entities.model import NftScamResponse
from services.nft import nft_metadata_repository
from solana_utils.rpc import SolanaRpcClient


def check_nft_token(
        model: NftScamClassifierModel,
        client: SolanaRpcClient,
        token_id: str
) -> NftScamResponse:
    metaplex_metadata_value = NftMetaplexMetadata()
    uri_metadata_value = NftUriMetadata()
    description = None
    result = NftScamResponse.WRONG_INPUT

    metaplex_metadata = client.nft_metadata(token_id)
    if metaplex_metadata.is_ok():
        metaplex_metadata_value = metaplex_metadata.ok()
        uri_metadata = client.nft_uri_metadata(metaplex_metadata_value.data.uri)
        if uri_metadata.is_ok():
            uri_metadata_value = uri_metadata.ok()
            description = uri_metadata_value.description

    metadata = NftMetadata(
        token_id=token_id,
        metaplex_metadata=metaplex_metadata_value,
        uri_metadata=uri_metadata_value
    )

    if description is not None:
        is_scam = model.check_scam([description])[0]
        result = NftScamResponse.SCAM if is_scam else NftScamResponse.NOT_SCAM

    exists = nft_metadata_repository.exists(token_id=token_id, meta_hash=metadata.sha256())

    if not exists:
        nft_metadata_repository.save_nft_metadata(metadata, result)
    else:
        pass  # add update time

    return result
