import pycom
from network import WLAN
import time
import machine



def wificonnect():
    teller = 0
    pycom.heartbeat(False)
    wlan = WLAN(mode=WLAN.STA)

    while not wlan.isconnected():
        wlan.connect(ssid = "IoT", auth=(WLAN.WPA2, "KdGIoT92!"))
        teller = teller + 1
        time.sleep(5)
        pycom.rgbled(0xFF0000)
        print("no wifi connection")
        machine.idle()
        if teller==5:
            print("no wifi connection")
            break

    print("WiFi connected succesfully")
    print(wlan.ifconfig())
    pycom.rgbled(0x00FF00)
