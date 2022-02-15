# Write your code here :-)
# Write your code here :-)
import time
import board
from analogio import AnalogOut, AnalogIn

analog_out = AnalogOut(board.A0)
analog_in = AnalogIn(board.A2)

k = 1
ktwo = 0.1
sum_error = 0

while True:
    # Count up from 0 to 65535, with 64 increment
    # which ends up corresponding to the DAC's 10-bit range\
    error = 60000 - analog_in.value
    sum_error += error
    adjust = error*k - sum_error*ktwo
    analog_out.value += adjust
    print(analog_in.value)
