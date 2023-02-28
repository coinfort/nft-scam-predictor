from services.nft import blacklist_nft_repository, whitelist_nft_repository


def is_valid_token_address(token_address) -> bool:
    return isinstance(token_address, str) and len(token_address) == 44


def is_in_blacklist(token_address: str) -> bool:
    return blacklist_nft_repository.exists(token_address)


def is_in_whitelist(token_address: str) -> bool:
    return whitelist_nft_repository.exists(token_address)
