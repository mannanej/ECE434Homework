This code will implement a text based version of Etch-A-Sketch on a 8x8 Matrix and the terminal.
There is a setup.sh file, but the python program should run the setup commands for you.
The grid starts with '.' in the blank spots and places a 'X' where the pen is.

You can move the pen with WASD/buttons/encoders and clear the screen with C/button5.
    - You can move the pen like a video game, W for UP, S for DOWN, A for LEFT, and D for RIGHT.
    - The way this is different from hw01 is you can now control the program with 5 buttons on the breadboard.
    - You can type in the console which input method you want.
    - If the buttons, top to bottom are 1-5:
    - 1. Up, 2. Left, 3. Down, 4. Right, 5. Clear.
    - The way this is different from hw02 is you can now control the program with 2 encoders on the breadboard.
    - The right knob is hooked to eQEP2 and turn it clockwise for UP and counterclockwise for DOWN
    - The left knob is hooked to eQEP0 and turn it clockwise for RIGHT and counterclockwise for LEFT

Due to the way the program reads inputs, you must hit ENTER after every input to update the screen, unless using the buttons or encoders.
The program will now display in the terminal and on the LED matrix.


For the temperature sensors, I used TMP101.sh to run the actual commands to read the inputs, then I used TMP101.py to read the bash file.
The sensor seems to work fine enough, but I couldn't seem to get the High and Low temps to set correctly. Everything else seems to work fine.
