import schedule
import time
import requests

urlPost='http://localhost:8000/readings/adToLast24'
urlGet='http://localhost:8000/readings/all'


def job():
    resp = requests.get(urlGet)
    data = resp.json()
    requests.post(urlPost,json=data)

schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)