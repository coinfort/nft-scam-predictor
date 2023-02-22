import json

from analyzer.analyzer import NFTScamResponse, check_nft_token
from analyzer.model import NftScamModel
from sol.rpc import Endpoint, SolanaRpcClient

model_file = "/opt/ml/model"
model = NftScamModel(model_file, device="cpu")
client = SolanaRpcClient.from_endpoint(endpoint=Endpoint.Mainnet)


def is_valid_token_length(token_address):
    return len(token_address) == 44


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
