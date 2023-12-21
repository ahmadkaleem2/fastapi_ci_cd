from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World1"}

@app.get("/feature")
def feature():
    return {"feature": "World1"}