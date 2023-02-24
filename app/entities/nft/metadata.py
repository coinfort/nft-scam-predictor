import dataclasses
import typing as tp

import dict_hash


@dataclasses.dataclass
class NftCreator:
    address: str
    verified: bool
    share: int


@dataclasses.dataclass
class NftCollectionReference:
    verified: bool
    key: str


@dataclasses.dataclass
class NftChainData:
    title: str
    symbol: str
    uri: str
    seller_fee_basis_points: int
    creators: tp.List[NftCreator]


@dataclasses.dataclass
class NftMetaplexMetadata:
    update_authority: str
    mint: str
    data: NftChainData
    is_mutable: bool
    primary_sale_happened: bool
    collection: NftCollectionReference


@dataclasses.dataclass
class NftUriMetadata:
    image: tp.Optional[str] = None
    description: tp.Optional[str] = None
    external_uri: tp.Optional[str] = None


def metadata_hash(
        metaplex_metadata: NftMetaplexMetadata,
        uri_metadata: NftUriMetadata
) -> str:
    meta = {
        "metaplex_metadata": dataclasses.asdict(metaplex_metadata),
        "uri_metadata": dataclasses.asdict(uri_metadata)
    }

    return dict_hash.sha256(meta)[:64]


__all__ = [
    "NftCreator",
    "NftCollectionReference",
    "NftChainData",
    "NftMetaplexMetadata",
    "NftUriMetadata",
    "metadata_hash"
]
