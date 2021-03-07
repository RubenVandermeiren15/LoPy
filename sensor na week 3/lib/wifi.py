from network import WLAN
import machine
import pycom
import time

wlan = WLAN(mode=WLAN.STA)
pycom.heartbeat(False)
wlan.connect(ssid='VDM', auth=(WLAN.WPA2, 'GalenGold15'))

while not wlan.isconnected():
    time.sleep(2)
    pycom.rgbled(0xFF0000)
    machine.idle()
    print("WiFi connected succesfully")
    print(wlan.ifconfig())
    pycom.rgbled(0x00FF00)
