from sense_hat import SenseHat
import time
import random

sense = SenseHat()

def base():
    r = [255,0,0]
    e = [0,0,0]
    image = [
            r,e,e,e,e,e,e,r,
            e,r,e,e,e,e,r,e,
            e,e,r,e,e,r,e,e,
            e,e,e,r,r,e,e,e,
            e,e,e,r,r,e,e,e,
            e,e,r,e,e,r,e,e,
            e,r,e,e,e,e,r,e,
            r,e,e,e,e,e,e,r
            ]
    sense.set_pixels(image)

try:
    base()
    print('\n\t[*] Use Joystick to start the counter.\n')
    counter = 0
    rightFlag = 0
    leftFlag = 0
    pointer = 0
    colour = [255,0,0]
    colour_flag = 1 # 1-Red, 2-Green, 3-Blue, 4-White, 5-Orange, 6-Yellow, 7-Indigo, 8-Violet
    while True:
        event = sense.stick.wait_for_event()
        #print('\t->\tDirection: {}\tAction: {}'.format(event.direction,event.action))
        if event.direction in ["right", "up"] and event.action in ["pressed"]:
            if(rightFlag>=0 and rightFlag<=9):
                pointer = rightFlag
                sense.show_letter(str(pointer),text_colour=colour)
                rightFlag = pointer + 1
                leftFlag = pointer - 1
            else:
                pointer = 0
                sense.show_letter(str(pointer),text_colour=colour)
                rightFlag = pointer + 1
                leftFlag = 9
        elif event.direction in ["left", "down"] and event.action in ["pressed"]:
            if(leftFlag>=0 and leftFlag<=9):
                pointer = leftFlag
                sense.show_letter(str(pointer),text_colour=colour)
                rightFlag = pointer + 1
                leftFlag = pointer - 1
            else:
                pointer = 9
                sense.show_letter(str(pointer),text_colour=colour)
                rightFlag = 0
                leftFlag = pointer - 1
        elif event.direction in ["middle"] and event.action in ["pressed"]:
            colour_flag = random.randint(1,8)
            if(colour_flag==1):
                colour = [255,0,0]
            elif(colour_flag==2):
                colour = [0,255,0]
            elif(colour_flag==3):
                colour = [0,0,255]
            elif(colour_flag==4):
                colour = [255,255,255]
            elif(colour_flag==5):
                colour = [255,127,0]
            elif(colour_flag==6):
                colour = [255,255,0]
            elif(colour_flag==7):
                colour = [75,0,130]
            else:
                colour = [159,0,255]
            sense.show_letter(str(pointer),text_colour=colour)
        else:
            pass
except KeyboardInterrupt:
    print('\n\n\t [*] Keyboard Interrupt. Aborting !!!\n')
    sense.clear()
    time.sleep(1)