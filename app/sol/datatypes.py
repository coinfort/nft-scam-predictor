import dataclasses
import typing as tp


@dataclasses.dataclass
class Creator:
    address: str
    verified: bool
    share: int


@dataclasses.dataclass
class Collection:
    verified: bool
    key: str


@dataclasses.dataclass
class ChainData:
    name: str
    symbol: str
    uri: str
    seller_fee_basis_points: int
    creators: tp.List[Creator]


@dataclasses.dataclass
class MetaplexMetadata:
    update_authority: str
    mint: str
    data: ChainData
    is_mutable: bool
    primary_sale_happened: bool
    collection: tp.Optional[Collection]


@dataclasses.dataclass
class UriMetadata:
    image: tp.Optional[str]
    description: tp.Optional[str]
    external_url: tp.Optional[str]


__all__ = [
    "Creator",
    "Collection",
    "ChainData",
    "MetaplexMetadata",
    "UriMetadata"
]
