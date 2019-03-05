import RPi.GPIO as GPIO
import time

class DetectMotion:

    def __init__(self):
        self.pinIn = 11
        self.setupGPIO()
        self.out = GPIO.input(self.pinIn)

    def setupGPIO(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.pinIn, GPIO.IN)

    def observeRoom(self):
        if self.out == 1:
            print('DetectMotion')
            return self.out
