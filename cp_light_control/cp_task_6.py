# Write your code here :-)
import time
import board
from analogio import AnalogOut, AnalogIn

analog_out = AnalogOut(board.A0)
analog_in = AnalogIn(board.A2)

k = 1



while True:
    # Count up from 0 to 65535, with 64 increment
    # which ends up corresponding to the DAC's 10-bit range\
    error = 60000 - analog_in.value
    adjust = error*k
    analog_out.value += adjust
    print(analog_in.value)
