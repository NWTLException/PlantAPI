from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
#imports for DHT22
import time
import board
import adafruit_dht

# pip3 install adafruit-circuitpython-dht
# pip install jinja2 
# pip3 install fastapi
# pip install "uvicorn[standard]"






app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="html")
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)


user = ["Kilian","Gabriel","Simon"]

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

users=[]

gehtmir={
    "id":0,
    "name":"Gehtmir",
    "mail":"gehtmir.sugma@caom.com"
}

oleg={
    "id":1,
    "name":"Oleg",
    "mail":"oleg.sugma@gmail.com"
}

users.insert(0,gehtmir)
users.insert(1,oleg)

@app.get("/users")
async def getAllUsers():
    return users




@app.get("/temphum")
async def getTempAndHum():
    while True:
        try:
          # Print the values to the serial port
            temperature_c = dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dhtDevice.humidity
            print(
                "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                    temperature_f, temperature_c, humidity
                )
            )
            response = {"temp":temperature_c, "humidity":humidity}
            return response
        except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
        except KeyboardInterrupt:
            dhtDevice.exit()
            print('exiting script')
        time.sleep(2.0)

    




