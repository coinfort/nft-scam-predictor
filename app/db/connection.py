from config import settings
from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = URL(
    drivername="postgresql",
    host=settings.POSTGRES_HOST,
    port=settings.DATABASE_PORT,
    username=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    database=settings.POSTGRES_DB,
    query={}
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    return SessionMaker()
