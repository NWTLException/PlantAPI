#main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from csv import DictWriter
from last24h import get_last_24h

## sudo uvicorn main:app --host 0.0.0.0

class Readings(BaseModel):
    dtm: str
    temp: float
    hum: float
    prsr: float
    airqu: float
    smoi: float

field_names = ['dtm','temp', 'hum', 'prsr', 'voc','smoi']

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/readIn")
async def recieveReadings(readings:Readings):
    global data
    data=readings
    dict={ 'dtm':data.dtm,
           'temp':data.temp,
           'hum':data.hum,
           'prsr':data.prsr,
           'voc':data.airqu,
           'smoi':0}
    with open('log.csv', 'a', encoding='UTF8', newline='') as f:
        dictwriter_object = DictWriter(f, fieldnames=field_names)
        dictwriter_object.writerow(dict)
        f.close()
    return data

@app.get("/readings/all")
async def getAllReadings():
    return data

@app.get("/readings/last24")
async def getAllReadings():
    li=get_last_24h()
    return li