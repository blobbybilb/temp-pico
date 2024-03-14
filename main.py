# Example for Pycom device.
# Connections:
# xxPy | QMC5883
# -----|-------
# P9   |  SDA
# P10  |  SCL

from machine import I2C, Pin
from qmc5883l import QMC5883L
import math

i2c = I2C(id=0)
print(i2c.scan())
qmc5883 = QMC5883L(i2c)

avg_of = 10

def avg_and_round(x):
    return round(x / avg_of * 1000)

# D = arctan(yGaussData/xGaussData)∗(180/π)

def get_angle(x, y):
    if x == 0:
        print("x is 0")
        return 90
    return math.atan(y / x) * (180 / math.pi)

while ...:
    x = y = z = t = 0

    for i in range(avg_of):
        xi, yi, zi = qmc5883.read_calib()
        # xi_raw, yi_raw, zi_raw, ti_raw = qmc5883.read_raw()
        # xi, yi, zi, ti = xi / xi_raw, yi / yi_raw, zi / zi_raw, ti / ti_raw
        x += xi
        y += yi
        z += zi
        # t += ti

    x, y, z = avg_and_round(x), avg_and_round(y), avg_and_round(z)

    print(x, y, z, get_angle(x, y))
    # print(x, y, z)


