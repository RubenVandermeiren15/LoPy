from machine import UART

uart = UART(1)

uart.init(baudrate=9600, bits=8, parity=None, stop=1, timeout_chars=100, pins=('P3','P4'))

while True:
    header_bytes = uart.read(1)
    while(header_bytes !=b'\xff'):
        header_bytes = uart.read(1)
    DATA_H = print(int(uart.read(1)[0])
    DATA_L = print(int(uart.read(1)[0])
    SUM = print(int(uart.read(1)[0]) +1

    if(DATA_H + DATA_L == SUM):
        distance = (DATA_H*256)+DATA_L
        print(distance)
