import requests


def get_predict(*, url: str, api_key: str, body: str) -> dict:
    headers = {'x-api-key': api_key}
    response = requests.post(
        url,
        headers=headers,
        data=body
    )
    return response.json()


__all__ = [
    "get_predict"
]
