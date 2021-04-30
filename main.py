from SI7021 import SI7021
import time
import wifi
import lora
from network import LoRa
import ultrasonic
from machine import *
import machine


# create an output pin on pin #0
p19 = Pin('P19',mode=Pin.OUT)

# set the value low then high

loraactive = False

if loraactive:
    LoRa = lora.init()
if not loraactive:
    wifi.set_connect()
ultrasonic.defsensor()


i2c = I2C(0, I2C.MASTER)
si7021 = SI7021(i2c)
while True:
    distance = ultrasonic.getdistance()

    try:
        humidity = si7021.humidity()
        temperature = si7021.temperature()
        info = str(distance)+"/"+str(humidity)+"/"+str(temperature)
        if not loraactive:
            wifi.sendultra(distance)
            print(str(humidity)+" %")
            print(str(temperature)+" C")
            wifi.sendhumidity(humidity)
            wifi.sendtemperature(temperature)
            print("wifi")   # de waardes verzonden naar adafruit dashboard

        else:
            lora.send(distance)
            print("LoRa")
        if(humidity <= 50):
            p19.value(1)
            time.sleep(10)
            p19.value(0)

    except Exception as e:
        print(e)

    print("sleeping")
    machine.sleep(5000, True)
    print("wake up")
