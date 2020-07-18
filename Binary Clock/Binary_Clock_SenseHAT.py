from sense_hat import SenseHat
import time
import datetime

sense = SenseHat()

b = [0,0,255]
e = [0,0,0]
w = [255,255,255]

base = [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
e,e,e,e,e,e,e,e,
e,w,e,e,w,e,e,w,
e,w,e,w,w,e,w,w,
w,w,e,w,w,e,w,w,
w,w,e,w,w,e,w,w
]

print("\n [*] Starting Binary Clock on Sense HAT...\n")

try:
    while True:
        sense.set_pixels(base)
        
        current = datetime.datetime.now()
        
        hour = current.strftime("%H") # %H for 24-hour format, %I for 12-hour format
        minute = current.strftime("%M")
        second = current.strftime("%S")
        
        #print("\t Displaying: ", hour, ":", minute, ":", second)
        
        if hour in ['01']:
            sense.set_pixel(1,7,255,0,0)
        elif hour in ['02']:
            sense.set_pixel(1,6,255,0,0)
        elif hour in ['03']:
            sense.set_pixel(1,6,255,0,0)
            sense.set_pixel(1,7,255,0,0)
        elif hour in ['04']:
            sense.set_pixel(1,5,255,0,0)
        elif hour in ['05']:
            sense.set_pixel(1,5,255,0,0)
            sense.set_pixel(1,7,255,0,0)
        elif hour in ['06']:
            sense.set_pixel(1,5,255,0,0)
            sense.set_pixel(1,6,255,0,0)
        elif hour in ['07']:
            sense.set_pixel(1,5,255,0,0)
            sense.set_pixel(1,6,255,0,0)
            sense.set_pixel(1,7,255,0,0)
        elif hour in ['08']:
            sense.set_pixel(1,4,255,0,0)
        elif hour in ['09']:
            sense.set_pixel(1,4,255,0,0)
            sense.set_pixel(1,7,255,0,0)
        elif hour in ['10']:
            sense.set_pixel(0,7,255,0,0)
        elif hour in ['11']:
            sense.set_pixel(0,7,255,0,0)
            sense.set_pixel(1,7,255,0,0)
        elif hour in ['12']:
            sense.set_pixel(0,7,255,0,0)
            sense.set_pixel(1,6,255,0,0)
        elif hour in ['13']:
            sense.set_pixel(0,7,255,0,0)
            sense.set_pixel(1,6,255,0,0)
            sense.set_pixel(1,7,255,0,0)
        elif hour in ['14']:
            sense.set_pixel(0,7,255,0,0)
            sense.set_pixel(1,5,255,0,0)
        elif hour in ['15']:
            sense.set_pixel(0,7,255,0,0)
            sense.set_pixel(1,5,255,0,0)
            sense.set_pixel(1,7,255,0,0)
        elif hour in ['16']:
            sense.set_pixel(0,7,255,0,0)
            sense.set_pixel(1,5,255,0,0)
            sense.set_pixel(1,6,255,0,0)
        elif hour in ['17']:
            sense.set_pixel(0,7,255,0,0)
            sense.set_pixel(1,5,255,0,0)
            sense.set_pixel(1,6,255,0,0)
            sense.set_pixel(1,7,255,0,0)
        elif hour in ['18']:
            sense.set_pixel(0,7,255,0,0)
            sense.set_pixel(1,4,255,0,0)
        elif hour in ['19']:
            sense.set_pixel(0,7,255,0,0)
            sense.set_pixel(1,4,255,0,0)
            sense.set_pixel(1,7,255,0,0)
        elif hour in ['20']:
            sense.set_pixel(0,6,255,0,0)
        elif hour in ['21']:
            sense.set_pixel(0,6,255,0,0)
            sense.set_pixel(1,7,255,0,0)
        elif hour in ['22']:
            sense.set_pixel(0,6,255,0,0)
            sense.set_pixel(1,6,255,0,0)
        elif hour in ['23']:
            sense.set_pixel(0,6,255,0,0)
            sense.set_pixel(1,6,255,0,0)
            sense.set_pixel(1,7,255,0,0)
        
        if minute in ['01']:
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['02']:
            sense.set_pixel(4,6,255,0,0)
        elif minute in ['03']:
            sense.set_pixel(4,6,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['04']:
            sense.set_pixel(4,5,255,0,0)
        elif minute in ['05']:
            sense.set_pixel(4,5,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['06']:
            sense.set_pixel(4,5,255,0,0)
            sense.set_pixel(4,6,255,0,0)
        elif minute in ['07']:
            sense.set_pixel(4,5,255,0,0)
            sense.set_pixel(4,6,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['08']:
            sense.set_pixel(4,4,255,0,0)
        elif minute in ['09']:
            sense.set_pixel(4,4,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['10']:
            sense.set_pixel(3,7,255,0,0)
        elif minute in ['11']:
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['12']:
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,6,255,0,0)
        elif minute in ['13']:
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,6,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['14']:
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,5,255,0,0)
        elif minute in ['15']:
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,5,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['16']:
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,5,255,0,0)
            sense.set_pixel(4,6,255,0,0)
        elif minute in ['17']:
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,5,255,0,0)
            sense.set_pixel(4,6,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['18']:
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,4,255,0,0)
        elif minute in ['19']:
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,4,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['20']:
            sense.set_pixel(3,6,255,0,0)
        elif minute in ['21']:
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['22']:
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(4,6,255,0,0)
        elif minute in ['23']:
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(4,6,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['24']:
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(4,5,255,0,0)
        elif minute in ['25']:
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(4,5,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['26']:
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(4,5,255,0,0)
            sense.set_pixel(4,6,255,0,0)
        elif minute in ['27']:
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(4,5,255,0,0)
            sense.set_pixel(4,6,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['28']:
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(4,4,255,0,0)
        elif minute in ['29']:
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(4,4,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['30']:
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(3,7,255,0,0)
        elif minute in ['31']:
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['32']:
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,6,255,0,0)
        elif minute in ['33']:
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,6,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['34']:
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,5,255,0,0)
        elif minute in ['35']:
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,5,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['36']:
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,5,255,0,0)
            sense.set_pixel(4,6,255,0,0)
        elif minute in ['37']:
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,5,255,0,0)
            sense.set_pixel(4,6,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['38']:
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,4,255,0,0)
        elif minute in ['39']:
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,4,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['40']:
            sense.set_pixel(3,5,255,0,0)
        elif minute in ['41']:
            sense.set_pixel(3,5,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['42']:
            sense.set_pixel(3,5,255,0,0)
            sense.set_pixel(4,6,255,0,0)
        elif minute in ['43']:
            sense.set_pixel(3,5,255,0,0)
            sense.set_pixel(4,6,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['44']:
            sense.set_pixel(3,5,255,0,0)
            sense.set_pixel(4,5,255,0,0)
        elif minute in ['45']:
            sense.set_pixel(3,5,255,0,0)
            sense.set_pixel(4,5,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['46']:
            sense.set_pixel(3,5,255,0,0)
            sense.set_pixel(4,5,255,0,0)
            sense.set_pixel(4,6,255,0,0)
        elif minute in ['47']:
            sense.set_pixel(3,5,255,0,0)
            sense.set_pixel(4,5,255,0,0)
            sense.set_pixel(4,6,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['48']:
            sense.set_pixel(3,5,255,0,0)
            sense.set_pixel(4,4,255,0,0)
        elif minute in ['49']:
            sense.set_pixel(3,5,255,0,0)
            sense.set_pixel(4,4,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['50']:
            sense.set_pixel(3,5,255,0,0)
            sense.set_pixel(3,7,255,0,0)
        elif minute in ['51']:
            sense.set_pixel(3,5,255,0,0)
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['52']:
            sense.set_pixel(3,5,255,0,0)
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,6,255,0,0)
        elif minute in ['53']:
            sense.set_pixel(3,5,255,0,0)
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,6,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['54']:
            sense.set_pixel(3,5,255,0,0)
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,5,255,0,0)
        elif minute in ['55']:
            sense.set_pixel(3,5,255,0,0)
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,5,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['56']:
            sense.set_pixel(3,5,255,0,0)
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,5,255,0,0)
            sense.set_pixel(4,6,255,0,0)
        elif minute in ['57']:
            sense.set_pixel(3,5,255,0,0)
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,5,255,0,0)
            sense.set_pixel(4,6,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif minute in ['58']:
            sense.set_pixel(3,5,255,0,0)
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,4,255,0,0)
        elif minute in ['59']:
            sense.set_pixel(3,5,255,0,0)
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,4,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        
        if second in ['01']:
            sense.set_pixel(7,7,255,0,0)
        elif second in ['02']:
            sense.set_pixel(7,6,255,0,0)
        elif second in ['03']:
            sense.set_pixel(7,6,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['04']:
            sense.set_pixel(7,5,255,0,0)
        elif second in ['05']:
            sense.set_pixel(7,5,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['06']:
            sense.set_pixel(7,5,255,0,0)
            sense.set_pixel(7,6,255,0,0)
        elif second in ['07']:
            sense.set_pixel(7,5,255,0,0)
            sense.set_pixel(7,6,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['08']:
            sense.set_pixel(7,4,255,0,0)
        elif second in ['09']:
            sense.set_pixel(7,4,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['10']:
            sense.set_pixel(6,7,255,0,0)
        elif second in ['11']:
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['12']:
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,6,255,0,0)
        elif second in ['13']:
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,6,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['14']:
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,5,255,0,0)
        elif second in ['15']:
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,5,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['16']:
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,5,255,0,0)
            sense.set_pixel(7,6,255,0,0)
        elif second in ['17']:
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,5,255,0,0)
            sense.set_pixel(7,6,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['18']:
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,4,255,0,0)
        elif second in ['19']:
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,4,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['20']:
            sense.set_pixel(6,6,255,0,0)
        elif second in ['21']:
            sense.set_pixel(6,6,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['22']:
            sense.set_pixel(6,6,255,0,0)
            sense.set_pixel(7,6,255,0,0)
        elif second in ['23']:
            sense.set_pixel(6,6,255,0,0)
            sense.set_pixel(7,6,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['24']:
            sense.set_pixel(6,6,255,0,0)
            sense.set_pixel(7,5,255,0,0)
        elif second in ['25']:
            sense.set_pixel(6,6,255,0,0)
            sense.set_pixel(7,5,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['26']:
            sense.set_pixel(6,6,255,0,0)
            sense.set_pixel(7,5,255,0,0)
            sense.set_pixel(7,6,255,0,0)
        elif second in ['27']:
            sense.set_pixel(6,6,255,0,0)
            sense.set_pixel(7,5,255,0,0)
            sense.set_pixel(7,6,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['28']:
            sense.set_pixel(6,6,255,0,0)
            sense.set_pixel(7,4,255,0,0)
        elif second in ['29']:
            sense.set_pixel(6,6,255,0,0)
            sense.set_pixel(7,4,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['30']:
            sense.set_pixel(6,6,255,0,0)
            sense.set_pixel(6,7,255,0,0)
        elif second in ['31']:
            sense.set_pixel(6,6,255,0,0)
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['32']:
            sense.set_pixel(6,6,255,0,0)
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,6,255,0,0)
        elif second in ['33']:
            sense.set_pixel(6,6,255,0,0)
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,6,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['34']:
            sense.set_pixel(6,6,255,0,0)
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,5,255,0,0)
        elif second in ['35']:
            sense.set_pixel(6,6,255,0,0)
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,5,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['36']:
            sense.set_pixel(6,6,255,0,0)
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,5,255,0,0)
            sense.set_pixel(7,6,255,0,0)
        elif second in ['37']:
            sense.set_pixel(6,6,255,0,0)
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,5,255,0,0)
            sense.set_pixel(7,6,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['38']:
            sense.set_pixel(6,6,255,0,0)
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,4,255,0,0)
        elif second in ['39']:
            sense.set_pixel(6,6,255,0,0)
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,4,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['40']:
            sense.set_pixel(6,5,255,0,0)
        elif second in ['41']:
            sense.set_pixel(6,5,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['42']:
            sense.set_pixel(6,5,255,0,0)
            sense.set_pixel(7,6,255,0,0)
        elif second in ['43']:
            sense.set_pixel(6,5,255,0,0)
            sense.set_pixel(7,6,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['44']:
            sense.set_pixel(6,5,255,0,0)
            sense.set_pixel(7,5,255,0,0)
        elif second in ['45']:
            sense.set_pixel(6,5,255,0,0)
            sense.set_pixel(7,5,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['46']:
            sense.set_pixel(6,5,255,0,0)
            sense.set_pixel(7,5,255,0,0)
            sense.set_pixel(7,6,255,0,0)
        elif second in ['47']:
            sense.set_pixel(6,5,255,0,0)
            sense.set_pixel(7,5,255,0,0)
            sense.set_pixel(7,6,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['48']:
            sense.set_pixel(6,5,255,0,0)
            sense.set_pixel(7,4,255,0,0)
        elif second in ['49']:
            sense.set_pixel(6,5,255,0,0)
            sense.set_pixel(7,4,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['50']:
            sense.set_pixel(6,5,255,0,0)
            sense.set_pixel(6,7,255,0,0)
        elif second in ['51']:
            sense.set_pixel(6,5,255,0,0)
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['52']:
            sense.set_pixel(6,5,255,0,0)
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,6,255,0,0)
        elif second in ['53']:
            sense.set_pixel(6,5,255,0,0)
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,6,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['54']:
            sense.set_pixel(6,5,255,0,0)
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,5,255,0,0)
        elif second in ['55']:
            sense.set_pixel(6,5,255,0,0)
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,5,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['56']:
            sense.set_pixel(6,5,255,0,0)
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,5,255,0,0)
            sense.set_pixel(7,6,255,0,0)
        elif second in ['57']:
            sense.set_pixel(6,5,255,0,0)
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,5,255,0,0)
            sense.set_pixel(7,6,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        elif second in ['58']:
            sense.set_pixel(6,5,255,0,0)
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,4,255,0,0)
        elif second in ['59']:
            sense.set_pixel(6,5,255,0,0)
            sense.set_pixel(6,7,255,0,0)
            sense.set_pixel(7,4,255,0,0)
            sense.set_pixel(7,7,255,0,0)
        
        time.sleep(1)
except KeyboardInterrupt:
    print("\n [*] Keyboard Interrupt. Aborting !!! \n")
    sense.clear()
