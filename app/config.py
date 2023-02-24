import os

import dotenv
from pydantic import BaseSettings


class BertModelSettings(BaseSettings):
    LOCATION = "/opt/ml/model"
    DEVICE = "cpu"


class Settings(BaseSettings):
    CHAINSTACK_NODE_URL: str

    DATABASE_PORT: str
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str

    BERT_MODEL_SETTINGS: BertModelSettings = BertModelSettings()

    class Config:
        env_file = ".env"


dotenv.load_dotenv(Settings.Config.env_file)

settings = Settings(
    CHAINSTACK_NODE_URL=os.getenv("CHAINSTACK_NODE_URL"),
    DATABASE_PORT=os.getenv("POSTGRES_PORT"),
    POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD"),
    POSTGRES_USER=os.getenv("POSTGRES_USERNAME"),
    POSTGRES_HOST=os.getenv("POSTGRES_HOST"),
    POSTGRES_DB=os.getenv("POSTGRES_DATABASE")
)
