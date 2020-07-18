import I2C_LCD_driver
import time
import datetime

lcd1 = I2C_LCD_driver.lcd()

try:
    while True:
        #lcd1.lcd_display_string("Hello World!", x,y) X = 1 or 2; 
        #lcd1.lcd_display_string("Ashutosh", 1,1)
        #time.sleep(1)
        #lcd1.lcd_clear()
        
        #lcd1.lcd_display_string("Shukla", 1,1)
        #time.sleep(1)
        #lcd1.lcd_clear()
  
        # Date and Time
        lcd1.lcd_display_string("Date: %s" %datetime.datetime.now().strftime("%d-%m-%Y"),1,0)
        lcd1.lcd_display_string("Time: %s" %datetime.datetime.now().strftime("%H:%M:%S"),2,0)
except KeyboardInterrupt:
        lcd1.lcd_clear()
        print('Keyboard Interrupt. Exiting.')

"""
Print IP Address
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915, 
        struct.pack('256s', ifname[:15])
    )[20:24])

lcd1.lcd_display_string("IP Address:", 1) 

lcd1.lcd_display_string(get_ip_address('eth0'), 2)
"""

"""
Scroll text right to left continuously
str_pad = " " * 16
my_long_string = "This is a string that needs to scroll"
my_long_string = str_pad + my_long_string

while True:
    for i in range (0, len(my_long_string)):
        lcd_text = my_long_string[i:(i+16)]
        lcd1.lcd_display_string(lcd_text,1)
        sleep(0.4)
        lcd1.lcd_display_string(str_pad,1)
"""

"""
right to left once
str_pad = " " * 16
my_long_string = "This is a string that needs to scroll"
my_long_string = str_pad + my_long_string

for i in range (0, len(my_long_string)):
 lcd_text = my_long_string[i:(i+16)]
 lcd1.lcd_display_string(lcd_text,1)
 sleep(0.4)
 lcd1.lcd_display_string(str_pad,1)
"""

"""
left to right once

padding = " " * 16
my_long_string = "This is a string that needs to scroll"
padded_string = my_long_string + padding

for i in range (0, len(my_long_string)):
 lcd_text = padded_string[((len(my_long_string)-1)-i):-i]
 lcd1.lcd_display_string(lcd_text,1)
 sleep(0.4)
 lcd1.lcd_display_string(padding[(15+i):i], 1)
"""

"""
single custom character

fontdata1 = [      
        [ 0b00010, 
          0b00100, 
          0b01000, 
          0b10000, 
          0b01000, 
          0b00100, 
          0b00010, 
          0b00000 ],
]

lcd1.lcd_load_custom_chars(fontdata1)
lcd1.lcd_write(0x80)
lcd1.lcd_write_char(0)
"""

"""
multiple custom characters

fontdata1 = [
        # char(0) - Upper-left character
        [ 0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b11111, 
          0b11111 ],

        # char(1) - Upper-middle character
        [ 0b00000, 
          0b00000, 
          0b00100, 
          0b00110, 
          0b00111, 
          0b00111, 
          0b11111, 
          0b11111 ],
        
        # char(2) - Upper-right character
        [ 0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b10000, 
          0b11000 ],
        
        # char(3) - Lower-left character
        [ 0b11111, 
          0b11111, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000 ],
       
        # char(4) - Lower-middle character
        [ 0b11111, 
          0b11111, 
          0b00111, 
          0b00111, 
          0b00110, 
          0b00100, 
          0b00000, 
          0b00000 ],
        
        # char(5) - Lower-right character
        [ 0b11000, 
          0b10000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000, 
          0b00000 ],
]

lcd1.lcd_load_custom_chars(fontdata1)

lcd1.lcd_write(0x80)
lcd1.lcd_write_char(0)
lcd1.lcd_write_char(1)
lcd1.lcd_write_char(2)

lcd1.lcd_write(0xC0)
lcd1.lcd_write_char(3)
lcd1.lcd_write_char(4)
lcd1.lcd_write_char(5)
"""

"""
printing data from sensor
import RPi.GPIO as GPIO
import dht11
import I2C_LCD_driver

from time import *

lcd = I2C_LCD_driver.lcd()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

while True:
  
  instance = dht11.DHT11(pin = 4)
  result = instance.read()

# Uncomment for Fahrenheit:
# result.temperature = (result.temperature * 1.8) + 32 

  if result.is_valid():
    lcd1.lcd_display_string("Temp: %d%s C" % (result.temperature, chr(223)), 1)
    lcd1.lcd_display_string("Humidity: %d %%" % result.humidity, 2)
"""

