import json
import typing as tp
from enum import Enum


class NftScamResponseType(Enum):
    CHECKS_PASSED = "CHECKS_PASSED"
    SUSPECTED_MALICIOUS = "SUSPECTED_MALICIOUS"
    DATA_FETCHING_ERROR = "DATA_FETCHING_ERROR"
    WRONG_INPUT = "INVALID_INPUT"

    def to_response(self, token_address: str) -> tp.Dict[str, str]:
        body = dict(
            result=self.value,
            token_address=token_address
        )

        if self == NftScamResponseType.SUSPECTED_MALICIOUS:
            body = body | dict(malicious_type="PHISHING")

        if self == NftScamResponseType.WRONG_INPUT or self == NftScamResponseType.DATA_FETCHING_ERROR:
            status_code = 400
        else:
            status_code = 200

        return dict(
            statusCode=status_code,
            body=json.dumps(body)
        )
