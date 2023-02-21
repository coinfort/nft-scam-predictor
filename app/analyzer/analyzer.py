import typing as tp

import requests
from solana.rpc.api import Client

from .model import NftScamModel
from .check_state import Response
from .metaplex import metadata
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def write_data_to_bd(token_address, metadata, model_predict):
    try:
        connection = psycopg2.connect(
            database="huy",
            user="postgres",
            password="itmo228itmo",
            host="test.cgzqg63k4sie.eu-central-1.rds.amazonaws.com",
            port="5432"
        )
        if metadata is None:
            metadata = ""
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        sql_create_database = 'INSERT INTO Metadata VALUES (\''  + token_address + '\' ,\'' + metadata + '\' ,\'' + str(model_predict) + '\');'
        cursor.execute(sql_create_database)
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()


def check_nft_token(model: NftScamModel, token_address: str) -> Response:
    description = nft_description(token_address)

    if description is None:  # Todo: Fix this behavior
        result = Response.WRONG_INPUT
    else:
        is_scam = model.check_scam([description])[0]
        if is_scam:
            result = Response.SCAM
        else:
            result = Response.NOT_SCAM

    write_data_to_bd(token_address, description, result)
    return result


def nft_metadata(token_address: str) -> tp.Dict[str, tp.Any]:
    mainnet_api_url = "http://api.mainnet-beta.solana.com"
    client = Client(mainnet_api_url)
    data = metadata.get_metadata(client, token_address)["data"]
    return data


def nft_description(token_address: str) -> tp.Optional[str]:
    try:
        data = nft_metadata(token_address)
        data = requests.get(data["uri"]).json()
        return data["description"]
    except Exception as _:
        return None


__all__ = ["check_nft_token"]
