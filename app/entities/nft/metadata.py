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
    update_authority: tp.Optional[str] = None
    mint: tp.Optional[str] = None
    data: tp.Optional[NftChainData] = None
    is_mutable: tp.Optional[bool] = None
    primary_sale_happened: tp.Optional[bool] = None
    collection: tp.Optional[NftCollectionReference] = None


@dataclasses.dataclass
class NftUriMetadata:
    image: tp.Optional[str] = None
    description: tp.Optional[str] = None
    external_uri: tp.Optional[str] = None


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
