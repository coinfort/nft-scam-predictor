from analyzer.analyzer import check_nft_token
from analyzer.model import NftScamClassifierModel
from config import settings
from entities.model import NftScamResponseType
from solana_utils.rpc import Endpoint, SolanaRpcClient
from validation.validation import (is_in_blacklist, is_in_whitelist,
                                   is_valid_token_address)

model = NftScamClassifierModel(
    model_path=settings.BERT_MODEL_SETTINGS.LOCATION,
    device=settings.BERT_MODEL_SETTINGS.DEVICE
)

client = SolanaRpcClient.from_endpoint(endpoint=Endpoint.Mainnet)


def lambda_handler(event, _):
    token_address = event["body"]
    result = NftScamResponseType.WRONG_INPUT

    if is_valid_token_address(token_address):
        if is_in_blacklist(token_address):
            result = NftScamResponseType.SUSPECTED_MALICIOUS
        elif is_in_whitelist(token_address):
            result = NftScamResponseType.CHECKS_PASSED
        else:
            result = check_nft_token(model, client, token_address)

    return result.to_response(token_address)
