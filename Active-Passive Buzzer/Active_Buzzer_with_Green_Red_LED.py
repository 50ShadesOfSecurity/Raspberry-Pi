"""
When Buzzer is ON, Green LED is ON and Red LED is OFF.
When Buzzer is OFF, Green LED is OFF and Red LED is ON.
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

redPin = 11
greenPin = 12
buzzerPin = 15

GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(buzzerPin,GPIO.OUT)

try:
    while True:
        GPIO.output(greenPin,1)
        GPIO.output(buzzerPin,1)
        GPIO.output(redPin,0)
        time.sleep(0.5)
        
        GPIO.output(greenPin,0)
        GPIO.output(buzzerPin,0)
        GPIO.output(redPin,1)
        time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
