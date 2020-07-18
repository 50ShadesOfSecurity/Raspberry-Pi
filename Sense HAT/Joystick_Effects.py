from sense_hat import SenseHat
import time
import random

sense = SenseHat()

def arrow():
    e = [0,0,0]
    r = [255,0,0]
    image = [
        r,e,e,e,e,e,e,e,
        e,r,e,e,e,e,e,e,
        e,e,r,e,e,e,e,e,
        e,e,e,r,e,e,e,e,
        e,e,e,e,r,e,e,r,
        e,e,e,e,e,r,e,r,
        e,e,e,e,e,e,r,r,
        e,e,e,e,r,r,r,r
        ]
    sense.set_pixels(image)
    
def effects(num):
    if(num==0):
        pass
    elif(num==1):
        e = [0,0,0]
        r = [255,0,0]
        g = [0,255,0]
        b = [0,0,255]
        y = [255,255,0]
        image = [
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,r,r,e,e,e,
            e,e,e,r,r,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e
            ]
        sense.set_pixels(image)
        time.sleep(0.25)
        image = [
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,g,g,g,g,e,e,
            e,e,g,e,e,g,e,e,
            e,e,g,e,e,g,e,e,
            e,e,g,g,g,g,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e
            ]
        sense.set_pixels(image)
        time.sleep(0.25)
        image = [
            e,e,e,e,e,e,e,e,
            e,b,b,b,b,b,b,e,
            e,b,e,e,e,e,b,e,
            e,b,e,e,e,e,b,e,
            e,b,e,e,e,e,b,e,
            e,b,e,e,e,e,b,e,
            e,b,b,b,b,b,b,e,
            e,e,e,e,e,e,e,e
            ]
        sense.set_pixels(image)
        time.sleep(0.25)
        image = [
            y,y,y,y,y,y,y,y,
            y,e,e,e,e,e,e,y,
            y,e,e,e,e,e,e,y,
            y,e,e,e,e,e,e,y,
            y,e,e,e,e,e,e,y,
            y,e,e,e,e,e,e,y,
            y,e,e,e,e,e,e,y,
            y,y,y,y,y,y,y,y
            ]
        sense.set_pixels(image)
        time.sleep(0.25)
    elif(num==2):
        i = 1
        while i<=4:
            x1 = random.randint(0,7)
            y1 = random.randint(0,7)
            x2 = random.randint(0,7)
            y2 = random.randint(0,7)
            x3 = random.randint(0,7)
            y3 = random.randint(0,7)
            x4 = random.randint(0,7)
            y4 = random.randint(0,7)
            sense.set_pixel(x1,y1,255,0,0)
            time.sleep(0.125)
            sense.set_pixel(x2,y2,0,255,0)
            time.sleep(0.125)
            sense.set_pixel(x1,y1,0,0,0)
            sense.set_pixel(x2,y2,0,0,0)
            sense.set_pixel(x3,y3,0,0,255)
            time.sleep(0.125)
            sense.set_pixel(x4,y4,255,255,0)
            time.sleep(0.125)
            sense.set_pixel(x3,y3,0,0,0)
            sense.set_pixel(x4,y4,0,0,0)
            i = i + 1
    elif(num==3):
        e = [0,0,0]
        r = [255,0,0]
        image = [
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,r,r,e,e,r,r,e,
            e,r,r,r,r,r,r,e,
            e,r,r,r,r,r,r,e,
            e,e,r,r,r,r,e,e,
            e,e,e,r,r,e,e,e,
            e,e,e,e,e,e,e,e
            ]
        sense.set_pixels(image)
        time.sleep(0.5)
        image = [
            e,e,e,e,e,e,e,e,
            r,r,e,e,e,e,r,r,
            r,r,r,e,e,r,r,r,
            r,r,r,r,r,r,r,r,
            r,r,r,r,r,r,r,r,
            e,r,r,r,r,r,r,e,
            e,e,r,r,r,r,e,e,
            e,e,e,r,r,e,e,e
            ]
        sense.set_pixels(image)
        time.sleep(0.5)
    elif(num==4):
        e = [0,0,0]
        g = [0,255,0]
        image = [
            e,g,e,e,e,e,g,e,
            e,e,g,e,e,g,e,e,
            e,e,g,g,g,g,e,e,
            e,g,g,g,g,g,g,e,
            g,g,e,g,g,e,g,g,
            g,g,g,g,g,g,g,g,
            g,e,g,e,e,g,e,g,
            e,e,e,e,e,e,e,e
            ]
        sense.set_pixels(image)
        time.sleep(0.5)
        image = [
            e,e,e,e,e,e,e,e,
            e,g,e,e,e,e,g,e,
            e,e,g,e,e,g,e,e,
            e,e,g,g,g,g,e,e,
            e,g,g,g,g,g,g,e,
            g,g,e,g,g,e,g,g,
            g,g,g,g,g,g,g,g,
            g,e,g,e,e,g,e,g
            ]
        sense.set_pixels(image)
        time.sleep(0.5)

try:
    print('\n\t[*] Use Joystick to change effects randomly. Next effect will take place after previous one is finished.\n')
    arrow()
    num = 0
    while True:
        effects(num)
        event = sense.stick.get_events()
        #print('\t->\tDirection: {}\tAction: {}'.format(event.direction,event.action))
        if(event):
            sense.clear()
            for i in event:
                if i.direction in ["right","left","up","down","middle"] and i.action in ["pressed"]:
                    num = random.randint(1,4)
                    if(num==1):
                        print('\n\t\t[*] Playing Colourful Blocks Effect (1-way)')
                    elif(num==2):
                        print('\n\t\t[*] Playing Random Colourful Pixels Effect')
                    elif(num==3):
                        print('\n\t\t[*] Playing Hearbeat Effect')
                    elif(num==4):
                        print('\n\t\t[*] Playing Green Skull Effect')
                else:
                    pass
except KeyboardInterrupt:
    print('\n\n\t [*] Keyboard Interrupt. Aborting !!!\n')
    sense.clear()