#!/usr/bin/env python3
from subprocess import call
import time
import Adafruit_BBIO.GPIO as GPIO

while True:
    with open("/sys/class/i2c-adapter/i2c-2/2-0048/hwmon/hwmon0/temp1_input", 'r') as f:
            milliC = f.readline(-1)
            milliC = int(milliC)
            # print(milliC)
            normalC = milliC / 1000
            # print(normalC)
            normalF = (normalC * (9 / 5) + 32)
            print("Bottom Sensor: ", normalF)
            f.close()
    # with open("/sys/class/i2c-adapter/i2c-2/2-0049/hwmon/hwmon0/temp1_input", 'r') as f:
    #         milliC = f.readline(-1)
    #         milliC = int(milliC)
    #         # print(milliC)
    #         normalC = milliC / 1000
    #         # print(normalC)
    #         normalF = (normalC * (9 / 5) + 32)
    #         print("Top Sensor: ", normalF)
    #         f.close()
    time.sleep(1)
