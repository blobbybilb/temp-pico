from hmc5883l import HMC5883L

sensor = HMC5883L(scl=1, sda=0)

x, y, z = sensor.read()
print(sensor.format_result(x, y, z))