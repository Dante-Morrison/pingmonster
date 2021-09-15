import os
import time
import requests
import datetime

url = 'https://texasrighttolife.com/'
tick = 0

def logWrite():
    with open('ping_log.txt', 'a') as f:
        f.write(str(r.status_code) + '\n')
        f.write(str(r.elapsed.total_seconds()) + '\n')
        f.write(str(datetime.datetime.now()) + '\n')
        #WARNING! these next two lines get the contents of the website. this is a lot of data.
        #f.write(str(r.headers) + '\n')
        #f.write(str(r.content) + '\n')
        f.write('\n')

while True:
    tick = tick + 1
    try:
        r = requests.get(url)
        #warning, this next line will generate a crap ton of data, only uncomment if you're prepared to deal with it
        #logWrite()
        print("ping attempt", tick, "site ping succsessful with server code", str(r.status_code))

    except:
        print("Error")

    #time.sleep(.25)