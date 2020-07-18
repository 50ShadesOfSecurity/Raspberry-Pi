from sense_hat import SenseHat
import time
import random

sense = SenseHat()

try:
    e = [0,0,0]
    c = [255,0,0]
    small = [
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        e,c,c,e,e,c,c,e,
        e,c,c,c,c,c,c,e,
        e,c,c,c,c,c,c,e,
        e,e,c,c,c,c,e,e,
        e,e,e,c,c,e,e,e,
        e,e,e,e,e,e,e,e
        ]
    big = [
        e,e,e,e,e,e,e,e,
        c,c,e,e,e,e,c,c,
        c,c,c,e,e,c,c,c,
        c,c,c,c,c,c,c,c,
        c,c,c,c,c,c,c,c,
        e,c,c,c,c,c,c,e,
        e,e,c,c,c,c,e,e,
        e,e,e,c,c,e,e,e
        ]
    print('\n\t[*] Use Joystick to change orientation of the heart or to change its color.\n')
    colour = 1  # 1-Red, 2-Green, 3-Blue, 4-White, 5-Orange, 6-Yellow, 7-Indigo, 8-Violet
    while True:
        sense.set_pixels(small)
        time.sleep(0.5)
        sense.set_pixels(big)
        time.sleep(0.5)
        event = sense.stick.get_events()
        if(event):
            for i in event:
                if i.direction in ["right"] and i.action in ["pressed"]:
                    sense.set_rotation(270)
                elif i.direction in ["left"] and i.action in ["pressed"]:
                    sense.set_rotation(90)
                elif i.direction in ["up"] and i.action in ["pressed"]:
                    sense.set_rotation(180)
                elif i.direction in ["down"] and i.action in ["pressed"]:
                    sense.set_rotation(0)
                elif i.direction in ["middle"] and i.action in ["pressed"]:
                    colour = random.randint(1,8)
                    if(colour==1):
                        c = [255,0,0]
                    elif(colour==2):
                        c = [0,255,0]
                    elif(colour==3):
                        c = [0,0,255]
                    elif(colour==4):
                        c = [255,255,255]
                    elif(colour==5):
                        c = [255,127,0]
                    elif(colour==6):
                        c = [255,255,0]
                    elif(colour==7):
                        c = [75,0,130]
                    else:
                        c = [159,0,255]
                    e = [0,0,0]
                    small = [
                        e,e,e,e,e,e,e,e,
                        e,e,e,e,e,e,e,e,
                        e,c,c,e,e,c,c,e,
                        e,c,c,c,c,c,c,e,
                        e,c,c,c,c,c,c,e,
                        e,e,c,c,c,c,e,e,
                        e,e,e,c,c,e,e,e,
                        e,e,e,e,e,e,e,e
                        ]
                    big = [
                        e,e,e,e,e,e,e,e,
                        c,c,e,e,e,e,c,c,
                        c,c,c,e,e,c,c,c,
                        c,c,c,c,c,c,c,c,
                        c,c,c,c,c,c,c,c,
                        e,c,c,c,c,c,c,e,
                        e,e,c,c,c,c,e,e,
                        e,e,e,c,c,e,e,e
                        ]
                else:
                    pass
except KeyboardInterrupt:
    print('\n\n\t [*] Keyboard Interrupt. Aborting !!!\n')
    sense.clear()
    time.sleep(1)