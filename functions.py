from gfxhat import lcd
from gfxhat import backlight
from gfxhat import lcd
import gfxhat
import time
from random import randint
from gfxhat import backlight

#vertical
def hori(x):
    y= 1
    while y < 64:
        lcd.set_pixel(x,y,1)
        lcd.show()
        y += 1
#horizontal
def verti(y):
    x= 1
    while x < 127:
        lcd.set_pixel(x,y,1)
        lcd.show()
        x += 1

def stairdr(y,x,h,w):
    while y < 64  and y < 63:
        stairdrvert(y,x,h,w)
        y = stairdrvert(y,x,h,w)
        stairdrhori(y,x,h,w)
        x= stairdrhori(y,x,h,w)
        if x == 127:
            break
        if y == 63:
            break

#verticaldown
def stairdrvert(y,x,h,w):
    y1 = y + h
    while y < y1:
        lcd.set_pixel(x,y,1)
        lcd.show()
        y += 1
        if x == 127:
            break
        if y == 63:
            break
    return y 
#horizontalright
def stairdrhori(y,x,h,w):
    x1 = x + w   
    while x < x1:
        lcd.set_pixel(x,y,1)
        lcd.show()
        x += 1
        if x == 127:
            break
        if y == 63:
            break
    return x

#random pixel
def randPix(t):
    y = randint(1,63)
    x = randint(1,128)
    lcd.set_pixel(x,y,1)
    lcd.show()
    time.sleep(t)
    gfxhat.lcd.clear()
    lcd.show()

#backlight generator
def clearBacklight():
    a = randint(0,255)
    b = randint(0,255)
    c = randint(0,255,)
    backlight.set_all(a,b,c)
    backlight.show()
