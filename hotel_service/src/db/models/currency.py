from ..database import Base
from sqlalchemy import Column, String, Integer


class Currency(Base):
    __tablename__ = "currency"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    icon_image = Column(String, nullable=True)
