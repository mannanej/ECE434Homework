from mmap import mmap
import struct
import time

GPIO1_offset = 0x4804c000
GPIO1_size = 0x4804cfff - GPIO1_offset
GPIO0_offset = 0x44e07000
GPIO0_size = 0x44e07fff - GPIO0_offset

GPIO_OE = 0x134
GPIO_DATAIN = 0x138
GPIO_SETDATAOUT = 0x194
GPIO_CLEARDATAOUT = 0x190

USR2 = 1<<23
USR3 = 1<<24

button1 = 1<<18 #P9_14
button0 = 1<<17 #P9_23

with open("/dev/mem", "r+b") as f:
    mem1 = mmap(f.fileno(), GPIO1_size, offset = GPIO1_offset)
    mem0 = mmap(f.fileno(), GPIO1_size, offset = GPIO1_offset)

packed_reg1 = mem1[GPIO_OE:GPIO_OE + 4]
packed_reg0 = mem0[GPIO_OE:GPIO_OE + 4]
reg_status1 = struct.unpack("<L", packed_reg1) [0]
reg_status0 = struct.unpack("<L", packed_reg0) [0]
reg_status1 &= ~(USR3) #3
reg_status0 &= ~(USR2)
mem1[GPIO_OE:GPIO_OE + 4] = struct.pack("<L", reg_status1)
mem0[GPIO_OE:GPIO_OE + 4] = struct.pack("<L", reg_status0)

try:
    while (True):
        button1state = struct.unpack("<L", mem1[GPIO_DATAIN:GPIO_DATAIN + 4]) [0] & button1
        button0state = struct.unpack("<L", mem0[GPIO_DATAIN:GPIO_DATAIN + 4]) [0] & button0
        if button1state:
            mem1[GPIO_SETDATAOUT:GPIO_SETDATAOUT + 4] = struct.pack("<L", USR3) #3
        if button0state:
            mem0[GPIO_SETDATAOUT:GPIO_SETDATAOUT + 4] = struct.pack("<L", USR2)
        if not button1state:
            mem1[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT + 4] = struct.pack("<L", USR3) #3
        if not button0state:
            mem0[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT + 4] = struct.pack("<L", USR2)

        # mem1[GPIO_SETDATAOUT:GPIO_SETDATAOUT + 4] = struct.pack("<L", USR3)
        # time.sleep(0.5)
        # mem1[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT + 4] = struct.pack("<L", USR3)
        # time.sleep(0.5)

except KeyboardInterrupt:
    mem1.close()
    mem0.close()