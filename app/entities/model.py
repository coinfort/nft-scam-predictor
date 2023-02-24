from enum import Enum


class NftScamResponse(Enum):
    NOT_SCAM = "good"
    SCAM = "scam"
    DATA_FETCHING_ERROR = "data_fetching_error"
    WRONG_INPUT = "invalid_input"
