#	Basic DC Motor Program

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)	#	M1_EN
GPIO.setup(11,GPIO.OUT)	#	M1
GPIO.setup(12,GPIO.OUT)	#	Out

GPIO.output(7,True)

try:
	while True:
		GPIO.output(11,True)
		GPIO.output(12,False)
		time.sleep(2)
		GPIO.output(11,False)
		GPIO.output(12,False)
		time.sleep(1)
		GPIO.output(11,False)
		GPIO.output(12,True)
		time.sleep(2)
		GPIO.output(11,False)
		GPIO.output(12,False)
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()