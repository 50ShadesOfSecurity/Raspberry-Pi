# https://gist.github.com/DenisFromHR/cc863375a6e19dce359d
# requires RPi_I2C_driver.py
import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()
# test 2
mylcd.lcd_display_string("RPi I2C test", 1)
mylcd.lcd_display_string(" Custom chars", 2)

sleep(2) # 2 sec delay

mylcd.lcd_clear()

# let's define a custom icon, consisting of 6 individual characters
# 3 chars in the first row and 3 chars in the second row
fontdata1 = [
        # Char 0 - Upper-left
        [ 0x00, 0x00, 0x03, 0x04, 0x08, 0x19, 0x11, 0x10 ],
        # Char 1 - Upper-middle
        [ 0x00, 0x1F, 0x00, 0x00, 0x00, 0x11, 0x11, 0x00 ],
        # Char 2 - Upper-right
        [ 0x00, 0x00, 0x18, 0x04, 0x02, 0x13, 0x11, 0x01 ],
        # Char 3 - Lower-left
        [ 0x12, 0x13, 0x1b, 0x09, 0x04, 0x03, 0x00, 0x00 ],
        # Char 4 - Lower-middle
        [ 0x00, 0x11, 0x1f, 0x1f, 0x0e, 0x00, 0x1F, 0x00 ],
        # Char 5 - Lower-right
        [ 0x09, 0x19, 0x1b, 0x12, 0x04, 0x18, 0x00, 0x00 ],
        # Char 6 - my test
	[ 0x1f,0x0,0x4,0xe,0x0,0x1f,0x1f,0x1f],
]

# Load logo chars (fontdata1)
mylcd.lcd_load_custom_chars(fontdata1)


# Write first three chars to row 1 directly
mylcd.lcd_write(0x80)
mylcd.lcd_write_char(0)
mylcd.lcd_write_char(1)
mylcd.lcd_write_char(2)
# Write next three chars to row 2 directly
mylcd.lcd_write(0xC0)
mylcd.lcd_write_char(3)
mylcd.lcd_write_char(4)
mylcd.lcd_write_char(5)
sleep(2)

mylcd.lcd_clear()

mylcd.lcd_display_string_pos("Testing",1,1) # row 1, column 1
sleep(1)
mylcd.lcd_display_string_pos("Testing",2,3) # row 2, column 3
sleep(1)
mylcd.lcd_clear()

# Now let's define some more custom characters
fontdata2 = [
        # Char 0 - left arrow
        [ 0x1,0x3,0x7,0xf,0xf,0x7,0x3,0x1 ],
        # Char 1 - left one bar 
        [ 0x10,0x10,0x10,0x10,0x10,0x10,0x10,0x10 ],
        # Char 2 - left two bars
        [ 0x18,0x18,0x18,0x18,0x18,0x18,0x18,0x18 ],
        # Char 3 - left 3 bars
        [ 0x1c,0x1c,0x1c,0x1c,0x1c,0x1c,0x1c,0x1c ],
        # Char 4 - left 4 bars
        [ 0x1e,0x1e,0x1e,0x1e,0x1e,0x1e,0x1e,0x1e ],
        # Char 5 - left start
        [ 0x0,0x1,0x3,0x7,0xf,0x1f,0x1f,0x1f ],
        # Char 6 - 
        # [ ],
]

# Load logo chars from the second set
mylcd.lcd_load_custom_chars(fontdata2)

block = chr(255) # block character, built-in

# display two blocks in columns 5 and 6 (i.e. AFTER pos. 4) in row 1
# first draw two blocks on 5th column (cols 5 and 6), starts from 0
mylcd.lcd_display_string_pos(block * 2,1,4)

# 
pauza = 0.2 # define duration of sleep(x)
#
# now draw cust. chars starting from col. 7 (pos. 6)

pos = 6
mylcd.lcd_display_string_pos(unichr(1),1,6)
sleep(pauza)

mylcd.lcd_display_string_pos(unichr(2),1,pos)
sleep(pauza)

mylcd.lcd_display_string_pos(unichr(3),1,pos)
sleep(pauza)

mylcd.lcd_display_string_pos(unichr(4),1,pos)
sleep(pauza)

