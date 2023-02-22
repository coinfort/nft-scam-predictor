import json

from analyzer.analyzer import NFTScamResponse, check_nft_token
from analyzer.model import NftScamModel
from solana_utils.rpc import Endpoint, SolanaRpcClient
from validation.validation import is_valid_token_length

model_file = "/opt/ml/model"
model = NftScamModel(model_file, device="cpu")
client = SolanaRpcClient.from_endpoint(endpoint=Endpoint.Mainnet)


def lambda_handler(event, _):
    token_address = event["body"]
    result = NFTScamResponse.WRONG_INPUT

    if is_valid_token_length(token_address):
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
