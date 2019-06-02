import mraa
import time
import requests

ENDPOINT = "https://farm-pfcun.transposit.io/api/v1/execute-http/dumpdata"

prevData = {"lon": 0,
            "la": 0}

data = {"lon": 2.0,
        "lat": 3.0}

button = mraa.Gpio(33)
power = mraa.Gpio(34)
prevReading = 0

button.dir(mraa.DIR_IN)
power.dir(mraa.DIR_OUT)

power.write(1)

while True:
    reading = button.read()
    print(reading)

    if (data['lon'] != prevData['lon'] or data['lat'] != prevData['lat']) and prevReading != reading:

        r = requests.post(url = ENDPOINT, data = data)
        prevData = data
        print(r)

    prevReading = reading
