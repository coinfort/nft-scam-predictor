import unittest
import sys
from common import get_predict


class TestNftScamPredictorIntegration(unittest.TestCase):
    VALID_INPUT = "DDgpWvsHTiLG92jVQNLGGmk1BXTm4YLaukJGhEKUWFup"
    INVALID_INPUT = "DDgpWvsHTiLG92jVQNLGGmk1BXTm4YLaukJGhEKUWFu8"
    SHORT_INPUT = "123"
    TEST_URL = "url"  # put here url for local testing
    TEST_API_KEY = "api_key"  # put here your api key for local testing

    # def test_valid_input(self):
    #     response = get_predict(url=self.TEST_URL,
    #                            api_key=self.TEST_API_KEY,
    #                            body=self.VALID_INPUT)
    #     self.assertEqual(response, {
    #         "result": "CHECKS_PASSED",
    #         "token_address": self.VALID_INPUT
    #     })
    #
    # def test_double_valid_input(self):
    #     self.test_valid_input()
    #     self.test_valid_input()
    #
    # def test_short_input(self):
    #     response = get_predict(url=self.TEST_URL,
    #                            api_key=self.TEST_API_KEY,
    #                            body=self.SHORT_INPUT)
    #     self.assertEqual(response, {
    #         "result": "INVALID_INPUT",
    #         "token_address": self.SHORT_INPUT
    #     })
    #
    # def test_invalid_input(self):
    #     response = get_predict(url=self.TEST_URL,
    #                            api_key=self.TEST_API_KEY,
    #                            body=self.INVALID_INPUT)
    #     self.assertEqual(response, {
    #         "result": "DATA_FETCHING_ERROR",
    #         "token_address": self.INVALID_INPUT
    #     })
    #
    # def test_empty_input(self):
    #     response = get_predict(url=self.TEST_URL,
    #                            api_key=self.TEST_API_KEY,
    #                            body=None)
    #     self.assertEqual(response, {
    #         "result": "INVALID_INPUT",
    #         "token_address": None
    #     })


if __name__ == '__main__':
    TestNftScamPredictorIntegration.TEST_API_KEY = sys.argv.pop()
    TestNftScamPredictorIntegration.TEST_URL = sys.argv.pop()
    unittest.main()
