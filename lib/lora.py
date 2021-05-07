from network import LoRa
import socket
import time
import ubinascii
import ustruct
import math





def init():
    teller = 0
    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
    app_eui = ubinascii.unhexlify('70B3D57ED003E4D4')
    app_key = ubinascii.unhexlify('511FCEA75A175980B26A145EAC4C56E9')
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
    while not lora.has_joined():
        time.sleep(1)
        print('Not yet joined...')
        teller = teller+1
        if teller==10:
            break
    return(lora)

def send(humidity,distance,temperature):
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    print('hello')
    factor = math.floor(distance/255)
    humidity = math.floor(humidity)
    temperature = math.floor(temperature)
    rest = distance%255
    print("H", humidity)
    print("T",temperature)
    print("F",factor)
    print("R",rest)

    print("yo")
    # send the prepared packet via LoRa
    s.send(bytes([humidity,factor,rest,temperature]))
