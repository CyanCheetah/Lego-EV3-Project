#!/usr/bin/env python3
import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_3
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
import ev3dev2.auto as ev3
from time import sleep
import ev3dev2.fonts as fonts
#from PIL import Image
#from ev3dev2.display import Display


import subprocess
import time

from ev3dev2.sound import Sound

import ev3dev2.sensor as sensor
import subprocess
sound = Sound()
screen = ev3.Display()
screen.clear()

sound.speak('Hello!')
sound.speak('Click the Button to Capture an Image')
while True:
    screen.clear()
    screen.draw.text((0,0), 'Click the Button', font=fonts.load('ncenI24'))
    screen.draw.text((0,6), 'to capture', font=fonts.load('ncenI24'))
    screen.draw.text((0,12), 'an image', font=fonts.load('ncenI24'))



    ts = TouchSensor(INPUT_3)
    if ts.is_pressed:
        timestamp = time.strftime('%Y%m%d-%H%M%S')
        filename = 'image-{}.jpg'.format(timestamp)
        subprocess.call(['fswebcam', '-r', '100x100', '--no-banner', filename])
        sound.speak('Image Captured!')
    screen.update()
#CyanCheetah
