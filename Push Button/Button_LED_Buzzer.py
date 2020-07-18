import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

redPin = 11
greenPin = 12
buzzerPin = 15
buttonPin = 16
flag1 = False
flag2 = True

GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(buzzerPin,GPIO.OUT)
GPIO.setup(buttonPin,GPIO.IN)

try:
    while True: 
        # When button is pressed, turn Green Pin and Buzzer ON and Red Pin OFF.
        # When button is released, turn Green Pin and Buzzer OFF and Red Pin ON.
        
        if(GPIO.input(buttonPin)==GPIO.LOW):
            GPIO.output(greenPin,1)
            GPIO.output(buzzerPin,1)
            GPIO.output(redPin,0)
        else:
            GPIO.output(greenPin,0)
            GPIO.output(buzzerPin,0)
            GPIO.output(redPin,1)
        

        # When button is pressed once, toggle Green Pin and Buzzer ON and Red Pin OFF.
        # When button is pressed again, toggle Green Pin and Buzzer OFF and Red Pin ON.
        """
        if (GPIO.input(buttonPin)==GPIO.LOW):
            while(GPIO.input(buttonPin)==GPIO.LOW):
                pass
            flag1 = not flag1;
            flag2 = not flag2;
            GPIO.output(greenPin,flag1)
            GPIO.output(buzzerPin,flag1)
            GPIO.output(redPin,flag2)
        """
except KeyboardInterrupt:
    GPIO.cleanup()
