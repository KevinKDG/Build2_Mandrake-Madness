from network import Sigfox
import socket
import ubinascii

def send(humidity,distance):
    # init Sigfox for RCZ1 (Europe)
    sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

    # create a Sigfox socket
    s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

    # make the socket blocking
    s.setblocking(True)

    # configure it as uplink only
    s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)
    distance = 1800
    factor = floor(distance/255)
    rest = distance%255
    print(factor)
    print(rest)
    # send some bytes
    #s.send(string)
    s.send(bytes([humidity,factor,rest]))
