# Play Active Buzzer Tone

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

buzzerPin = 12

GPIO.setup(buzzerPin,GPIO.OUT)

try:
    while True:
        GPIO.output(buzzerPin,0)
        time.sleep(1)
        GPIO.output(buzzerPin,1)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()