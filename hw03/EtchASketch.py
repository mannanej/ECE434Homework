#!/usr/bin/env python3
# This program will implement a text based Etch-A-Sketch program that runs in the terminal and on a LED matrix
# Program created by Eddie Mannan on 12/8/2022
import sys
import smbus
from array import *
import time
from subprocess import call
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2

# Buttons
GPIO.setup("P8_7", GPIO.IN)   # BUTTON 1
GPIO.setup("P8_9", GPIO.IN)   # BUTTON 2
GPIO.setup("P8_18", GPIO.IN)   # BUTTON 3
GPIO.setup("P8_15", GPIO.IN)   # BUTTON 4
GPIO.setup("P8_17", GPIO.IN)   # BUTTON 5

# Simple print statements that tell the user how to play
print("Start of Etch-A-Sketch")
print("Instructions:")
print("W: Move Pen Up   ---  S: Move Pen Down")
print("A: Move Pen Left --- D: Move Pen Right")
print("C: Clear/Shake")
print("***Must Hit ENTER After Each Letter Entry To Make Pen Move***")
print("")
print("Keyboard or Buttons or Encoders?")

# Load some init values for the program
currentX = 1
currentY = 1

screen = [['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.']]

# This method will run through and print the screen array
def printScreen(screen):
    # This chuck will display the sketch on the LED matrix
    bus = smbus.SMBus(2)
    bus.write_byte_data(0x70, 0x21, 0)  # Start oscillator
    bus.write_byte_data(0x70, 0x81, 0)  # Disp on
    bus.write_byte_data(0x70, 0xe7, 0)  # Full brightness
    matrix = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

    for x in range(8):
        greenBits = 0
        redBits = 0
        for y in range(8):
            if screen[x][y] == 'X':
                greenBits += 1 << y
        matrix[2 * x] = greenBits
        matrix[2 * x + 1] = redBits
    bus.write_i2c_block_data(0x70, 0, matrix)

    for row in screen:
        for column in row:
            print(column, end=" ")
        print()


def keyboard(currentX, currentY, screen):
    print("Start of Keyboard:")
    # This method will listen for inputs from the keyboard, and add an X to the screen in the correct location
    for line in sys.stdin:
        if (line.__contains__('w') and currentX >= 1):
            currentX = currentX - 1
            currentY = currentY
        elif (line.__contains__('a') and currentY >= 1):
            currentX = currentX
            currentY = currentY - 1
        elif (line.__contains__('s') and currentX <= 6):
            currentX = currentX + 1
            currentY = currentY
        elif (line.__contains__('d') and currentY <= 6):
            currentX = currentX
            currentY = currentY + 1
        elif (line.__contains__('c')):
            screen = [['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.']]
        screen[currentX][currentY] = 'X'
        printScreen(screen)


def buttons(currentX, currentY, screen):
    print("Start of Buttons:")
    # This method will listen for inputs from the buttons, and add an X to the screen in the correct location
    while True:
        if (GPIO.input("P8_7") == 1 and currentX >= 1):
            currentX = currentX - 1
            currentY = currentY
            screen[currentX][currentY] = 'X'
            printScreen(screen)
            time.sleep(0.5)
        elif (GPIO.input("P8_9") == 1 and currentY >= 1):
            currentX = currentX
            currentY = currentY - 1
            screen[currentX][currentY] = 'X'
            printScreen(screen)
            time.sleep(0.5)
        elif (GPIO.input("P8_18") == 1 and currentX <= 6):
            currentX = currentX + 1
            currentY = currentY
            screen[currentX][currentY] = 'X'
            printScreen(screen)
            time.sleep(0.5)
        elif (GPIO.input("P8_15") == 1 and currentY <= 6):
            currentX = currentX
            currentY = currentY + 1
            screen[currentX][currentY] = 'X'
            printScreen(screen)
            time.sleep(0.5)
        elif (GPIO.input("P8_17") == 1):
            screen = [['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.']]
            screen[currentX][currentY] = 'X'
            printScreen(screen)
            time.sleep(0.5)

def encoders(currentX, currentY, screen):
    print("Start of Encoders:")
    # This method will listen for inputs from the encoders, and add an X to the screen in the correct location
    setupFile = call("./setup.sh", shell=True)
    with open("/dev/bone/counter/2/count0/enable", 'w') as f:
        f.write('1')
        f.close()
    with open("/dev/bone/counter/2/count0/ceiling", 'w') as f:
        f.write('1000000')
        f.close()
    with open("/dev/bone/counter/0/count0/enable", 'w') as f:
        f.write('1')
        f.close()
    with open("/dev/bone/counter/0/count0/ceiling", 'w') as f:
        f.write('100')
        f.close()
    oldDataUpDown = 1000000
    oldDataLeftRight = 1000000
    
    while True:
        with open("/dev/bone/counter/2/count0/count", 'r') as f:
            dataUpDown = f.readline(-1)
            dataUpDown = int(dataUpDown)
            f.close()
        with open("/dev/bone/counter/0/count0/count", 'r') as f:
            dataLeftRight = f.readline(-1)
            dataLeftRight = int(dataLeftRight)
            f.close()
            print("Old: ", oldDataLeftRight)
            print("New: ", dataLeftRight)
        if (dataUpDown > oldDataUpDown and currentX >= 1):  # Up
            currentX = currentX - 1
            currentY = currentY
            screen[currentX][currentY] = 'X'
            printScreen(screen)
            oldDataUpDown = dataUpDown
        elif (dataLeftRight > oldDataLeftRight and currentY >= 1):  # Left
            currentX = currentX
            currentY = currentY - 1
            screen[currentX][currentY] = 'X'
            printScreen(screen)
            oldDataLeftRight = dataLeftRight
        elif (dataUpDown < oldDataUpDown and currentX <= 6):    # Down
            currentX = currentX + 1
            currentY = currentY
            screen[currentX][currentY] = 'X'
            printScreen(screen)
            oldDataUpDown = dataUpDown
        elif (dataLeftRight < oldDataLeftRight and currentY <= 6):  # Right
            currentX = currentX
            currentY = currentY + 1
            screen[currentX][currentY] = 'X'
            printScreen(screen)
            oldDataLeftRight = dataLeftRight
        elif (GPIO.input("P8_17") == 1):
            screen = [['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.']]
            screen[currentX][currentY] = 'X'
            printScreen(screen)
        time.sleep(1)

inputs = ""
for line in sys.stdin:
    if (line.__contains__("k")):
        keyboard(currentX, currentY, screen)
    elif (line.__contains__("b")):
        buttons(currentX, currentY, screen)
    elif (line.__contains__("e")):
        encoders(currentX, currentY, screen)
