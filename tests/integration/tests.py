import unittest
import sys
from common import get_predict


class TestNftScamPredictorIntegration(unittest.TestCase):
    VALID_INPUT = "DDgpWvsHTiLG92jVQNLGGmk1BXTm4YLaukJGhEKUWFup" # ABC #2851
    INVALID_INPUT = "123"
    TEST_URL = "url"
    TEST_API_KEY = "api_key"

    def test_valid_input(self):
        response = get_predict(url=self.TEST_URL,
                               api_key=self.TEST_API_KEY,
                               body=self.VALID_INPUT)
        self.assertEqual(response, {
            "result": "good",
            "token_address": self.VALID_INPUT
        })

    def test_invalid_input(self):
        response = get_predict(url=self.TEST_URL,
                               api_key=self.TEST_API_KEY,
                               body=self.INVALID_INPUT)
        self.assertEqual(response, {
            "result": "invalid_input",
            "token_address": self.INVALID_INPUT
        })


if __name__ == '__main__':
    TestNftScamPredictorIntegration.TEST_API_KEY = sys.argv.pop()
    TestNftScamPredictorIntegration.TEST_URL = sys.argv.pop()
    unittest.main()
