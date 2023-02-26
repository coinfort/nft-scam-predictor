import unittest

from analyzer.analyzer import check_nft_token
from analyzer.model import NftScamClassifierModel
from entities.model import NftScamResponse
from config import settings
from solana_utils.rpc import Endpoint, SolanaRpcClient


class TestNftScamPredictorIntegration(unittest.TestCase):
    NOT_SCAM_ADDRESS = "DDgpWvsHTiLG92jVQNLGGmk1BXTm4YLaukJGhEKUWFup"
    SCAM_ADDRESS = "5YQssEfjm4cz5UJtcoD2y7HkZVuCANi5YpXhtkZwSpDT"
    INVALID_ADDRESS = "5YQssEfjm4cz5UJtcoD2y7HkZVuCANi5YpXhtkZwSpD2"
    model = NftScamClassifierModel(
        model_path=settings.BERT_MODEL_SETTINGS.LOCATION,
        device=settings.BERT_MODEL_SETTINGS.DEVICE
    )

    client = SolanaRpcClient.from_endpoint(endpoint=Endpoint.Mainnet)

    def test_not_scam_input(self):
        self.assertEqual(NftScamResponse.NOT_SCAM, check_nft_token(self.model, self.client, self.NOT_SCAM_ADDRESS))

    def test_scam_input(self):
        self.assertEqual(NftScamResponse.SCAM, check_nft_token(self.model, self.client, self.SCAM_ADDRESS))

    def test_error_data(self):
        self.assertEqual(
            NftScamResponse.DATA_FETCHING_ERROR,
            check_nft_token(self.model, self.client, self.INVALID_ADDRESS)
        )


if __name__ == '__main__':
    unittest.main()
