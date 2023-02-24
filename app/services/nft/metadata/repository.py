import datetime
import typing as tp

from db.connection import get_db

from .dto import *
from .table import NftMetadata


class NftMetadataRepository:
    def __init__(self):
        self.db = get_db()

    def save_nft_metadata(self, dto: CreateNftMetadataDto):
        metaplex_metadata = dto.metaplex_metadata
        uri_metadata = dto.uri_metadata

        nft = NftMetadata(
            token_id=dto.token_id,
            hash=dto.hash,
            update_authority=metaplex_metadata.update_authority,
            mint=metaplex_metadata.mint,
            title=metaplex_metadata.data.title,
            description=uri_metadata.description,
            is_mutable=metaplex_metadata.is_mutable,
            token_type="metaplex",  # TODO: Fix
            collection_id=None,  # TODO: Fix
            is_collection_verified=None,  # TODO: Fix
            seller_fee_basis_points=metaplex_metadata.data.seller_fee_basis_points,
            uri=metaplex_metadata.data.uri,
            image=uri_metadata.image,
            symbol=metaplex_metadata.data.symbol,
            external_uri=uri_metadata.external_uri,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
            predict_result=dto.result.value
        )

        self.db.add(nft)
        self.db.commit()

    def update_timestamp(self, dto: UpdateNftMetadataTimestampDto):
        self.db.query(NftMetadata).filter(
            NftMetadata.token_id == dto.token_id,
            NftMetadata.hash == dto.hash
        ).update({
            NftMetadata.updated_at: datetime.datetime.utcnow()
        })
        self.db.commit()

    def find_by_token_and_hash(self, dto: NftMetadataTokenHashDto) -> tp.Optional[NftMetadata]:
        return self.db \
            .query(NftMetadata.token_id, NftMetadata.hash) \
            .filter_by(token_id=dto.token_id, hash=dto.hash) \
            .first()

    def exists(self, dto: NftMetadataTokenHashDto) -> bool:
        return self.find_by_token_and_hash(dto) is not None

    def find_by_token_id(self, token_id: str) -> tp.List[NftMetadata]:
        return self.db \
            .query(NftMetadata.token_id) \
            .filter_by(token_id=token_id)
