#readSensor.py
import time
import bme680
import requests
from datetime import datetime

url='http://localhost:8000/readIn'

try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except (RuntimeError, IOError):
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)
while True:
    if sensor.get_sensor_data() and sensor.data.heat_stable:
        dt = datetime.now()
        dtstr = dt.strftime('%Y-%m-%d %H:%M:%S.%f')
        readings={
                    "dtm":dtstr,
                    "temp":sensor.data.temperature,
                    "hum":sensor.data.humidity,
                    "prsr":sensor.data.pressure,
                    "airqu":sensor.data.gas_resistance,
                    "smoi":0
                }
        requests.post(url,json=readings)
    time.sleep(1)
        