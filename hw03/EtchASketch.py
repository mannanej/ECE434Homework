#!/usr/bin/env python3
# This program will implement a Etch-A-Sketch program
# Program created by Eddie Mannan on 12/8/2022
import sys
import smbus
from array import *
import time
from subprocess import call
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2

# This method is the MAIN method, it sets up some globals for the code and gets things initialized
def main():
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

    for line in sys.stdin:
        if (line.__contains__("k")):
            keyboard(currentX, currentY, screen)
        elif (line.__contains__("b")):
            buttons(currentX, currentY, screen)
        elif (line.__contains__("e")):
            encoders(currentX, currentY, screen)
####################################################################################################################################
# This method will run through and print the screen array
def printScreen(screen):
    # This chuck will display the sketch on the LED matrix
    bus = smbus.SMBus(2)
    bus.write_byte_data(0x70, 0x21, 0)  # Start oscillator
    bus.write_byte_data(0x70, 0x81, 0)  # Disp on
    bus.write_byte_data(0x70, 0xe7, 0)  # Full brightness
    matrix = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

    for row in range(8):
        greenBits = 0
        redBits = 0
        for column in range(8):
            if screen[row][column] == 'X':
                greenBits += 1 << column
        matrix[2 * row] = greenBits
        matrix[2 * row + 1] = redBits
    bus.write_i2c_block_data(0x70, 0, matrix)

    # This chunk will display the sketch on the terminal
    for row in screen:
        for column in row:
            print(column, end=" ")
        print()
####################################################################################################################################
# This method will listen for inputs from the keyboard, and add an X to the screen in the correct location
def keyboard(currentX, currentY, screen):
    print("Start of Keyboard:")
    for line in sys.stdin:
        if (line.__contains__('w') and currentX >= 1):          # UP
            currentX = currentX - 1
        elif (line.__contains__('a') and currentY >= 1):        # LEFT
            currentY = currentY - 1
        elif (line.__contains__('s') and currentX <= 6):        # DOWN
            currentX = currentX + 1
        elif (line.__contains__('d') and currentY <= 6):        # RIGHT
            currentY = currentY + 1
        elif (line.__contains__('c')):                          # CLEAR
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
####################################################################################################################################
# This method will listen for inputs from the buttons, and add an X to the screen in the correct location
def buttons(currentX, currentY, screen):
    print("Start of Buttons:")
    while True:
        if (GPIO.input("P8_7") == 1 and currentX >= 1):             # UP
            currentX = currentX - 1
        elif (GPIO.input("P8_9") == 1 and currentY >= 1):           # LEFT
            currentY = currentY - 1
        elif (GPIO.input("P8_18") == 1 and currentX <= 6):          # DOWN
            currentX = currentX + 1
        elif (GPIO.input("P8_15") == 1 and currentY <= 6):          # RIGHT
            currentY = currentY + 1
        elif (GPIO.input("P8_17") == 1):                            # CLEAR
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
        time.sleep(0.25)
####################################################################################################################################
# This method will listen for inputs from the encoders, and add an X to the screen in the correct location
def encoders(currentX, currentY, screen):
    print("Start of Encoders:")
    # This command will run the setup.sh file to config our encoder pins
    setupFile = call("./setup.sh", shell=True)
    # This section will set our pins to enabled and set the ceiling to 1000000
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
    
    # This chunk will read the encoders and display their location to the screen
    while True:
        # This chunk will read the count file to see how much the encoder has moved
        with open("/dev/bone/counter/2/count0/count", 'r') as f:
            dataUpDown = f.readline(-1)
            dataUpDown = int(dataUpDown)
            f.close()
            # print("Old: ", oldDataUpDown)
            # print("New: ", dataUpDown)
        with open("/dev/bone/counter/0/count0/count", 'r') as f:
            dataLeftRight = f.readline(-1)
            dataLeftRight = int(dataLeftRight)
            f.close()
            # print("Old: ", oldDataLeftRight)
            # print("New: ", dataLeftRight)
        if (dataUpDown > oldDataUpDown and currentX >= 1):          # Up
            currentX = currentX - 1
            oldDataUpDown = dataUpDown
        elif (dataLeftRight > oldDataLeftRight and currentY >= 1):  # Left
            currentY = currentY - 1
            oldDataLeftRight = dataLeftRight
        elif (dataUpDown < oldDataUpDown and currentX <= 6):        # Down
            currentX = currentX + 1
            oldDataUpDown = dataUpDown
        elif (dataLeftRight < oldDataLeftRight and currentY <= 6):  # RIGHT
            currentY = currentY + 1
            oldDataLeftRight = dataLeftRight
        elif (GPIO.input("P8_17") == 1):                            # CLEAR
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
        time.sleep(0.25)
####################################################################################################################################
# This is a call to main to get the ball rolling
main()
# END FILE
####################################################################################################################################
