from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    name: str

@app.get("/ooi")
def helloworld():
    return "Hello I am learning FastAPI with noor  inceptez"

@app.post("/hi")
def helloworld_post():
    return "Hello I am learning FastAPI"

@app.get("/person/{person}")
def great_user_get(person: str):
    return {"Hey Hi Welcome ": person}

@app.post("/person/")
def great_user_post(data: InputData):
    return {"Hey Hi Welcome ": data.name}
