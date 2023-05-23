from ..database import Base
from sqlalchemy import TIMESTAMP, Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from .country import Country


class City(Base):
    __tablename__ = "city"

    id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    country_id = Column(Integer, ForeignKey('country.id', ondelete='CASCADE'), nullable=False)
    country = relationship(Country, backref='cities')
