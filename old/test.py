from machine import I2C, SoftI2C, Pin

i2c = I2C(0, scl=Pin(1), sda=Pin(0))

print(i2c.scan())


# i2c = SoftI2C(scl=Pin(15), sda=Pin(14), freq=15000)
# print(i2c.scan())