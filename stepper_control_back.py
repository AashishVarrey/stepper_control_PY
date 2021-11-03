#!/usr/bin/python3

#necessary modules
import RPi.GPIO as GPIO
import time
import json

GPIO.setmode(GPIO.BCM)

pins = [12,16,20,21]
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial = 0)

#adjust led pin as needed
ledPin = 26
GPIO.setup(ledPin, GPIO.OUT)
oldangle = 0

try:
  global oldangle
  while True:
    with open("Lab5.txt","r") as f:
      data = json.load(f)
    newangle = int(data["newangle"])

    if newangle == 0:
      #run led code
      #spin motor in certain direction until adc value is...
      break
    else:
      if oldangle < newangle:
        if abs(oldangle - newangle) < 180:
          #rotate clockwise assuming that clockwise is towards larger values
          #old angle equals new anlgle
        else:
          #rotate ccw
          #oldangle = new angle
          pass
      elif:
        if oldangle > newangle:
          if abs(oldangle - newangle) < 180:
            #rotate ccw
            #old angle = new angle
          else:
            #rotate cw
            #old angle = new angle
      else:
        #do nothing sinc ethe two angles are the same
        pass

