import dataclasses
import datetime

from entities.model import NftScamResponseType
from entities.nft.metadata import NftMetaplexMetadata, NftUriMetadata


@dataclasses.dataclass
class NftMetadataTokenHashDto:
    token_id: str
    hash: str


@dataclasses.dataclass
class UpdateNftMetadataTimestampDto(NftMetadataTokenHashDto):
    time: datetime.datetime


@dataclasses.dataclass
class CreateNftMetadataDto(NftMetadataTokenHashDto):
    metaplex_metadata: NftMetaplexMetadata
    uri_metadata: NftUriMetadata
    result: NftScamResponseType


__all__ = [
    "NftMetadataTokenHashDto",
    "UpdateNftMetadataTimestampDto",
    "CreateNftMetadataDto"
]
