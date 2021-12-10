#!/usr/bin/python3

#necessary modules
import RPi.GPIO as GPIO
import time
import json
from PCF8591 import ADC
from stepper2 import stepper

GPIO.setmode(GPIO.BCM)

#ADC OBJECT
#LED = ADC(0X48)

#set up led pin
#ledPin = 26
GPIO.setup(26, GPIO.OUT, initial = 0)

state = 0
pins = [12,16,20,21]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT, initial = 0)
sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
             [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]
counter = 1
#stepper motor objects
#motorcw = stepper(sequence,state,pins,counter,1,0x48)
#motorccw = stepper(sequence,state,pins,counter,-1,0x48)
#motorcw.setup()
#motorccw.setup()
#variable to keep track of old angle
oldangle = int(0)
#motor = stepper(0x48)
try:
    i = 1
    motorcw = stepper(sequence,state,pins,counter,1,0x48)
    motorccw = stepper(sequence,state,pins,counter,-1,0x48)
    motorcw.setup()
    motorccw.setup()

    while True:
        with open("Lab5.txt","r") as f:
            data = json.load(f)
        newangle = int(data["newangle"])
        #print(newangle)
        if newangle == int(0) and i == 1:
            motorcw.zero()
        #elif newangle == int() and i!=1:
        #    motorcw.zero()
            #pass      
        else:
            if oldangle < newangle:
                if abs(oldangle - newangle) < 180:
                    motorcw.goAngle(abs(oldangle-newangle))
                    #motor.goAngle(abs(oldangle-newangle),1)
                    oldangle = int(newangle)
                    #rotate clockwise assuming that clockwise is towards larger values
                    #old angle equals new anlgle
                else:
                    motorccw.goAngle((360-abs(oldangle-newangle)))
                    #motor.goAngle(abs(oldangle-newangle),-1)
                    oldangle = int(newangle)
                    #rotate ccw
                    #oldangle = new angle
            elif oldangle > newangle:
                if abs(oldangle - newangle) < 180:
                    motorccw.goAngle(abs(oldangle-newangle))
                    #motor.goAngle(abs(oldangle-newangle),-1)
                    oldangle = int(newangle)
                    #rotate ccw
                    #old angle = new angle
                else:
                    motorcw.goAngle((360-abs(oldangle-newangle)))
                    #motor.goAngle(abs(oldangle-newangle),1)
                    #oldangle = newangle
                    #rotate cw
                    oldangle = int(newangle)
        i += 1
        #print(oldangle,newangle,i)
            #elif newangle == 0:
            #    motorcw.zero()
                #do nothing sinc ethe two angles are the same
                #pass
except:
    GPIO.cleanup()
