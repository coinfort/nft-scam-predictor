from enum import Enum


class NftScamResponse(Enum):
    NOT_SCAM = "good"
    SCAM = "scam"
    WRONG_INPUT = "invalid input"
