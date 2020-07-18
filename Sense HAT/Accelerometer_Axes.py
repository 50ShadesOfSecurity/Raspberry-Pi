from sense_hat import SenseHat

sense = SenseHat()

try:
    while True:
        accel = sense.get_accelerometer_raw()
        
        x = round(accel['x'])
        y = round(accel['y'])
        z = round(accel['z'])
        #print('X: {}, Y: {}, Z: {}'.format(x,y,z))
    
        if x == 0:
            sense.set_pixel(0,3,255,255,255)
            sense.set_pixel(0,4,255,255,255)
            sense.set_pixel(1,3,255,255,255)
            sense.set_pixel(1,4,255,255,255)
            sense.set_pixel(6,3,255,255,255)
            sense.set_pixel(6,4,255,255,255)
            sense.set_pixel(7,3,255,255,255)
            sense.set_pixel(7,4,255,255,255)
        elif x == 1:
            sense.set_pixel(0,3,255,255,255)
            sense.set_pixel(0,4,255,255,255)
            sense.set_pixel(1,3,255,255,255)
            sense.set_pixel(1,4,255,255,255)
            sense.set_pixel(6,3,255,0,0)
            sense.set_pixel(6,4,255,0,0)
            sense.set_pixel(7,3,255,0,0)
            sense.set_pixel(7,4,255,0,0)
        elif x == -1:
            sense.set_pixel(0,3,255,0,0)
            sense.set_pixel(0,4,255,0,0)
            sense.set_pixel(1,3,255,0,0)
            sense.set_pixel(1,4,255,0,0)
            sense.set_pixel(6,3,255,255,255)
            sense.set_pixel(6,4,255,255,255)
            sense.set_pixel(7,3,255,255,255)
            sense.set_pixel(7,4,255,255,255)
        if y == 0:
            sense.set_pixel(3,0,255,255,255)
            sense.set_pixel(3,1,255,255,255)
            sense.set_pixel(4,0,255,255,255)
            sense.set_pixel(4,1,255,255,255)
            sense.set_pixel(3,6,255,255,255)
            sense.set_pixel(3,7,255,255,255)
            sense.set_pixel(4,6,255,255,255)
            sense.set_pixel(4,7,255,255,255)
        elif y == 1:
            sense.set_pixel(3,0,255,255,255)
            sense.set_pixel(3,1,255,255,255)
            sense.set_pixel(4,0,255,255,255)
            sense.set_pixel(4,1,255,255,255)
            sense.set_pixel(3,6,255,0,0)
            sense.set_pixel(3,7,255,0,0)
            sense.set_pixel(4,6,255,0,0)
            sense.set_pixel(4,7,255,0,0)
        elif y == -1:
            sense.set_pixel(3,0,255,0,0)
            sense.set_pixel(3,1,255,0,0)
            sense.set_pixel(4,0,255,0,0)
            sense.set_pixel(4,1,255,0,0)
            sense.set_pixel(3,6,255,255,255)
            sense.set_pixel(3,7,255,255,255)
            sense.set_pixel(4,6,255,255,255)
            sense.set_pixel(4,7,255,255,255)
        if z == 0:
            sense.set_pixel(3,3,255,255,255)
            sense.set_pixel(4,3,255,255,255)
            sense.set_pixel(3,4,255,255,255)
            sense.set_pixel(4,4,255,255,255)
        elif z == 1:
            sense.set_pixel(3,3,0,255,0)
            sense.set_pixel(4,3,0,255,0)
            sense.set_pixel(3,4,0,255,0)
            sense.set_pixel(4,4,0,255,0)
        elif z == -1:
            sense.set_pixel(3,3,255,0,0)
            sense.set_pixel(4,3,255,0,0)
            sense.set_pixel(3,4,255,0,0)
            sense.set_pixel(4,4,255,0,0)
        
except KeyboardInterrupt:
    sense.clear()
