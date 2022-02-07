import time
import board
from analogio import AnalogIn

input = AnalogIn(board.D2)

while(True):
  print(input.value)
  
