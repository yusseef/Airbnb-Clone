from fastapi import FastAPI
from .db.database import engine
from .db.database import Base

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def hello_world():
    return "Hello World from hotel service"
