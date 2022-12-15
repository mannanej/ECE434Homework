This code will implement a text based version of Etch-A-Sketch on a 9x9 grid.
The grid starts with '.' in the blank spots and places a 'X' where the pen is.
You can move the pen with WASD and clear the screen with C.
    - The way this is different from hw01 is you can now control the program with 5 buttons on the breadboard.
    - You can type in the console which input method you want.
    - If the buttons, top to bottom are 1-5:
    - 1. Up, 2. Left, 3. Down, 4. Right, 5. Clear.
Due to the way the program reads inputs, you must hit ENTER after every input to update the screen, unless using the buttons.


1. What's the min and max voltage?
    - The min voltage is ~60mV and the max is ~360mV

2. What period and frequency is it?
    - The period is 81ns and the frequency is 12.27MHz
    - ***I dont know if these values are correct, the osilloscope was giving me strange readings. Some of my next answers may be wrong because of this.***

3. How close is it to 100ms?
    - It isn't close at all. Way off.

4. Why do they differ?
    - They differ because the actual board cannot run as fast as the code wants it too. So it pushes the pulse out as fast as it can.

5. Run htop and see how much processor you are using.
    - It is running around ~30%

6. Try different values for the sleep time (2nd argument). What's the shortest period you can get? Make a table of the fastest values you try and the corresponding period and processor usage. Try using markdown tables: https://www.markdownguide.org/extended-syntax/#tables
    - 

7. How stable is the period?
    - The period doesn't seem to be very stable at all.

8. Try launching something like vi. How stable is the period?
    - It seems like the period is a bit less stable, since we have to give up some processor.

9. Try cleaning up togglegpio.sh and removing unneeded lines. Does it impact the period?
    - It helps the period, but only a small amount.

10. Togglegpio.sh uses bash (first line in file). Try using sh. Is the period shorter?
    Yes. Shell runs faster.

11. What's the shortest period you can get?
    - 20ns


    # hw02 grading

| Points      | Description |
| ----------- | ----------- |
|  2/2 | Buttons and LEDs 
|  8/8 | Etch-a-Sketch works
|      | Measuring a gpio pin on an Oscilloscope 
|  2/2 | Questions answered
|  4/4 | Table complete
|  0/2 | gpiod
|      | Security
|  0/1 | ssh port 
|  0/1 | fail2ban
| 16/20   | **Total**


Max voltage seems too small.  81 ns period is way too small. What were you measuring?

I'm suprised c 2-bit is faster than python 2-bit.  Looks like you didn't do python with gpiod.

