# Write your code here :-)

import board
import busio
import time
import math

from sphero_rvr import *

import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D11, echo_pin=board.D10)

#declare rvr as RVRDrive object
rvr = RVRDrive()
#wake
rvr.wake()

#Set leds to red
rvr.set_all_leds(255,0,0)
time.sleep(0.1)
#Set leds to green
rvr.set_all_leds(0,255,0)
time.sleep(0.1)
#Set leds to blue
rvr.set_all_leds(0,0,255)
time.sleep(0.1)
#turn off leds
rvr.set_all_leds(0,0,0)

#Set control parameters
setpoint = 100.0
k = 3
MAX_SPEED = 255

while True:
    try:
        sensor_distance = sonar.distance

        # Add your proportional control code here.
        error = setpoint - sensor_distance
        output = k*error

        if(output > MAX_SPEED):
            output = MAX_SPEED
        elif(output < -MAX_SPEED):
            output = -MAX_SPEED

        # Read the Sphero RVR library file to find the rvr.setMotors(left,right) command.
        # Use this command in the next line to send the output of your proportional
        # control to both the left and right motors.
        
        rvr.setMotors(output,output)
        
    except RuntimeError:
        print("Retrying!")
        pass
    time.sleep(0.2)

