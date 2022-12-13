#!/usr/bin/env python3
# This program will flash an LED as fast as possible
# Program created by Eddie Mannan on 12/12/2022
import time
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P9_12", GPIO.OUT)   # RED

print("Fast Blink Start")
while True:
    GPIO.output("P9_12", GPIO.HIGH)
    GPIO.output("P9_12", GPIO.LOW)
