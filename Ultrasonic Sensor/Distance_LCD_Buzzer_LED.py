import I2C_LCD_driver
import RPi.GPIO as GPIO
import time

lcd1 = I2C_LCD_driver.lcd()
GPIO.setmode(GPIO.BOARD)

ledPin = 11
buzzerPin = 12
triggerPin = 15
echoPin = 16

GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(buzzerPin,GPIO.OUT)
GPIO.setup(triggerPin,GPIO.OUT)
GPIO.setup(echoPin,GPIO.IN)

#print('Let the trigger to settle.')
GPIO.output(triggerPin,0)
time.sleep(0.5)

try:
    print('\n\t [*] Sensing distance from the sensor. See the LCD.')
    lcd1.lcd_display_string("Ranging Sensor",1,0)
    while True:
        lcd1.lcd_display_string("Dist.:          ",2,0)
        GPIO.output(triggerPin,1)
        time.sleep(0.00001) # 10 nano seconds
        GPIO.output(triggerPin,0)
        
        while GPIO.input(echoPin)==0:
            pulse_start = time.time()
            
        while GPIO.input(echoPin)==1:
            pulse_end = time.time()
        
        pulse_duration = pulse_end - pulse_start
        #print('Start:',pulse_start,' End:',pulse_end,' Duration:',pulse_duration)
        
        distance = pulse_duration * 17150
        #distance = pulse_duration * 14.5
        distance = round(distance,0)
        #print('Distance:',distance)
        
        if distance<15:
            GPIO.output(buzzerPin,1)
            GPIO.output(ledPin,1)
        else:
            GPIO.output(buzzerPin,0)
            GPIO.output(ledPin,0)
        
        lcd1.lcd_display_string("Dist.: %d cm" %distance,2,0)
        time.sleep(0.5)
except KeyboardInterrupt:
    print('\n\n\t [*] Keyboard Interrupt. Aborting !!!\n')
    lcd1.lcd_clear()
    GPIO.cleanup()