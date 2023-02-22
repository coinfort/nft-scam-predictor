import json

from analyzer.model import NftScamModel
from analyzer.analyzer import check_nft_token
from analyzer.check_state import Response

model_file = '/opt/ml/model'
model = NftScamModel(model_file, device="cpu")


def is_valid_token_length(token_address):
    return len(token_address) == 44


def lambda_handler(event, context):
    token_address = event['body']
    result = Response.WRONG_INPUT
    if is_valid_token_length(token_address):
        result = check_nft_token(model, token_address)

    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                "predicted_label": result.value,
                "token_address": token_address,
            }
        )
    }
