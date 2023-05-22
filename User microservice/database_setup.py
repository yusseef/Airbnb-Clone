import configparser
from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base, sessionmaker

config = configparser.ConfigParser()
config.read('config.ini')

db_username = config['DATABASE']['Username']
db_password = config['DATABASE']['Password']
db_host = config['DATABASE']['Host']
db_name = config['DATABASE']['Name']

db_username = config['DATABASE']['Username']
db_password = config['DATABASE']['Password']
db_host = config['DATABASE']['Host']
db_name = config['DATABASE']['Name']

print(db_username)
print(db_password)
print(db_host)
print(db_name)

# create the engine
engine = None
try:
    engine_str = f'postgresql://{db_username}:{db_password}@{db_host}/{db_name}'
    engine = create_engine(engine_str, echo=True)

except Exception as e:
    print(f"Error creating engine: {e}")

if engine is not None:
    # create the base class
    Base = declarative_base()

    # create the session factory
    try:
        Session = sessionmaker(bind=engine)
        
    except Exception as e:
        print(f"Error in session maker: {e}")