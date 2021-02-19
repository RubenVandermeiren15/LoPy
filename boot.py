from network import WLAN
import machine
import pycom
import time
wlan = WLAN(mode=WLAN.STA)

wlan.connect(ssid='wifi', auth=(WLAN.WPA2, 'wachtwoord'))
while not wlan.isconnected():
    pycom.heartbeat(False)
    time.sleep(2)
    pycom.rgbled(0xFF0000)
print("WiFi connected succesfully")
pycom.heartbeat(False)
pycom.rgbled(0x00FF00)
print(wlan.ifconfig())
