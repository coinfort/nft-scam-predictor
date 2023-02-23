from db.connection import Base, engine
from sqlalchemy import Boolean, Column, DateTime, Integer, String, text


class NftMetadata(Base):
    __tablename__ = "nft_metadata"

    token_id = Column(String(length=44), primary_key=True, nullable=False)
    hash = Column(String, primary_key=True, nullable=False)
    update_authority = Column(String(length=44), nullable=False)
    mint = Column(String(length=44), nullable=False)
    title = Column(String, nullable=True)
    description = Column(String, nullable=True)
    is_mutable = Column(Boolean, nullable=True)
    token_type = Column(String, nullable=True)
    collection_id = Column(String, nullable=True)
    is_collection_verified = Column(Boolean, nullable=True)
    seller_fee_basis_points = Column(Integer, nullable=True)
    uri = Column(String, nullable=True)
    image = Column(String, nullable=True)
    symbol = Column(String, nullable=True)
    external_uri = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=text("now()"), nullable=False)
    updated_at = Column(DateTime, server_default=text("now()"), nullable=False)
    predict_result = Column(String, nullable=False)

    def __repr__(self):
        return f"{self.__class__.__name__}(token_id={self.token_id}, hash={self.hash})"


Base.metadata.create_all(engine)
