This code will implement a text based version of Etch-A-Sketch on a 9x9 grid.
The grid starts with '.' in the blank spots and places a 'X' where the pen is.
You can move the pen with WASD and clear the screen with C.
    - The way this is different from hw01 is you can now control the program with 5 buttons on the breadboard.
    - You can type in the console which input method you want.
    - If the buttons, top to bottom are 1-5:
    - 1. Up, 2. Left, 3. Down, 4. Right, 5. Clear.
Due to the way the program reads inputs, you must hit ENTER after every input to update the screen, unless using the buttons.


1. What's the min and max voltage?

2. What period and frequency is it?

3. How close is it to 100ms?

4. Why do they differ?

5. Run htop and see how much processor you are using.

6. Try different values for the sleep time (2nd argument). What's the shortest period you can get? Make a table of the fastest values you try and the corresponding period and processor usage. Try using markdown tables: https://www.markdownguide.org/extended-syntax/#tables

7. How stable is the period?

8. Try launching something like vi. How stable is the period?

9. Try cleaning up togglegpio.sh and removing unneeded lines. Does it impact the period?

10. Togglegpio.sh uses bash (first line in file). Try using sh. Is the period shorter?

11. What's the shortest period you can get?