from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def hello_world():
    return "Hello World from user service"
