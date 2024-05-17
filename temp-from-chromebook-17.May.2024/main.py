import network
import time
from machine import Pin
import wd

wd.id = "test123"


wifi = network.WLAN(network.STA_IF)

led = Pin("LED", Pin.OUT)

wifi.active(True)
wifi.connect('electronics-workshop', 'elecwork123')

def blink_led(times):
    for i in range(times):
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)


while ...:
    blink_led(wifi.status() + 3)
    time.sleep(1)

    if wifi.status() == 3:
        led.on()
        time.sleep(1)
        led.off()
        break
wd.connect_web_server()
wd.init_log()
wd.log("Connected to network")