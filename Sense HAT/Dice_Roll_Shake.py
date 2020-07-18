from sense_hat import SenseHat
import time
import random

sense = SenseHat()

def base_r():
    r = [255,0,0]
    g = [0,255,0]
    b = [0,0,255]
    y = [255,255,0]
    w = [255,255,255]
    image = [
            r,r,r,w,w,g,g,g,
            r,r,r,w,g,g,g,g,
            r,r,r,w,w,g,g,g,
            w,r,w,w,w,w,w,w,
            w,w,w,w,w,w,b,w,
            y,y,y,w,w,b,b,b,
            y,y,y,y,w,b,b,b,
            y,y,y,w,w,b,b,b
            ]
    sense.set_pixels(image)

def base_y():
    r = [255,0,0]
    g = [0,255,0]
    b = [0,0,255]
    y = [255,255,0]
    w = [255,255,255]
    image = [
            y,y,y,w,w,r,r,r,
            y,y,y,w,r,r,r,r,
            y,y,y,w,w,r,r,r,
            w,y,w,w,w,w,w,w,
            w,w,w,w,w,w,g,w,
            b,b,b,w,w,g,g,g,
            b,b,b,b,w,g,g,g,
            b,b,b,w,w,g,g,g
            ]
    sense.set_pixels(image)

def base_b():
    r = [255,0,0]
    g = [0,255,0]
    b = [0,0,255]
    y = [255,255,0]
    w = [255,255,255]
    image = [
            b,b,b,w,w,y,y,y,
            b,b,b,w,y,y,y,y,
            b,b,b,w,w,y,y,y,
            w,b,w,w,w,w,w,w,
            w,w,w,w,w,w,r,w,
            g,g,g,w,w,r,r,r,
            g,g,g,g,w,r,r,r,
            g,g,g,w,w,r,r,r
            ]
    sense.set_pixels(image)
    
def base_g():
    r = [255,0,0]
    g = [0,255,0]
    b = [0,0,255]
    y = [255,255,0]
    w = [255,255,255]
    image = [
            g,g,g,w,w,b,b,b,
            g,g,g,w,b,b,b,b,
            g,g,g,w,w,b,b,b,
            w,g,w,w,w,w,w,w,
            w,w,w,w,w,w,y,w,
            r,r,r,w,w,y,y,y,
            r,r,r,r,w,y,y,y,
            r,r,r,w,w,y,y,y
            ]
    sense.set_pixels(image)

def dice(num):
    e = [0,0,0]
    r = [255,0,0]
    if(num==1):
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
    elif(num==2):
        image = [
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,r,r,e,e,e,e,
            e,e,r,r,e,e,e,e,
            e,e,e,e,r,r,e,e,
            e,e,e,e,r,r,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e
            ]
    elif(num==3):
        image = [
            e,e,e,e,e,e,e,e,
            e,r,r,e,e,e,e,e,
            e,r,r,e,e,e,e,e,
            e,e,e,r,r,e,e,e,
            e,e,e,r,r,e,e,e,
            e,e,e,e,e,r,r,e,
            e,e,e,e,e,r,r,e,
            e,e,e,e,e,e,e,e
            ]
    elif(num==4):
        image = [
            e,e,e,e,e,e,e,e,
            e,r,r,e,e,r,r,e,
            e,r,r,e,e,r,r,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,r,r,e,e,r,r,e,
            e,r,r,e,e,r,r,e,
            e,e,e,e,e,e,e,e
            ]
    elif(num==5):
        image = [
            e,e,e,e,e,e,e,e,
            e,r,r,e,e,r,r,e,
            e,r,r,e,e,r,r,e,
            e,e,e,r,r,e,e,e,
            e,e,e,r,r,e,e,e,
            e,r,r,e,e,r,r,e,
            e,r,r,e,e,r,r,e,
            e,e,e,e,e,e,e,e
            ]
    else:
        image = [
            e,r,r,e,e,r,r,e,
            e,r,r,e,e,r,r,e,
            e,e,e,e,e,e,e,e,
            e,r,r,e,e,r,r,e,
            e,r,r,e,e,r,r,e,
            e,e,e,e,e,e,e,e,
            e,r,r,e,e,r,r,e,
            e,r,r,e,e,r,r,e
            ]
    sense.set_pixels(image)

try:
    base_r()
    print('\n\t[*] Shake the Sense HAT to roll the dice.\n')
    while True:
        accel = sense.get_accelerometer_raw()
        
        x = abs(accel['x'])
        y = abs(accel['y'])
        z = abs(accel['z'])
        #print('X: {}, Y: {}, Z: {}'.format(x,y,z))
        
        if x > 2 or y > 2 or z > 2:
            time.sleep(0.5)
            base_r()
            time.sleep(0.25)
            base_y()
            time.sleep(0.25)
            base_b()
            time.sleep(0.25)
            base_g()
            time.sleep(0.25)
            dice(random.randint(1,6))
except KeyboardInterrupt:
    print('\n\n\t [*] Keyboard Interrupt. Aborting !!!\n')
    sense.clear()