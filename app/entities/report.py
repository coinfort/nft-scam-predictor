import json
import typing as tp
from enum import Enum


class NftReportResponseType(Enum):
    REPORT_ACCEPTED = "REPORT_ACCEPTED"
    ADDED_TO_BLACKLIST = "ADDED_TO_BLACKLIST"
    ADDED_TO_WHITELIST = "ADDED_TO_WHITELIST"
    INVALID_INPUT = "INVALID_INPUT"

    def to_response(self, token_address: str) -> tp.Dict[str, str]:
        body = dict(
            result=self.value,
            token_address=token_address
        )

        if self == NftReportResponseType.INVALID_INPUT:
            status_code = 400
        else:
            status_code = 200

        return dict(
            statusCode=status_code,
            body=json.dumps(body)
        )
