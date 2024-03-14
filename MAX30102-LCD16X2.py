"""import max30102
m = max30102.MAX30102()
red, ir = m.read_sequential()
# after you load red and ir
import hrcalc
xx = hrcalc.calc_hr_and_spo2(ir[:100], red[:100]) 
print(xx)
# give 100 values (136, True, 98.752554, True)
# this shows hr is 136 and it is a valid value, spo2 is 98% and it is a valid value
# this value is produced when using line 10 - 110 of sample logs*/"""


import max30102
import hrcalc
# import hrcalc1
import I2C_LCD_driver
from time import *

m = max30102.MAX30102()

lcd = I2C_LCD_driver.lcd()
lcd.lcd_clear()
lcd.backlight(1)

# 100 samples are read and used for HR/SpO2 calculation in a single loop
while True:
    red, ir = m.read_sequential()
    print(hrcalc.calc_hr_and_spo2(ir, red))
    irString = str(hrcalc.calc_hr_and_spo2_ir(ir,red))
    redString = str(hrcalc.calc_hr_and_spo2_red(ir,red))
    lcd.lcd_display_string("heart rate = " + irString, 1, 0)
    lcd.lcd_display_string("spo2 = " + redString, 2, 0)
	

