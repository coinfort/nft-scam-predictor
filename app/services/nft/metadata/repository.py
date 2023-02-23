import datetime
import typing as tp

from db.connection import get_db
from entities import NftMetadata as INftMeta
from entities.model import NftScamResponse

from .table import NftMetadata


class NftMetadataRepository:
    def __init__(self):
        self.db = get_db()

    def save_nft_metadata(self, metadata: INftMeta, result: NftScamResponse):
        metaplex_metadata = metadata.metaplex_metadata
        uri_metadata = metadata.uri_metadata

        nft = NftMetadata(
            token_id=metadata.token_id,
            hash=metadata.sha256(),
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
            predict_result=result.value
        )

        self.db.add(nft)
        self.db.commit()

    def find_by_token_and_hash(self, token_id: str, meta_hash: str) -> tp.Optional[NftMetadata]:
        return self.db \
            .query(NftMetadata.token_id, NftMetadata.hash) \
            .filter_by(token_id=token_id, hash=meta_hash) \
            .first()

    def exists(self, token_id: str, meta_hash: str) -> bool:
        return self.find_by_token_and_hash(token_id, meta_hash) is not None

    def find_by_token_id(self, token_id: str) -> tp.List[NftMetadata]:
        return self.db \
            .query(NftMetadata.token_id) \
            .filter_by(token_id=token_id)
