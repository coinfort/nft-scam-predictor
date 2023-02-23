import datetime

from analyzer.model import NftScamClassifierModel
from entities import NftMetaplexMetadata, NftUriMetadata, metadata_hash
from entities.model import NftScamResponse
from services.nft import nft_metadata_repository
from services.nft.metadata.dto import (CreateNftMetadataDto,
                                       NftMetadataTokenHashDto,
                                       UpdateNftMetadataTimestampDto)
from solana_utils.rpc import SolanaRpcClient


def check_nft_token(
        model: NftScamClassifierModel,
        client: SolanaRpcClient,
        token_id: str
) -> NftScamResponse:
    metaplex_metadata_value = NftMetaplexMetadata()
    uri_metadata_value = NftUriMetadata()
    result = NftScamResponse.WRONG_INPUT

    metaplex_metadata = client.nft_metadata(token_id)
    if metaplex_metadata.is_ok():
        metaplex_metadata_value = metaplex_metadata.ok()
        uri_metadata = client.nft_uri_metadata(metaplex_metadata_value.data.uri)
        if uri_metadata.is_ok():
            uri_metadata_value = uri_metadata.ok()

    description = uri_metadata_value.description

    if description is not None:
        is_scam = model.check_scam([description])[0]
        result = NftScamResponse.SCAM if is_scam else NftScamResponse.NOT_SCAM

    meta_hash = metadata_hash(metaplex_metadata_value, uri_metadata_value)

    exists = nft_metadata_repository.exists(
        NftMetadataTokenHashDto(token_id=token_id, hash=meta_hash)
    )

    if not exists:
        dto = CreateNftMetadataDto(
            token_id=token_id,
            hash=meta_hash,
            metaplex_metadata=metaplex_metadata_value,
            uri_metadata=uri_metadata_value,
            result=result
        )
        nft_metadata_repository.save_nft_metadata(dto)
    else:
        dto = UpdateNftMetadataTimestampDto(
            token_id=token_id,
            hash=meta_hash,
            time=datetime.datetime.utcnow()
        )
        nft_metadata_repository.update_timestamp(dto)

    return result
