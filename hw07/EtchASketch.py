#!/usr/bin/env python3
# This program will implement a Etch-A-Sketch program
# Program created by Eddie Mannan on 12/8/2022
# import sys
import smbus
from array import *
import time
from flask import Flask, render_template, request

# This method is the MAIN method, it sets up some globals for the code and gets things initialized
def main():

    # Simple print statements that tell the user how to play
    print("Start of Etch-A-Sketch")

    # Load some init values for the program
    global currentX
    currentX = 1
    global currentY
    currentY = 1

    global screen
    screen = [['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.']]

    app = Flask(__name__)

    @app.route("/")
    @app.route("/<state>")
    def checkMove (state = None):
        global currentX
        global currentY
        global screen
        if state == 'up' and currentX >= 2:     # UP
            currentX = currentX - 1
        elif state == 'left' and currentY >= 2:   # LEFT
            currentY = currentY - 1
        elif state == 'down' and currentX <= 5:   # DOWN
            currentX = currentX + 1
        elif state == 'right' and currentY <= 5:   # RIGHT
            currentY = currentY + 1
        elif state == 'clear':                    # CLEAR
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
        template_data = {
            'title' : state,
        }
        return render_template('index.html', **template_data)
    
    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=8081, debug=True)
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
# This is a call to main to get the ball rolling
main()
# END FILE
####################################################################################################################################
