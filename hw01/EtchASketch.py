#!/usr/bin/env python3
# This program will implement a text based Etch-A-Sketch program that runs in the terminal
# Program created by Eddie Mannan on 12/8/2022
import sys
from array import *

# Simple print statements that tell the user how to play
print("Start of Etch-A-Sketch")
print("Instructions:")
print("W: Move Pen Up   ---  S: Move Pen Down")
print("A: Move Pen Left --- D: Move Pen Right")
print("C: Clear/Shake")
print("***Must Hit ENTER After Each Letter Entry To Make Pen Move***")

# Load some init values for the program
currentX = 1
currentY = 1

screen = [['', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        ['0', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['4', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['5', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['6', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['7', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['8', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['9', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]

# This method will run through and print the screen array
def printScreen():
    for row in screen:
        for column in row:
            print(column, end = " ")
        print()

# This method will listen for inputs, and add an X to the screen in the correct location
for line in sys.stdin:
    if (line.__contains__('w') and currentX >= 2):
        currentX = currentX - 1
        currentY = currentY
    elif (line.__contains__('a') and currentY >= 2):
        currentX = currentX
        currentY = currentY - 1
    elif (line.__contains__('s') and currentX <= 9):
        currentX = currentX + 1
        currentY = currentY
    elif (line.__contains__('d') and currentY <= 9):
        currentX = currentX
        currentY = currentY + 1
    elif (line.__contains__('c')):
        screen = [['', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        ['0', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['4', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['5', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['6', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['7', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['8', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['9', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
    screen[currentX][currentY] = 'X'
    printScreen()
