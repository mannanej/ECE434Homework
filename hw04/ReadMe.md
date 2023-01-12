This code will implement a simple version of Etch-A-Sketch on a 8x8 Matrix and the terminal.
There is a setup.sh file, but the python program should run the setup commands for you.
The grid starts with '.' in the blank spots and places a 'X' where the pen is.

You can move the pen and clear the screen with WASD/Buttons/Encoders/Flask.
    - You can type in the console which input method you want.
    - You can move the pen like a video game, W for UP, S for DOWN, A for LEFT, and D for RIGHT.
    - ***The way this is different from hw01 is you can now control the program with 5 buttons on the breadboard.***
    - If the buttons, top to bottom are 1-5:
    - 1. Up, 2. Left, 3. Down, 4. Right, 5. Clear.
    - ***The way this is different from hw02 is you can now control the program with 2 encoders on the breadboard.***
    - The right knob is hooked to eQEP2 and turn it clockwise for UP and counterclockwise for DOWN.
    - The left knob is hooked to eQEP0 and turn it clockwise for RIGHT and counterclockwise for LEFT.
    - The bottom button(5) is still for CLEAR while using the encoders.
    - ***The way this is different from hw03 is you can no control the program using Flask.***
    - You can access the Flask page by going to 192.168.7.2:8081.
    - The buttons work a little funny. If you hover over the button, it will count as a "click" until a button is actually clicked.
    This happens with all the buttons, but it works almost exactly the same as before.

Due to the way the program reads inputs, you must hit ENTER after every keyboard input to update the screen.
The program will now display in the terminal and on the LED matrix.
