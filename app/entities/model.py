from enum import Enum


class NftScamResponse(Enum):
    NOT_SCAM = "good"
    SCAM = "scam"
    METADATA_FETCHING_ERROR = "metadata_fetching_error"
    WRONG_INPUT = "invalid_input"
