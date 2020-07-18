#	Single phase stepper motor program
#	NEMA 17 1.8 degree standard bipolar stepper motor

import RPi.GPIO as GPIO
import time

# Variables

delay = 0.003
steps = 50	# 90 degree rotation
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Enable GPIO pins for  ENA and ENB for stepper

enable_a = 3
enable_b = 13

# Enable pins for IN1-4 to control step sequence

coil_A_1_pin = 11
coil_A_2_pin = 12
coil_B_1_pin = 15
coil_B_2_pin = 16

# Set pin states

GPIO.setup(enable_a, GPIO.OUT)
GPIO.setup(enable_b, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

# Set ENA and ENB to high to enable stepper

GPIO.output(enable_a, 1)
GPIO.output(enable_b, 1)

# Function for step sequence

def setStep(w1, w2, w3, w4):
 	GPIO.output(coil_A_1_pin, w1)
 	GPIO.output(coil_A_2_pin, w2)
 	GPIO.output(coil_B_1_pin, w3)
 	GPIO.output(coil_B_2_pin, w4)

# loop through step sequence based on number of steps
# full stepping single phase

for i in range(0, steps):
	setStep(1,0,0,0)
	time.sleep(delay)
	setStep(0,1,0,0)
	time.sleep(delay)
	setStep(0,0,1,0)
	time.sleep(delay)
	setStep(0,0,0,1)
	time.sleep(delay)

# Reverse previous step sequence to reverse motor direction
for i in range(0, steps):
	setStep(0,0,0,1)
	time.sleep(delay)
	setStep(0,0,1,0)
	time.sleep(delay)
	setStep(0,1,0,0)
	time.sleep(delay)
	setStep(1,0,0,0)
	time.sleep(delay)
GPIO.cleanup()
