from database_setup import engine, Base, Session
from models.user_model import User

Base.metadata.create_all(bind = engine)