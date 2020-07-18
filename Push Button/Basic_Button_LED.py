import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ledPin = 11
buttonPin = 12

GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(buttonPin,GPIO.IN)

flag = False

try:
    while True:
        # When button is pressed, turn LED ON. When button is released, turn LED OFF.
        
        if(GPIO.input(buttonPin)==GPIO.LOW):
            GPIO.output(ledPin,1)
        else:
            GPIO.output(ledPin,0)
        
        # Press the Button to toggle LED (ON->OFF，OFF->ON).
        """
        if (GPIO.input(buttonPin)==GPIO.LOW):
            while(GPIO.input(buttonPin)==GPIO.LOW):
                pass
            flag = not flag
            GPIO.output(ledPin,flag)
        """
except KeyboardInterrupt:
    GPIO.cleanup()
