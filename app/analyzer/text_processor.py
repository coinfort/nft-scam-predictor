import re

URL_REGEX = re.compile(
    r"(https?:\/\/)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
)
NUMBER_REGEX = re.compile(r'\d+(?:,\d*)?')
TOKENS_REGEX = re.compile(r"\$\w+")
COINS = ["ETH", "SOL", "USDT", "USDC", "DAI", "BTC"]


def replace_url(text):
    return URL_REGEX.sub("[URL]", text)


def replace_tokens(text):
    return TOKENS_REGEX.sub("[TOKEN_NAME]", text)


def replace_numbers(text):
    return NUMBER_REGEX.sub("[NUM]", text)


def preprocess_text_pipe(text):
    words = replace_url(text)
    words = replace_tokens(words)
    words = replace_numbers(words)

    words = " ".join(words)
    words = [word if not word == "URL" else "[URL]" for word in words]
    words = [word if not word == "NUM" else "[NUM]" for word in words]
    words = [word if not word == "TOKEN_NAME" else "[TOKEN_NAME]" for word in words]
    words = [word.strip() for word in words]
    return " ".join(words).strip()


__all__ = [
    "preprocess_text_pipe"
]
