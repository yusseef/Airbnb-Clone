import configparser
from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base, sessionmaker

config = configparser.ConfigParser()
print(config.read('/home/yussef/Airbnb/Airbnb-Clone/User microservice/src/db/env.ini'))


db_username = config['DATABASE']['Username']
db_password = config['DATABASE']['Password']
db_host = config['DATABASE']['Host']
db_name = config['DATABASE']['Name']

print(db_username)
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
