from ..database import Base
from sqlalchemy import Column, String
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL

class Currency(Base):
    __tablename__ = "currency"

    id = Column(GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL)
    name = Column(String, nullable=False)
    icon_image = Column(String, nullable=True)
