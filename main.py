from machine import I2C
from SI7021 import SI7021
import time
import wifi
import lora
from network import LoRa
import ultrasonic


loraactive = False

if loraactive:
    LoRa = lora.init()
if not loraactive:
    wifi.set_connect()
ultrasonic.defsensor()
print("sensor")

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
            wifi.sendhumidity(humidity)
            print("wifi")

        else:
            lora.send(distance)
            print("LoRa")
        print(str(humidity)+" %")
        print(str(temperature)+" C")
    except Exception as e:
        print(e)


    time.sleep(5)
