from machine import I2C, Pin
from libs.vl53l4cd import VL53L4CD

# Make sure to set the correct pins!
i2c_1 = I2C(id=1, sda=Pin(2), scl=Pin(3))
print(i2c_1.scan())
vl53_1 = VL53L4CD(i2c_1)

# OPTIONAL: can set non-default values
vl53_1.inter_measurement = 0
vl53_1.timing_budget = 20

i2c_2 = I2C(id=0, sda=Pin(0), scl=Pin(1))
print(i2c_2.scan())
vl53_2 = VL53L4CD(i2c_2)

# OPTIONAL: can set non-default values
vl53_2.inter_measurement = 0
vl53_2.timing_budget = 20

# print("VL53L4CD Simple Test.")
# print("--------------------")
# model_id, module_type = vl53_1.model_info
# print("Model ID: 0x{:0X}".format(model_id))
# print("Module Type: 0x{:0X}".format(module_type))
# print("Timing Budget: {}".format(vl53_1.timing_budget))
# print("Inter-Measurement: {}".format(vl53_1.inter_measurement))
# print("--------------------")

vl53_1.start_ranging()

while True:
    while not vl53_1.data_ready:
        pass
    vl53_1.clear_interrupt()
    print("Distance: {} cm".format(vl53_1.distance))

    while not vl53_2.data_ready:
        pass
    vl53_2.clear_interrupt()
    print("Distance: {} cm".format(vl53_2.distance))
    