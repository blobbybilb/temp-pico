import drv
from machine import Pin, PWM, SoftI2C
import time
from tof import VL53L4CD

frequency = 40_000

ain1 = PWM(Pin(12, Pin.OUT))
ain2 = PWM(Pin(11, Pin.OUT))
bin1 = PWM(Pin(14, Pin.OUT))
bin2 = PWM(Pin(13, Pin.OUT))
ain1.freq(frequency)
ain2.freq(frequency)
bin1.freq(frequency)
bin2.freq(frequency)

md = drv.DRV8833(ain1, ain2, bin1, bin2)

md.throttle_a(0.9)
md.throttle_b(-0.9)
time.sleep(2)
md.stop_a()
md.stop_b()
md.deinit()

tof = VL53L4CD(SoftI2C(scl=Pin(19), sda=Pin(18)))
tof.start_ranging()

while ...:
    while not tof.data_ready:
        pass
    tof.clear_interrupt()
    print("Distance: {} cm".format(tof.distance))
