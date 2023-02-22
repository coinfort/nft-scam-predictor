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
    collection: tp.Optional[NftCollectionReference]


@dataclasses.dataclass
class NftUriMetadata:
    image: tp.Optional[str]
    description: tp.Optional[str]
    external_uri: tp.Optional[str]


@dataclasses.dataclass
class NftMetadata:
    token_id: str
    metaplex_metadata: NftMetaplexMetadata
    uri_metadata: NftUriMetadata

    def sha256(self) -> str:
        return dict_hash.sha256(dataclasses.asdict(self))[:64]


__all__ = [
    "NftCreator",
    "NftCollectionReference",
    "NftChainData",
    "NftMetaplexMetadata",
    "NftUriMetadata",
    "NftMetadata"
]
