
from network import WLAN
from mqtt import MQTTClient
import machine
import time


wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid='telenet-2201056', auth=(WLAN.WPA2, '4XpNpfyjhuh3'))

while not wlan.isconnected():
    machine.idle()
print("Connected to Wifin")
client = MQTTClient("Lopy4", "192.168.0.196", port=1883)
#client = MQTTClient("device_id", "io.adafruit.com",user="your_username", password="your_api_key", port=1883)
#client.set_callback(sub_cb)
client.connect()
#client.subscribe(topic="youraccount/feeds/lights")
while True:
    print("Sending ON")
    client.publish(topic="sensor/programmatic", msg="ON")
    time.sleep(1)
    print("Sending OFF")
    client.publish(topic="sensor/programmatic", msg="OFF")

    time.sleep(1)
