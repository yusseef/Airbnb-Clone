from db.database_setup import Base
from validators.email_validator import Email
from validators.password_validator import Password
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, Boolean, Text, String, DateTime, Date, Sequence, Enum, text
from sqlalchemy_utils import ChoiceType

class User(Base):
    __tablename__ = 'user'

    USER_TYPES = [ 
        ('ADMIN', 'admin'),
        ('OWNER', 'owner'),
        ('CUSTOMER', 'customer'),
        ]

    id = Column(Integer, Sequence('user_id_seq'), primary_key = True, autoincrement = True)
    first_name = Column(String(50), nullable = False)
    last_name = Column(String(50), nullable = False)
    email = Column(Email, unique=True, nullable = False)
    password = Column(Password, nullable = False)
    user_type = Column(ChoiceType(choices=USER_TYPES), default='CUSTOMER')
    date_of_birth = Column(Date)
    facebook_id = Column(String(100))
    twitter_id = Column(String(100))
    about = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=text('CURRENT_TIMESTAMP') )

    def __repr__(self):
        return f"{self.full_name} / f{self.email}"
