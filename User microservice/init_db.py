from database_setup import engine, Base, Session
from models import User

Base.metadata.create_all(bind = engine)