import json

from analyzer.analyzer import check_nft_token
from analyzer.model import NftScamClassifierModel
from config import settings
from entities.model import NftScamResponse
from solana_utils.rpc import Endpoint, SolanaRpcClient
from validation.validation import (is_in_blacklist, is_in_whitelist,
                                   is_valid_token_length)

model = NftScamClassifierModel(
    model_path=settings.BERT_MODEL_SETTINGS.LOCATION,
    device=settings.BERT_MODEL_SETTINGS.DEVICE
)

client = SolanaRpcClient.from_endpoint(endpoint=Endpoint.Mainnet)


def lambda_handler(event, _):
    token_address = event["body"]
    result = NftScamResponse.WRONG_INPUT

    if is_in_blacklist(token_address):
        result = NftScamResponse.SCAM
    elif is_in_whitelist(token_address):
        result = NftScamResponse.GOOD
    elif is_valid_token_length(token_address):
        result = check_nft_token(model, client, token_address)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "result": result.value,
                "token_address": token_address,
            }
        )
    }
