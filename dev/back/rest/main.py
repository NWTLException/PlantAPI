#main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from csv import DictWriter
from datetime import datetime

class Readings(BaseModel):
    dtm: datetime
    temp: float
    hum: float
    prsr: float
    airqu: float

class reading: 
    def __init__(self,datetime,temp,hum,prsr,voc,smoi): 
        self.datetime = datetime 
        self.temp = temp
        self.hum = hum
        self.prsr = prsr
        self.voc = voc
        self.smoi = smoi 

last24=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

field_names = ['timestamp','temp', 'hum', 'prsr', 'voc','smoi']

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
    dict={ 'datetime':data.dtm,
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
    return last24