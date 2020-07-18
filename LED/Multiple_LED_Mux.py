#	Program to blink 8 LEDs sequentially using M74HC238 demultiplexer (3-to-8 line decoder).

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)	#	G2A
GPIO.setup(11,GPIO.OUT)	#	G2B
GPIO.setup(12,GPIO.OUT)	#	G1

GPIO.setup(13,GPIO.OUT)	#	A
GPIO.setup(15,GPIO.OUT)	#	B
GPIO.setup(16,GPIO.OUT)	#	C

#	All output pins work when both G2A & G2B are LOW and G1 is HIGH.
GPIO.output(7,0)
GPIO.output(11,0)
GPIO.output(12,1)

GPIO.output(13,1)
GPIO.output(15,0)
GPIO.output(16,1)
time.sleep(5)

GPIO.cleanup()
