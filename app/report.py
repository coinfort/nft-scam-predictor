from entities.report import NftReportResponseType
from report.utils import commit_report
from validation.validation import (is_in_blacklist, is_in_whitelist,
                                   is_valid_token_address)


def lambda_handler(event, _):
    token_address = event["body"]
    result = NftReportResponseType.INVALID_INPUT

    if is_valid_token_address(token_address):
        if is_in_blacklist(token_address):
            result = NftReportResponseType.ADDED_TO_BLACKLIST
        elif is_in_whitelist(token_address):
            result = NftReportResponseType.ADDED_TO_WHITELIST
        else:
            commit_report(token_address)
            result = NftReportResponseType.REPORT_ACCEPTED

    return result.to_response(token_address)
