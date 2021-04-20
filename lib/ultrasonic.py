from machine import UART

uart = UART(1)
def defsensor():
    uart = UART(1)
    uart.init(baudrate=9600, bits=8, parity=None, stop=1, timeout_chars=100)

def getdistance():
    uart.init(baudrate=9600, bits=8, parity=None, stop=1, timeout_chars=100)
    header_bytes = uart.read(1)
    while(header_bytes != b'\xff'):
         header_bytes = uart.read(1)
         print(header_bytes)
    DATA_H = int(uart.read(1)[0])
    DATA_L = int(uart.read(1)[0])
    SUM = int(uart.read(1)[0])

    if(DATA_H + DATA_L - SUM):
        distance = (DATA_H*256)+DATA_L
        return(distance)
