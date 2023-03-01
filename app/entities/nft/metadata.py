import dataclasses
import hashlib
import json
import typing as tp


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
    collection: tp.Optional[NftCollectionReference] = None


@dataclasses.dataclass
class NftUriMetadata:
    image: tp.Optional[str] = None
    description: tp.Optional[str] = None
    external_uri: tp.Optional[str] = None


def metadata_hash(
        metaplex_metadata: NftMetaplexMetadata,
        uri_metadata: NftUriMetadata
) -> str:
    """
    :return: MD5 hash of given metadata (32 symbols)
    """
    meta = {
        "metaplex_meta": dataclasses.asdict(metaplex_metadata),
        "uri_meta": dataclasses.asdict(uri_metadata)
    }
    packed = json.dumps(meta).encode("utf-8")
    return hashlib.md5(packed).digest().hex()


__all__ = [
    "NftCreator",
    "NftCollectionReference",
    "NftChainData",
    "NftMetaplexMetadata",
    "NftUriMetadata",
    "metadata_hash"
]
