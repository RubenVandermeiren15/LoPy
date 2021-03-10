import wifi
import lora
import sensor
import time
import urequest as requests


wifi.wificonnect()

aio_key = "aio_PRIx84zB0k0shUDCfGhDvjZhhEfW"
username = "rubetsky"
feed_name = "sensor"
url = 'https://io.adafruit.com/api/v2/' + username + '/feeds/' + feed_name + '/data'
headers = {'X-AIO-Key': aio_key, 'Content-Type': 'application/json'}
#lora.getlora()

while True:
    #lora.senddata
    afstand = sensor.readsensor()
    body = {'value': afstand}
    try:
        r = requests.post(url, json=body, headers=headers)
        print(r.text)
        r.close()
    except Exception as e:
        print(e)
    time.sleep(3)
