from machine import I2C
from qmc5883l import QMC5883L
from time import sleep

# Please check that correct PINs are set on hmc5883l library!
i2c = I2C(id=0)
print(i2c.scan())
sensor = QMC5883L(i2c)

Xmin=1000
Xmax=-1000
Ymin=1000
Ymax=-1000

while True:
    try:
        sleep(0.2)
        x, y, z, _ = sensor.read_scaled()
        Xmin=min(x,Xmin)
        Xmax=max(x,Xmax)
        Ymin=min(y,Ymin)
        Ymax=max(y,Ymax)
        # print(sensor.format_result(x, y, z))
        print("Xmin="+str(Xmin)+"; Xmax="+str(Xmax)+"; Ymin="+str(Ymin)+"; Ymax="+str(Ymax))

    except KeyboardInterrupt:
        print()
        print('Got ctrl-c')
        
        xs=1
        ys=(Xmax-Xmin)/(Ymax-Ymin)
        xb =xs*(1/2*(Xmax-Xmin)-Xmax)
        yb =xs*(1/2*(Ymax-Ymin)-Ymax)
        print("Calibration corrections:")
        print("xs="+str(xs))
        print("xb="+str(xb))
        print("ys="+str(ys))
        print("yb="+str(yb))
        break