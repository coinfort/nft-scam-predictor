from db.connection import Base, engine
from sqlalchemy import Column, String


class ReportNft(Base):
    __tablename__ = "report_nfts"

    token_id = Column(String(length=44), primary_key=True, nullable=False)

    def __repr__(self):
        return f"{self.__class__.__name__}(token_id={self.token_id})"


Base.metadata.create_all(engine)