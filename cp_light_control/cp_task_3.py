import time
import board
from analogio import AnalogOut

analog_out = AnalogOut(board.A0)
analog_in = AnalongIn(board.A2)

while True:
    # Count up from 0 to 65535, with 64 increment
    # which ends up corresponding to the DAC's 10-bit range
    analog_out.value = analog_in.value
