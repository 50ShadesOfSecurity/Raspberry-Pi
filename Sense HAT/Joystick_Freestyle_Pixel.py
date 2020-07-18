from sense_hat import SenseHat
import time
import random

sense = SenseHat()

try:
    x = 4
    y = 4
    colour = [255,0,0]
    colour_count = 1    # 1-Red, 2-Green, 3-Blue, 4-White, 5-Orange, 6-Yellow, 7-Indigo, 8-Violet
    sense.set_pixel(x,y,colour)
    print('\n\t[*] Use Joystick to move the pixel freely across LED matrix or to change its color.\n')
    while True:
        event = sense.stick.wait_for_event()
        #print('\t->\tDirection: {}\tAction: {}'.format(event.direction,event.action))
        sense.set_pixel(x,y,0,0,0)
        if event.direction in ["right"] and event.action in ["pressed"]:
            if(x==7):
                x = 0
            else:
                x = x + 1
        elif event.direction in ["left"] and event.action in ["pressed"]:
            if(x==0):
                x = 7
            else:
                x = x - 1
        elif event.direction in ["up"] and event.action in ["pressed"]:
            if(y==0):
                y = 7
            else:
                y = y - 1
        elif event.direction in ["down"] and event.action in ["pressed"]:
            if(y==7):
                y = 0
            else:
                y = y + 1
        elif event.direction in ["middle"] and event.action in ["pressed"]:
            colour_count = random.randint(1,8)
            if(colour_count==1):
                colour = [255,0,0]
            elif(colour_count==2):
                colour = [0,255,0]
            elif(colour_count==3):
                colour = [0,0,255]
            elif(colour_count==4):
                colour = [255,255,255]
            elif(colour_count==5):
                colour = [255,127,0]
            elif(colour_count==6):
                colour = [255,255,0]
            elif(colour_count==7):
                colour = [75,0,130]
            else:
                colour = [159,0,255]
        else:
            pass
        sense.set_pixel(x,y,colour)
except KeyboardInterrupt:
    print('\n\n\t [*] Keyboard Interrupt. Aborting !!!\n')
    sense.clear()