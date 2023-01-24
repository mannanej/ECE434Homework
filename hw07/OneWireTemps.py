#!/usr/bin/env python3
from subprocess import call
import Adafruit_BBIO.GPIO as GPIO

# This starts an infinite while loop so we can just keep on reading temps
while True:
    # this opens the file that the kernal writes too
    with open("/sys/class/hwmon/hwmon0/temp1_input", 'r') as f:
        # this chunk converts it from the base value to F
            milliC = f.readline(-1)
            milliC = int(milliC)
            # print(milliC)
            normalC = milliC / 1000
            # print(normalC)
            normalFRight = (normalC * (9 / 5) + 32)
            # print("Right Sensor: ", normalF)
            f.close()
    with open("/sys/class/hwmon/hwmon1/temp1_input", 'r') as f:
        # this chunk converts it from the base value to F
            milliC = f.readline(-1)
            milliC = int(milliC)
            # print(milliC)
            normalC = milliC / 1000
            # print(normalC)
            normalFMiddle = (normalC * (9 / 5) + 32)
            # print("Middle Sensor: ", normalF)
            f.close()
    with open("/sys/class/hwmon/hwmon2/temp1_input", 'r') as f:
        # this chunk converts it from the base value to F
            milliC = f.readline(-1)
            milliC = int(milliC)
            # print(milliC)
            normalC = milliC / 1000
            # print(normalC)
            normalFLeft = (normalC * (9 / 5) + 32)
            # print("Left Sensor: ", normalF)
            f.close()
    print("Left Temp: ", normalFLeft, " Middle Temp: ", normalFMiddle, " Right Temp: ", normalFRight)
