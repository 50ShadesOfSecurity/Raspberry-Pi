import RPi as GPIO
import time

GPIO.setmode(GPIO.BOARD)
ControlPin = [7,11,13,15]

for pin in ControlPin:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,0)

# Half Stepping
seq = [	[1,0,0,0],
        [1,1,0,0],
		[0,1,0,0],
		[0,1,1,0],
		[0,0,1,0],
		[0,0,1,1],
		[0,0,0,1],
		[1,0,0,1]
        ]

# Single Phase Stepping
#	seq = [	[1,0,0,0],
#			[0,1,0,0],
#			[0,0,1,0],
#			[0,0,0,1]
#           ]

# Full (Dual Phase) Stepping
#	seq = [	[1,1,0,0],
#		    [0,1,1,0],
#			[0,0,1,1],
#			[1,0,0,1]
#           ]

for i in range(512):
	for halfstep in range(8):
		for pin in range(4):
			GPIO.output(ControlPin[pin], seq[halfstep][pin])
			time.sleep(0.001)
GPIO.cleanup()