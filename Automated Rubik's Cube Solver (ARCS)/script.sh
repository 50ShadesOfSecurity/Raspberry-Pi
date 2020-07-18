if [ -f ~/Desktop/moves.txt ]
	then	echo -e 'import RPi.GPIO as GPIO\nimport time\n\ndelay = 0.003\nsteps = 50\n\nGPIO.setmode(GPIO.BOARD)\nGPIO.setwarnings(False)\n\nenable_m1a = 15\nenable_m1b = 16\n\nGPIO.setup(enable_m1a, GPIO.OUT)\nGPIO.setup(enable_m1b, GPIO.OUT)\n\nenable_m2a = 18\nenable_m2b = 22\n\nGPIO.setup(enable_m2a, GPIO.OUT)\nGPIO.setup(enable_m2b, GPIO.OUT)\n\nenable_m3a = 29\nenable_m3b = 31\n\nGPIO.setup(enable_m3a, GPIO.OUT)\nGPIO.setup(enable_m3b, GPIO.OUT)\n\nenable_m4a = 32\nenable_m4b = 33\n\nGPIO.setup(enable_m4a, GPIO.OUT)\nGPIO.setup(enable_m4b, GPIO.OUT)\n\ncoil_A_1_pin = 7\ncoil_A_2_pin = 11\ncoil_B_1_pin = 12\ncoil_B_2_pin = 13\n\nGPIO.setup(coil_A_1_pin, GPIO.OUT)\nGPIO.setup(coil_A_2_pin, GPIO.OUT)\nGPIO.setup(coil_B_1_pin, GPIO.OUT)\nGPIO.setup(coil_B_2_pin, GPIO.OUT)\n\ndef setStep(w1, w2, w3, w4):\n\tGPIO.output(coil_A_1_pin, w1)\n\tGPIO.output(coil_A_2_pin, w2)\n\tGPIO.output(coil_B_1_pin, w3)\n\tGPIO.output(coil_B_2_pin, w4)\n' >> ~/Desktop/final_program.py;
				count=1;
		while :
			do	if [ $(wc -l moves.txt | head -c $count | tail -c 1) =   ]
					then	break;
				fi
				let count+=1;
			done
		count=`expr $count - 1`;
		count=$(wc -l moves.txt | head -c $count);
		for (( limit=1; limit<=$count; limit++ ))
			do	char=$(head -n $limit moves.txt | tail -n 1)
				case "$char" in
					R2) echo -e 'GPIO.output(enable_m3a, 1)\nGPIO.output(enable_m3b, 1)\n\nfor i in range(0, steps):\n\tsetStep(1,0,0,0)\n\ttime.sleep(delay)\n\tsetStep(0,1,0,0)\n\ttime.sleep(delay)\n\tsetStep(0,0,1,0)\n\ttime.sleep(delay)\n\tsetStep(0,0,0,1)\n\ttime.sleep(delay)\n\nGPIO.output(enable_m3a, 0)\nGPIO.output(enable_m3b, 0)' >> ~/Desktop/final_program.py;
						;;
					Ri2) echo -e 'GPIO.output(enable_m3a, 1)\nGPIO.output(enable_m3b, 1)\n\nfor i in range(0, steps):\n\tsetStep(0,0,0,1)\n\ttime.sleep(delay)\n\tsetStep(0,0,1,0)\n\ttime.sleep(delay)\n\tsetStep(0,1,0,0)\n\ttime.sleep(delay)\n\tsetStep(1,0,0,0)\n\ttime.sleep(delay)\n\nGPIO.output(enable_m3a, 0)\nGPIO.output(enable_m3b, 0)' >> ~/Desktop/final_program.py;
						;;
					L2) echo -e 'GPIO.output(enable_m1a, 1)\nGPIO.output(enable_m1b, 1)\n\nfor i in range(0, steps):\n\tsetStep(1,0,0,0)\n\ttime.sleep(delay)\n\tsetStep(0,1,0,0)\n\ttime.sleep(delay)\n\tsetStep(0,0,1,0)\n\ttime.sleep(delay)\n\tsetStep(0,0,0,1)\n\ttime.sleep(delay)\n\nGPIO.output(enable_m1a, 0)\nGPIO.output(enable_m1b, 0)' >> ~/Desktop/final_program.py;
						;;
					Li2) echo -e 'GPIO.output(enable_m1a, 1)\nGPIO.output(enable_m1b, 1)\n\nfor i in range(0, steps):\n\tsetStep(0,0,0,1)\n\ttime.sleep(delay)\n\tsetStep(0,0,1,0)\n\ttime.sleep(delay)\n\tsetStep(0,1,0,0)\n\ttime.sleep(delay)\n\tsetStep(1,0,0,0)\n\ttime.sleep(delay)\n\nGPIO.output(enable_m1a, 0)\nGPIO.output(enable_m1b, 0)' >> ~/Desktop/final_program.py;
						;;
					F2) echo -e 'GPIO.output(enable_m4a, 1)\nGPIO.output(enable_m4b, 1)\n\nfor i in range(0, steps):\n\tsetStep(1,0,0,0)\n\ttime.sleep(delay)\n\tsetStep(0,1,0,0)\n\ttime.sleep(delay)\n\tsetStep(0,0,1,0)\n\ttime.sleep(delay)\n\tsetStep(0,0,0,1)\n\ttime.sleep(delay)\n\nGPIO.output(enable_m4a, 0)\nGPIO.output(enable_m4b, 0)' >> ~/Desktop/final_program.py;
						;;
					Fi2) echo -e 'GPIO.output(enable_m4a, 1)\nGPIO.output(enable_m4b, 1)\n\nfor i in range(0, steps):\n\tsetStep(0,0,0,1)\n\ttime.sleep(delay)\n\tsetStep(0,0,1,0)\n\ttime.sleep(delay)\n\tsetStep(0,1,0,0)\n\ttime.sleep(delay)\n\tsetStep(1,0,0,0)\n\ttime.sleep(delay)\n\nGPIO.output(enable_m4a, 0)\nGPIO.output(enable_m4b, 0)' >> ~/Desktop/final_program.py;
						;;
					B2) echo -e 'GPIO.output(enable_m2a, 1)\nGPIO.output(enable_m2b, 1)\n\nfor i in range(0, steps):\n\tsetStep(1,0,0,0)\n\ttime.sleep(delay)\n\tsetStep(0,1,0,0)\n\ttime.sleep(delay)\n\tsetStep(0,0,1,0)\n\ttime.sleep(delay)\n\tsetStep(0,0,0,1)\n\ttime.sleep(delay)\n\nGPIO.output(enable_m2a, 0)\nGPIO.output(enable_m2b, 0)' >> ~/Desktop/final_program.py;
						;;
					Bi2) echo -e 'GPIO.output(enable_m2a, 1)\nGPIO.output(enable_m2b, 1)\n\nfor i in range(0, steps):\n\tsetStep(0,0,0,1)\n\ttime.sleep(delay)\n\tsetStep(0,0,1,0)\n\ttime.sleep(delay)\n\tsetStep(0,1,0,0)\n\ttime.sleep(delay)\n\tsetStep(1,0,0,0)\n\ttime.sleep(delay)\n\nGPIO.output(enable_m2a, 0)\nGPIO.output(enable_m2b, 0)' >> ~/Desktop/final_program.py;
						;;
				esac
			done
fi
sudo python ~/Desktop/final_program.py