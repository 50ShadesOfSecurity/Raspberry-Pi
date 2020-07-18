#	For Gripper and Wheel
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)	#	M1_EN
GPIO.setup(11,GPIO.OUT)	#	M1
GPIO.setup(12,GPIO.OUT)	#	OUT

GPIO.setup(13,GPIO.OUT)	#	M2_EN
GPIO.setup(15,GPIO.OUT)	#	M2
GPIO.setup(16,GPIO.OUT)	#	OUT

GPIO.output(7,True)
GPIO.output(13,True)

try:
	while True:
		GPIO.output(11,True)
		GPIO.output(12,False)
		time.sleep(0.5)
		GPIO.output(11,False)
		GPIO.output(12,True)
		time.sleep(0.5)
		GPIO.output(11,True)
		GPIO.output(12,False)
		time.sleep(0.5)
		GPIO.output(11,False)
		GPIO.output(12,True)
		time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()