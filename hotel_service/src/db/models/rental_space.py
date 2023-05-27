from ..database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean, Float, Integer, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from sqlalchemy_utils import ChoiceType
from .property_type import PropertyType
from .room_type import RoomType
from .category import Category
from .currency import Currency
from .city import City

BOOKED_STATUS = 1
AVAILABLE_STATUS = 2

STATUS_TYPES = (
    (BOOKED_STATUS, "Booked"),
    (AVAILABLE_STATUS, "Available")
)


class RentalSpace(Base):
    __tablename__ = "rental_space"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    address = Column(String, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    price = Column(Float)
    # counts (beds, bathrooms)
    bedroom_count = Column(Integer)
    bathroom_count = Column(Integer)
    # FK ids
    property_type_id = Column(
        Integer,
        ForeignKey("property_type.id", ondelete='CASCADE'), 
        nullable=False)
    room_type_id = Column(
        Integer,
        ForeignKey('room_type.id', ondelete='CASCADE'), 
        nullable=False)
    city_id = Column(
        Integer,
        ForeignKey("city.id", ondelete='CASCADE'),
        nullable=False)
    category_id = Column(
        Integer,
        ForeignKey("category.id", ondelete='CASCADE'),
        nullable=False)
    currency_id = Column(
        Integer,
        ForeignKey("currency.id", ondelete='CASCADE'),
        nullable=False)
    # relationships
    property_type = relationship(PropertyType)
    room_type = relationship(RoomType)
    city = relationship(City)
    category = relationship(Category)
    currency = relationship(Currency)
    status = Column(ChoiceType(choices=STATUS_TYPES), default=AVAILABLE_STATUS) 
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())

