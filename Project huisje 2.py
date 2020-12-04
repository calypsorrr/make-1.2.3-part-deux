#!/usr/bin/env python
"""
Info about our project comes here
"""


# Imports
from guizero import App, PushButton, Text, Box
from gpiozero import LED
import sys
import time
from gpiozero.pins.pigpio import PiGPIOFactory


__author__ = "Bo Claes"
__email__ = "bo.claes@student.kdg.be"
__status__ = "Development"


# Configurations
IP_ADRESS = PiGPIOFactory(  host='192.168.1.206')

led_01 = LED(pin=21, pin_factory=IP_ADRESS)
led_02 = LED(pin=26, pin_factory=IP_ADRESS)
led_03 = LED(pin=20, pin_factory=IP_ADRESS)
led_04 = LED(pin=16, pin_factory=IP_ADRESS)


def exit_app():
    sys.exit()

def toggle_led():
    led_01.toggle()
    led_02.toggle()
    led_03.toggle()
    led_04.toggle()
    if led_01.is_lit:
        ledButton.text = "LED OFF"
    else:
        ledButton.text = "LED ON"

def led_blink():
    for i in range(10):
        led_01.on()
        led_02.on()
        led_03.on()
        led_04.on()
        time.sleep(2)
        led_01.off()
        led_02.off()
        led_03.off()
        led_04.off()

def main():
    global ledButton
    # App
    app = App(title="Project house", height=400, width=400)

    # Boxes
    displayBox = Box(app, border= True, height=35, width=400)
    buttonBox = Box(app, layout="grid", align="top")

    # Title
    title = Text(displayBox, text="Push a button")
    title.text_size = 20

    # Buttons
    ledButton = PushButton(buttonBox, toggle_led, text="LED ON", grid=[0,0])
    ledButton.text_size = 25
    blinkButton = PushButton(buttonBox, led_blink, text="Push to party", grid=[10,0])
    blinkButton.text_size= 25
    exitButton = PushButton(app, exit_app, text="EXIT", align="bottom", width=16, height=2)
    exitButton.text_size = 32

    app.display()

if __name__ == '__main__':  # code to execute if called from command-line
    main()
