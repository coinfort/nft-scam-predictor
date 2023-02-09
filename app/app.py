import json

from analyzer.model import NftScamModel
from analyzer.analyzer import check_nft_token

model_file = '/opt/ml/model'
model = NftScamModel(model_file, device="cpu")


def lambda_handler(event, context):
    token_address = event['body']
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


