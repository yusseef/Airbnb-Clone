from fastapi import FastAPI
from models.user_model import User
app = FastAPI()


@app.get("/")
def hello_world():
    return "Hello World from user service"
