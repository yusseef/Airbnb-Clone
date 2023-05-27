from ..database import Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from .country import Country


class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    country_id = Column(Integer, ForeignKey('country.id', ondelete='CASCADE'), nullable=False)
    country = relationship(Country, backref='cities')
