from ..database import Base
from sqlalchemy import TIMESTAMP, Column, String, Integer
from sqlalchemy.sql import func


class PropertyType(Base):
    __tablename__ = "property_type"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    icon_image = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())
