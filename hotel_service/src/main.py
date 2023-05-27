from fastapi import FastAPI
from .db.database import Base # noqa

app = FastAPI()


@app.get("/")
def hello_world():
    return "Hello World from hotel service"
