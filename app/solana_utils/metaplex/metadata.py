import struct

import base58
from entities.nft_metadata import *
from solana.publickey import PublicKey
from solana_utils.programs import *


def get_metadata_account(mint_key: PublicKey) -> PublicKey:
    seeds = [b"metadata", bytes(METADATA_PROGRAM_ID), bytes(mint_key)]
    pda, _ = PublicKey.find_program_address(seeds, METADATA_PROGRAM_ID)
    return pda


def unpack_struct(data: bytes, start: int, length: int) -> bytes:
    data_slice = data[start: start + length]
    unpacked = struct.unpack("<" + "B" * length, data_slice)
    return bytes(unpacked)


def parse_bytes(data: bytes, start: int, length: int) -> bytes:
    decoded = unpack_struct(data, start, length)
    return base58.b58encode(decoded)


def parse_account(data: bytes, start: int) -> bytes:
    return parse_bytes(data, start=start, length=32)


def parse_metadata_bytes(data: bytes):
    assert (data[0] == 4)
    i = 1
    source_account = parse_account(data, i)
    i += 32
    mint_account = parse_account(data, i)
    i += 32
    name_len = struct.unpack("<I", data[i:i + 4])[0]
    i += 4
    name = unpack_struct(data, i, name_len)
    i += name_len
    symbol_len = struct.unpack("<I", data[i:i + 4])[0]
    i += 4
    symbol = unpack_struct(data, i, symbol_len)
    i += symbol_len
    uri_len = struct.unpack("<I", data[i:i + 4])[0]
    i += 4
    uri = unpack_struct(data, i, uri_len)
    i += uri_len
    fee = struct.unpack("<h", data[i:i + 2])[0]
    i += 2
    has_creator = data[i]
    i += 1
    creator_accounts = []
    verified = []
    share = []
    if has_creator:
        creator_len = struct.unpack("<I", data[i:i + 4])[0]
        i += 4
        for _ in range(creator_len):
            creator = parse_account(data, i)
            creator_accounts.append(creator)
            i += 32
            verified.append(data[i])
            i += 1
            share.append(data[i])
            i += 1
    primary_sale_happened = bool(data[i])
    i += 1
    is_mutable = bool(data[i])

    creators = [
        NftCreator(address=c.hex(), verified=v, share=s) for c, v, s in zip(creator_accounts, verified, share)
    ]

    internal_data = NftChainData(
        title=name.decode("utf-8").strip("\x00"),
        symbol=symbol.decode("utf-8").strip("\x00"),
        uri=uri.decode("utf-8").strip("\x00"),
        seller_fee_basis_points=fee,
        creators=creators
    )

    metadata = NftMetaplexMetadata(
        update_authority=source_account.decode("utf-8"),
        mint=mint_account.decode("utf-8"),
        data=internal_data,
        is_mutable=is_mutable,
        primary_sale_happened=primary_sale_happened,
        collection=None
    )

    return metadata


__all__ = [
    "get_metadata_account",
    "parse_metadata_bytes"
]
