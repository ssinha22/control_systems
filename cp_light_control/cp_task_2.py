import time
import board
from analogio import AnalogIn

analog_in = AnalogIn(board.d2)

analog_in.value = 0

def getValue(pin):
  return 255*(pin.value/65536)

value = 0
for(value<255):
  analog_in.value += 100
  value = getValue(analog_in)
