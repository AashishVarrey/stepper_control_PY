#!/usr/bin/python3

#necessary modules
import RPi.GPIO as GPIO
import time
import json
#from PCF8591 import ADC
from stepper1 import stepper

"""GPIO.setmode(GPIO.BCM)

#ADC OBJECT
LED = ADC(0X48)

#set up led pin
ledPin = 26
GPIO.setup(ledPin, GPIO.OUT)

#set up motor pins
pins = [12,16,20,21]
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial = 0)

#stepper motor object
motor = stepper()"""
#variable to keep track of old angle
oldangle = 0
motor = stepper(0x48)
try:
  while True:
    with open("Lab5.txt","r") as f:
      data = json.load(f)
    newangle = int(data["newangle"])

    if newangle == 0:
      motor.zero()
    else:
      if oldangle < newangle:
        if abs(oldangle - newangle) < 180:
          motor.goAngle(abs(oldangle-newangle,1))
          oldangle = newangle
          #rotate clockwise assuming that clockwise is towards larger values
          #old angle equals new anlgle
        else:
          motor.goAngle(abs(oldangle-newangle,-1))
          oldangle = newangle
          #rotate ccw
          #oldangle = new angle
      elif oldangle > newangle:
        if abs(oldangle - newangle) < 180:
          motor.goAngle(abs(oldangle-newangle),-1)
          oldangle = newangle
          #rotate ccw
          #old angle = new angle
        else:
          motor.goAngle(abs(oldangle-newangle),1)
          oldangle = newangle
          #rotate cw
          #old angle = new angle
      else:
        #do nothing sinc ethe two angles are the same
        pass
except:
  GPIO.cleanup()
