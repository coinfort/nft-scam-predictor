import typing as tp

from db.connection import get_db

from .table import WhitelistNft


class WhitelistNftRepository:
    def __init__(self, db=get_db()):
        self.db = db

    def add_token_address(self, token_address: str):
        self.db.add(WhitelistNft(
           token_id=token_address
        ))
        self.db.commit()

    def find(self, token_id: str) -> tp.Optional[WhitelistNft]:
        return self.db.query(WhitelistNft.token_id).filter_by(token_id=token_id).first()

    def exists(self, token_id: str) -> bool:
        return self.find(token_id) is not None
