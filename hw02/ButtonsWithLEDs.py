#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import time

# LEDs
GPIO.setup("P9_12", GPIO.OUT)   # RED
GPIO.setup("P9_15", GPIO.OUT)   # YELLOW
GPIO.setup("P9_23", GPIO.OUT)   # GREEN
GPIO.setup("P9_27", GPIO.OUT)   # BLUE

# Buttons
GPIO.setup("P8_7", GPIO.IN)   # BUTTON 1
GPIO.setup("P8_9", GPIO.IN)   # BUTTON 2
GPIO.setup("P8_11", GPIO.IN)   # BUTTON 3
GPIO.setup("P8_15", GPIO.IN)   # BUTTON 4
GPIO.setup("P8_17", GPIO.IN)   # BUTTON 5


while True:
    # Top button with Red LED - WORKS
    if (GPIO.input("P8_7") == 1):
        GPIO.output("P9_12", GPIO.HIGH)
    else:
        GPIO.output("P9_12", GPIO.LOW)
    # Second button with Yellow LED
    if (GPIO.input("P8_9") == 1):
        GPIO.output("P9_15", GPIO.HIGH)
    else:
        GPIO.output("P9_15", GPIO.LOW)
    # Third button with Green LED
    if (GPIO.input("P8_11") == 1):
        GPIO.output("P9_23", GPIO.HIGH)
    else:
        GPIO.output("P9_23", GPIO.LOW)
    # Fourth button with Blue LED
    if (GPIO.input("P8_15") == 1):
        GPIO.output("P9_27", GPIO.HIGH)
    else:
        GPIO.output("P9_27", GPIO.LOW)
