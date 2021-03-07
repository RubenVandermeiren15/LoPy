from network import LoRa
import socket
import time
import ubinascii
import sensor
import ustruct


lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

app_eui = ubinascii.unhexlify('70B3D57ED003E4C8')
app_key = ubinascii.unhexlify('C21BE17CE702108BA7D870822739D89C')
dev_eui = ubinascii.unhexlify('70B3D57ED003E4C8')

def joinlora():
    lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)
    packet = ustruct.pack('f',3.33)

    while not lora.has_joined():
        time.sleep(2.5)
        print('Not yet joined')

    print('Joined')

def senddata():
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    s.setblocking(True)
    meten = readsensor()
    s.send(bytes(meten))
    s.send(packet)
    s.setblocking(False)

    data = s.recv(64)
    return(data)
