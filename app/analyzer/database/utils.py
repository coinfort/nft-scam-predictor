from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
import datetime
from dict_hash import sha256

DATABASE = {
    'drivername': 'postgresql',
    'host': 'all.cgzqg63k4sie.eu-central-1.rds.amazonaws.com',
    'port': '5432',
    'username': 'postgres',
    'password': 'ycbuDVt1FUbO4hVz9jNU',
    'database': 'Metadata',
    'query': {}
}

DeclarativeBase = declarative_base()


class Metadata(DeclarativeBase):
    __tablename__ = 'Metadata_New'

    TokenID = Column(String, primary_key=True)
    Hash = Column(String, primary_key=True)
    Title = Column(String)
    Description = Column(String)
    IsMutable = Column(Boolean)
    TokenType = Column(String)
    CollectionID = Column(String)
    IsCollectionVerified = Column(Boolean)
    TokenUri = Column(String)
    Image = Column(String)
    Symbol = Column(String)
    Mint = Column(String)
    UpdateAuthority = Column(String)
    ExternalUri = Column(String)
    TimeOfAppeal = Column(DateTime)

    def __repr__(self):
        return "Metadata(token_adddress = {}, hash = {})".format(self.TokenID, self.Hash)


def write_metadata_to_bd(token_address, metadata):
    engine = create_engine(URL(**DATABASE))
    Session = sessionmaker(bind=engine)
    session = Session()
    is_exits = session.query(Metadata.TokenID, Metadata.Hash) \
                   .filter_by(TokenID=token_address, Hash=str(sha256(metadata))).first() is not None
    if is_exits:
        session.query(Metadata) \
            .filter_by(TokenID=token_address, Hash=str(sha256(metadata))).first() \
            .TimeOfAppeal = datetime.datetime.utcnow()
    else:
        session.add(Metadata(
            TokenID=token_address,
            Hash=str(sha256(metadata)),
            Title=metadata['Title'],
            Description=metadata['Description'],
            IsMutable=metadata['IsMutable'] == 1,
            TokenType=metadata['TokenType'],
            CollectionID=metadata['CollectionID'],
            IsCollectionVerified=metadata['IsCollectionVerified'] == 1,
            TokenUri=metadata['TokenUri'],
            Image=metadata['Image'],
            Symbol=metadata['Symbol'],
            Mint=metadata['Mint'],
            UpdateAuthority=metadata['UpdateAuthority'],
            ExternalUri=metadata['ExternalUri'],
            TimeOfAppeal=datetime.datetime.utcnow()
        ))
    session.commit()


def create_bd():
    engine = create_engine(URL(**DATABASE))
    DeclarativeBase.metadata.create_all(engine)


def show_data():
    engine = create_engine(URL(**DATABASE))
    Session = sessionmaker(bind=engine)
    session = Session()
    for m in session.query(Metadata):
        print(m)
