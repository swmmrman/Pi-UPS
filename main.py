from ina219 import INA219
from ina219 import DeviceRangeError
from time import sleep

ah = 0
wh = 0
rs = 0
rm = 0
rh = 0

SHUNT_R = 0.05
MAX_AMPS = 3

ina = INA219(SHUNT_R, MAX_AMPS)
ina.configure()

try:
    while True:
        volts = ina.voltage()
        amps = (ina.current() / 1000)
        watts = volts * amps
        wh = wh + (watts / 60 / 60 / 4)
        ah = ah + (amps / 60 / 60 / 4)
        rs = rs + 0.25
        if rs == 60:
            rs = 0
        rm = rm + 1
        if rm == 60:
            rm = 0
        rh = rh + 1
        print(F"\rWatts:\t\t{watts:.4f}w\n"
              F"Voltage:\t{volts:.4f}v\n"
              F"Current:\t{amps:.4f}a\n"
              F"WH:\t\t{wh:.4f}wh\n"
              F"Energy:\t\t{ah:.4f}ah\n"
              F"Time:\t\t{rh:02d}:{rm:02d}:{rs:02.1f}  ",
              end="")
        sleep(0.25)
        print("\033[A"*6)
except KeyboardInterrupt:
    print("\n")
