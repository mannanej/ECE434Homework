#!/usr/bin/env python3
from subprocess import call
import time
import Adafruit_BBIO.GPIO as GPIO

# This starts an infinite while loop so we can just keep on reading temps
while True:
    # this opens the file that the kernal writes too
    with open("/sys/class/i2c-adapter/i2c-2/2-0048/hwmon/hwmon0/temp1_input", 'r') as f:
        # this chunk converts it from the base value to F
            milliC = f.readline(-1)
            milliC = int(milliC)
            # print(milliC)
            normalC = milliC / 1000
            # print(normalC)
            normalF = (normalC * (9 / 5) + 32)
            print("Bottom Sensor: ", normalF)
            f.close()
#     with open("/sys/class/i2c-adapter/i2c-2/2-0049/hwmon/hwmon0/temp1_input", 'r') as f:
#             milliC = f.readline(-1)
#             milliC = int(milliC)
#             # print(milliC)
#             normalC = milliC / 1000
#             # print(normalC)
#             normalF = (normalC * (9 / 5) + 32)
#             print("Top Sensor: ", normalF)
#             f.close()
    time.sleep(1)
