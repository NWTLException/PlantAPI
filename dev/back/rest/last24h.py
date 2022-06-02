from datetime import datetime, timedelta
import csv

class reading: 
    def __init__(self,dtm,temp,hum,prsr,voc,smoi): 
        self.dtm = dtm 
        self.temp = temp
        self.hum = hum
        self.prsr = prsr
        self.voc = voc
        self.smoi = smoi 

def get_last_24h():
    file = open("log.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    filtered = []
    lastDayDateTime = datetime.now() - timedelta(days=1)
    for row in csvreader:
        if row:
            datem=datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')
            if datem>=lastDayDateTime and datem.minute==0 and datem.second==0:
                filtered.append(reading(row[0],row[1],row[2],row[3],row[4],row[5]))
    file.close()
    last24=[]
    for e in filtered:
        dc={'dtm':e.dtm,'temp':e.temp,'hum':e.hum,'prsr':e.prsr,'voc':e.voc,'smoi':e.smoi}
        last24.append(dc)
    return last24

li=get_last_24h()
print(li)
