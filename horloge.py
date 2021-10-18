import time
import datetime

now = datetime.datetime.now()
heurs = int(now.strftime("%H"))
min = int(now.strftime("%M"))
sec = int(now.strftime("%S"))

while sec < 60:
    print(heurs,":",min,":",sec)
    time.sleep(1.0)
    sec += 1
    if sec == 60:
        min += 1
        sec -= 60
        if min == 60:
            heurs += 1
            min -= 60
