import RPi.GPIO as GPIO
import time
from PCF8591 import ADC

    
GPIO.setmode(GPIO.BCM)
#stepper class
class stepper:
    def __init__(self,sequence,state,pins,counter,di,address):
        self.sequence = sequence
        self.state = state
        self.pins = pins
        self.counter = counter
        self.di = di
        self.ledread = ADC(address)
    def setup(self):  #function to set up pins
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT, initial=0)
        GPIO.setup(26, GPIO.OUT, initial = 0)
        
    def delay_us(self,tus): # use microseconds to improve time resolution
        endTime = time.time() + float(tus)/ float(1E6)
        while time.time() < endTime:
            pass

    def halfstep(self): #turn certain number of half steps
        # dir = -/+ 1 (ccw / cw)
        for hstep in range(8):
            self.state += self.di
            if self.state > 7: self.state = 0
            elif self.state < 0: self.state =  7
            for pinx in range(4):    # 4 pins that need to be energized
                GPIO.output(self.pins[pinx], self.sequence[self.state][pinx])
            self.delay_us(1000)
    def moveSteps(self,steps):
        # move the actuation sequence a given number of half steps
        for step in range(steps):
            self.halfstep()

    def goAngle(self,angle): #go a certain angle
        steps = round(float(512) / float(360) * float(angle))
        self.moveSteps(steps)
    
    def zero(self): #zeroing function, 
        GPIO.output(26,1)
        time.sleep(3)
        while self.ledread.read(0) < 210:
            self.goAngle(1)
            self.counter += 1
            self.delay_us(10000)
        GPIO.output(26,0)
