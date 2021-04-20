import wifi
import sensor
import lora
import time
from network import LoRa
import machine
loraactive = False

if loraactive:
    LoRa = lora.init()
if not loraactive:
    wifi.set_connect()

sensor.defsensor()
print("sensor")
while True:

    distance = sensor.getdistance()
    if not loraactive:
        wifi.send(distance)
        print("wifi")

    else:
        lora.send(distance)
        print("LoRa")
    print("sleeping")
    machine.sleep(10000,True)
    print("waking up")
# power usage sleep 40 10s, active 70 3s
#30,76923076923077 + 233,3333333333333 /13
#20,31558185404339mAh
#60h
