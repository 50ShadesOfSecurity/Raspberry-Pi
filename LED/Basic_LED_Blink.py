# Blink LED 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ledPin = 12

GPIO.setup(ledPin,GPIO.OUT)

try:
    while True:
        GPIO.output(ledPin,0)
        time.sleep(1)
        GPIO.output(ledPin,1)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
