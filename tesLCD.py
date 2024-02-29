import I2C_LCD_driver
from time import *
#import psutil
import re

lcd = I2C_LCD_driver.lcd()
lcd.lcd_clear()
lcd.backlight(1)
lcd.lcd_display_string("Hello World!", 1, 0)
sleep(5)
