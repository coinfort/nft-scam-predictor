import typing as tp

from db.connection import get_db

from .table import ReportNft


class ReportNftRepository:
    def __init__(self, db=get_db()):
        self.db = db

    def add_token_address(self, token_address: str):
        self.db.add(ReportNft(
           token_id=token_address
        ))
        self.db.commit()

    def find(self, token_id: str) -> tp.Optional[ReportNft]:
        return self.db.query(ReportNft.token_id).filter_by(token_id=token_id).first()

    def exists(self, token_id: str) -> bool:
        return self.find(token_id) is not None
