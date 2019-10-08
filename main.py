from functions import hori
from functions import verti
from functions import stairdr
from functions import randPix
from functions import clearBacklight
from gfxhat import backlight
from gfxhat import lcd
import gfxhat

backlight.set_all(0, 55,0)
gfxhat.lcd.clear()
backlight.show()
gfxhat.lcd.show()


print('''Enter the program number to run the code:

1. Draw a line on verticle on the x axis
2. Draw a horizontal line on the y axis
3. Create a staircase starting at (x,y)
4. Display a random pixel
5. Clears the backlight and resets colour at random
''')

while True:
    
    numb = input("Enter the program number: ")
    if numb == '1':
        x = int(input("Enter the x axis: "))
        hori(x)
    elif numb == '2':
        y = int(input("Enter the y axis: "))
        verti(y)
    elif numb == '3':
        x = int(input("Enter the x axis: "))
        y = int(input("Enter the y axis: "))
        w = int(input("Enter the width of the stair"))
        h = int(input("Enter the height of the stair"))
        print = "The stairs will go down and left"
        stairdr(x,y,w,h)
    elif numb =='4':
        t = int(input("Enter the time you wish the pixel to display for in seconds"))
        randPix(t)
    elif numb =='5':
        clearBacklight()
