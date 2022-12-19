#!/usr/bin/env python3
from subprocess import call
import time
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P9_30", GPIO.IN) # Alert

while True:
    otherFile = call("./TMP101.sh", shell=True)
    if (GPIO.input("P9_30") == 1):
        print("ALERT")
    time.sleep(1)
