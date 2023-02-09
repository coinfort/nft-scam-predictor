from enum import Enum


class Response(Enum):
    NOT_SCAM = 0
    SCAM = 1
    WRONG_INPUT = 2
