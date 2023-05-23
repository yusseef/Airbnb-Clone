from ..database import Base
from sqlalchemy import TIMESTAMP, Column, String
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL

class Country(Base):
    __tablename__ = "country"

    id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)