In section 2.6 Blinking an LED:
- To start the code, you must run: sudo make TARGET=hello.pru0 start
- To stop the code, you must run: sudo make TARGET=hello.pru0 stop
- I got a frequency of 12.5 MHz. There is some jitter, but it seems to be mostly stable

In section 5.3 PWM Generator:
- Here, I got a different frequency of 66.5 MHz with a Standard Deviation of ~0.5 MHz. There doesn't seem to be any jitter, the signal looks very stable, just not very symetric


# hw08 grading

| Points      | Description |
| ----------- | ----------- |
| 14/14 | PRU
|  0/2 | Controlling the PWM Frequency - optional
|  0/2 | Reading an Input at Regular Intervals - optional
|  0/2 | Analog Wave Generator - optional
| 14 | **Total**

*My comments are in italics. --may*
