from machine import Pin
import time

red = Pin(15, Pin.OUT)
green = Pin(14, Pin.OUT)
blue = Pin(13, Pin.OUT)

button1 = Pin(16, Pin.IN, Pin.PULL_UP)
button2 = Pin(21, Pin.IN, Pin.PULL_UP)
button3 = Pin(18, Pin.IN, Pin.PULL_UP)

red_is_on = False
green_is_on = False
blue_is_on = False

while True:
    if button1.value() == 0:
        red_is_on = not red_is_on
        red.value(red_is_on)
        time.sleep(0.25)
    if button2.value() == 0:
        green_is_on = not green_is_on
        green.value(green_is_on)
        time.sleep(0.25)
    if button3.value() == 0:
        blue_is_on = not blue_is_on
        blue.value(blue_is_on)
        time.sleep(0.25)

    time.sleep(0.05)