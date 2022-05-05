#main.py
from fastapi import FastAPI
from pydantic import BaseModel

class Readings(BaseModel):
    temp: float
    hum: float
    prsr: float
    airqu: float

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/readIn")
async def recieveReadings(readings:Readings):
    global data
    data=readings
    return data

@app.get("/readings/all")
async def getAllReadings():
    return data