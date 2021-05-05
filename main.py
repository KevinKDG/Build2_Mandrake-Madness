from SI7021 import SI7021
import time
import wifi
import lora
import sigfox
from network import LoRa
import ultrasonic
from machine import *
import machine


# create an output pin on pin #0
p19 = Pin('P19',mode=Pin.OUT)

# set the value low then high




i2c = I2C(0, I2C.MASTER)
si7021 = SI7021(i2c)
lora.init()
while True:
    distance = ultrasonic.getdistance()

    try:
        humidity = si7021.humidity()
        temperature = si7021.temperature()
        info = str(distance)+"/"+str(humidity)+"/"+str(temperature)

        lora.send(humidity,distance,temperature)
        print(str(humidity)+" %")
        print(str(temperature)+" C")

        print("sent")   # de waardes verzonden naar adafruit dashboard
        rx_pkt = s.recv(64)
        if (len(rx_pkt) > 0)|humidity <=80:
            p19.value(1)
            time.sleep(5)
            p19.valeu(0)

    except Exception as e:
        print(e)
    time.sleep(5)
