from enum import Enum


class NftScamResponse(Enum):
    GOOD = "GOOD"
    SCAM = "SCAM"
    DATA_FETCHING_ERROR = "DATA_FETCHING_ERROR"
    WRONG_INPUT = "INVALID_INPUT"
