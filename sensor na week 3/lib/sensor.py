from machine import UART
import time

uart = UART(1)
uart.init(baudrate=9600, bits=8, parity=None, stop=1, timeout_chars=100, pins=
('P3','P4'))

def readsensor():
    while True:
        header_bytes = uart.read(1)
        while(header_bytes !=b'\xff'):
            header_bytes = uart.read(1)
        DATA_H = int(uart.read(1)[0])
        DATA_L = int(uart.read(1)[0])
        SUM = int(uart.read(1)[0]) +1

        distance = (DATA_H*256)+DATA_L

        if distance < 30:
            print("too close it is corona time")
        else:
            cm = distance / 10
            print("distance: " + str(cm) + " cm")
            time.sleep(1)

readsensor()
