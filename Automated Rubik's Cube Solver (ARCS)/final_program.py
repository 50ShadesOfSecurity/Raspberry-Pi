import RPi.GPIO as GPIO
import time

delay = 0.003
steps = 100
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

enable_m1a = 15
enable_m1b = 16

GPIO.setup(enable_m1a, GPIO.OUT)
GPIO.setup(enable_m1b, GPIO.OUT)

enable_m2a = 18
enable_m2b = 22

GPIO.setup(enable_m2a, GPIO.OUT)
GPIO.setup(enable_m2b, GPIO.OUT)

enable_m3a = 29
enable_m3b = 31

GPIO.setup(enable_m3a, GPIO.OUT)
GPIO.setup(enable_m3b, GPIO.OUT)

enable_m4a = 32
enable_m4b = 33

GPIO.setup(enable_m4a, GPIO.OUT)
GPIO.setup(enable_m4b, GPIO.OUT)

coil_A_1_pin = 7
coil_A_2_pin = 11
coil_B_1_pin = 12
coil_B_2_pin = 13

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

def setStep(w1, w2, w3, w4):
 	GPIO.output(coil_A_1_pin, w1)
 	GPIO.output(coil_A_2_pin, w2)
 	GPIO.output(coil_B_1_pin, w3)
 	GPIO.output(coil_B_2_pin, w4)

GPIO.output(enable_m1a, 1)
GPIO.output(enable_m1b, 1)

for i in range(0, steps):
	setStep(1,0,0,0)
	time.sleep(delay)
	setStep(0,1,0,0)
	time.sleep(delay)
	setStep(0,0,1,0)
	time.sleep(delay)
	setStep(0,0,0,1)
	time.sleep(delay)

GPIO.output(enable_m1a, 0)
GPIO.output(enable_m1b, 0)

GPIO.output(enable_m2a, 1)
GPIO.output(enable_m2b, 1)

for i in range(0, steps):
	setStep(1,0,0,0)
	time.sleep(delay)
	setStep(0,1,0,0)
	time.sleep(delay)
	setStep(0,0,1,0)
	time.sleep(delay)
	setStep(0,0,0,1)
	time.sleep(delay)

GPIO.output(enable_m2a, 0)
GPIO.output(enable_m2b, 0)

GPIO.output(enable_m3a, 1)
GPIO.output(enable_m3b, 1)

for i in range(0, steps):
	setStep(1,0,0,0)
	time.sleep(delay)
	setStep(0,1,0,0)
	time.sleep(delay)
	setStep(0,0,1,0)
	time.sleep(delay)
	setStep(0,0,0,1)
	time.sleep(delay)

GPIO.output(enable_m3a, 0)
GPIO.output(enable_m3b, 0)

GPIO.output(enable_m4a, 1)
GPIO.output(enable_m4b, 1)

for i in range(0, steps):
	setStep(1,0,0,0)
	time.sleep(delay)
	setStep(0,1,0,0)
	time.sleep(delay)
	setStep(0,0,1,0)
	time.sleep(delay)
	setStep(0,0,0,1)
	time.sleep(delay)

GPIO.output(enable_m4a, 0)
GPIO.output(enable_m4b, 0)

GPIO.cleanup()
