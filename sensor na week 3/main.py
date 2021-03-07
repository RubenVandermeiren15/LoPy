import wifi
import lora
import sensor
import time
import urequests as requests


aio_key = "aio_wUMm44oYLxvvvFaCpN96Hz5mFfi5"
username = "rubetsky"
feed_name = "sensor"

wifi.wificonnect('VDM', 'GalenGold15')

#lora.getlora()

while True:
    #lora.senddata

    afstand = readsensor()

    url = 'https://io.adafruit.com/api/v2/' + username + '/feeds/' + feed_name
    + '/data'
    body = {'value': afstand}
    headers = {'X-AIO-Key': aio_key, 'Content-Type': 'application/json'}
    try:
        r = requests.post(url, json=body, headers=headers)
        print(r.text)
        r.close()

    except Exception as e:
        print(e)
    time.sleep(10)
