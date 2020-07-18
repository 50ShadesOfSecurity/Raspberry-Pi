import RPi.GPIO as GPIO
import time, datetime

now = datetime.datetime.now()

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
 #GPIO ports for the 7seg pins
segment8 =  [21,22,23,24,26,29,31,32]

for segment in segment8:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)
 
    #Digit 1
    GPIO.setup(33, GPIO.OUT)
    GPIO.output(33, 0) #Off initially
    #Digit 2
    GPIO.setup(35, GPIO.OUT)
    GPIO.output(35, 0) #Off initially
    #Digit 3
    GPIO.setup(36, GPIO.OUT)
    GPIO.output(36, 0) #Off initially
    #Digit 4
    GPIO.setup(37, GPIO.OUT)
    GPIO.output(37, 0) #Off initially

null = [0,0,0,0,0,0,0]
zero = [1,1,1,1,1,1,0]
one = [0,1,1,0,0,0,0]
two = [1,1,0,1,1,0,1]
three = [1,1,1,1,0,0,1]
four = [0,1,1,0,0,1,1]
five = [1,0,1,1,0,1,1]
six = [1,0,1,1,1,1,1]
seven = [1,1,1,0,0,0,0]
eight = [1,1,1,1,1,1,1]
nine = [1,1,1,1,0,1,1]

def print_segment(charector):
    if charector == 1:
        for i in range(7):
            GPIO.output(segment8[i], one[i])

    if charector == 2:
        for i in range(7):
            GPIO.output(segment8[i], two[i])

    if charector == 3:
        for i in range(7):
            GPIO.output(segment8[i], three[i])

    if charector == 4:
        for i in range(7):
            GPIO.output(segment8[i], four[i])

    if charector == 5:
        for i in range(7):
            GPIO.output(segment8[i], five[i])

    if charector == 6:
        for i in range(7):
            GPIO.output(segment8[i], six[i])

    if charector == 7:
        for i in range(7):
            GPIO.output(segment8[i], seven[i])

    if charector == 8:
        for i in range(7):
            GPIO.output(segment8[i], eight[i])

    if charector == 9:
        for i in range(7):
            GPIO.output(segment8[i], nine[i])

    if charector == 0:
        for i in range(7):
            GPIO.output(segment8[i], zero[i])        
            
    return;

while 1:

    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    h1 = hour/10
    h2 = hour % 10
    m1 = minute /10
    m2 = minute % 10
    print (h1,h2,m1,m2)

  
    delay_time = 0.001 #delay to create virtual effect
    
    
    GPIO.output(33, 1) #Turn on Digit One
    print_segment (h1) #Print h1 on segment
    time.sleep(delay_time)
    GPIO.output(33, 0) #Turn off Digit One

    GPIO.output(35, 1) #Turn on Digit One
    print_segment (h2) #Print h1 on segment
    GPIO.output(32, 1) #Display point On
    time.sleep(delay_time)
    GPIO.output(32, 0) #Display point Off
    GPIO.output(35, 0) #Turn off Digit One

    GPIO.output(36, 1) #Turn on Digit One
    print_segment (m1) #Print h1 on segment
    time.sleep(delay_time)
    GPIO.output(36, 0) #Turn off Digit One

    GPIO.output(37, 1) #Turn on Digit One
    print_segment (m2) #Print h1 on segment
    time.sleep(delay_time)
    GPIO.output(37, 0) #Turn off Digit One
 
    #time.sleep(1)