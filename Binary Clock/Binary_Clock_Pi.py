import I2C_LCD_driver
import RPi.GPIO as GPIO
import time
import datetime

lcd1 = I2C_LCD_driver.lcd()
GPIO.setmode(GPIO.BOARD)

try:
    while True:
        hour = datetime.datetime.now().strftime("%H") # %H for 24-hour format, %I for 12-hour format
        minute = datetime.datetime.now().strftime("%M")
        second = datetime.datetime.now().strftime("%S")
        
        lcd1.lcd_display_string("Binary Clock ",1,2)
        lcd1.lcd_display_string("%s" %datetime.datetime.now().strftime("%H : %M : %S"),2,2)
except KeyboardInterrupt:
    print("\n [*] Keyboard Interrupt. Aborting !!!\n")
    lcd1.lcd_clear()