mylcd.lcd_display_string_pos(block,1,pos)
sleep(pauza)

# and another one, same as above, 1 char-space to the right
pos = pos +1 # increase column by one

mylcd.lcd_display_string_pos(unichr(1),1,pos)
sleep(pauza)
mylcd.lcd_display_string_pos(unichr(2),1,pos)
sleep(pauza)
mylcd.lcd_display_string_pos(unichr(3),1,pos)
sleep(pauza)
mylcd.lcd_display_string_pos(unichr(4),1,pos)
sleep(pauza)
mylcd.lcd_display_string_pos(block,1,pos)
sleep(pauza)


#
# now again load first set of custom chars - smiley
mylcd.lcd_load_custom_chars(fontdata1)

mylcd.lcd_display_string_pos(unichr(0),1,9)
mylcd.lcd_display_string_pos(unichr(1),1,10)
mylcd.lcd_display_string_pos(unichr(2),1,11)
mylcd.lcd_display_string_pos(unichr(3),2,9)
mylcd.lcd_display_string_pos(unichr(4),2,10)
mylcd.lcd_display_string_pos(unichr(5),2,11)

sleep(2)
mylcd.lcd_clear()
sleep(1)
mylcd.backlight(0)

"""
import I2C_LCD_driver
import time
import datetime

lcd = I2C_LCD_driver.lcd()

# It's a 16x2 LCD i.e. X=1-2, Y=1-16

# Print a string at X-Y coordinate.
# lcd.lcd_display_string("Hello World!", x,y)

# Print Date and Time
# lcd1.lcd_display_string("Date: %s" %datetime.datetime.now().strftime("%d/%m/%Y"),1,0)
# lcd1.lcd_display_string("Time: %s" %datetime.datetime.now().strftime("%H:%M:%S"),2,0)

# Clear the display
# lcd.lcd_clear()

####################
# Print IP Address #
####################

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915, 
        struct.pack('256s', ifname[:15])
    )[20:24])

lcd.lcd_display_string("IP Address:", 1) 

lcd.lcd_display_string(get_ip_address('eth0'), 2)

##########################################
# Scroll text right to left continuously #
##########################################

str_pad = " " * 16
my_long_string = "This is a string that needs to scroll"
my_long_string = str_pad + my_long_string

while True:
    for i in range (0, len(my_long_string)):
        lcd_text = my_long_string[i:(i+16)]
        lcd.lcd_display_string(lcd_text,1)
        sleep(0.4)
        lcd.lcd_display_string(str_pad,1)

######################
# right to left once #
######################

str_pad = " " * 16
my_long_string = "This is a string that needs to scroll"
my_long_string = str_pad + my_long_string

for i in range (0, len(my_long_string)):
 lcd_text = my_long_string[i:(i+16)]
 lcd.lcd_display_string(lcd_text,1)
 sleep(0.4)
 lcd.lcd_display_string(str_pad,1)

######################
# left to right once #
######################

padding = " " * 16
my_long_string = "This is a string that needs to scroll"
padded_string = my_long_string + padding

for i in range (0, len(my_long_string)):
 lcd_text = padded_string[((len(my_long_string)-1)-i):-i]
 lcd.lcd_display_string(lcd_text,1)
 sleep(0.4)
 lcd.lcd_display_string(padding[(15+i):i], 1)

###########################
# single custom character #
###########################

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

lcd.lcd_load_custom_chars(fontdata1)
lcd.lcd_write(0x80)
lcd.lcd_write_char(0)

##############################
# multiple custom characters #
##############################

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

lcd.lcd_load_custom_chars(fontdata1)

lcd.lcd_write(0x80)
lcd.lcd_write_char(0)
lcd.lcd_write_char(1)
lcd.lcd_write_char(2)

lcd.lcd_write(0xC0)
lcd.lcd_write_char(3)
lcd.lcd_write_char(4)
lcd.lcd_write_char(5)

#############################
# printing data from sensor #
#############################

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
    lcd.lcd_display_string("Temp: %d%s C" % (result.temperature, chr(223)), 1)
    lcd.lcd_display_string("Humidity: %d %%" % result.humidity, 2)
"""