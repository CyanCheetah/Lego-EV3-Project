#!/usr/bin/env python3

import time
import ev3dev2.auto as ev3
import ev3dev2.fonts as fonts
import subprocess
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.button import Button
btn = Button()
sound = Sound()
screen = ev3.Display()
screen.clear()

sound.speak('Hello!')
sound.speak('Click the Button to Capture an Image')
screen.clear()
screen.draw.text((0,0), 'Click the Button', font=fonts.load('ncenI24'))
screen.draw.text((0,12), 'to capture', font=fonts.load('ncenI24'))
screen.draw.text((0,24), 'an image', font=fonts.load('ncenI24'))

while not btn.down:
    ts = TouchSensor(INPUT_4)
    if ts.is_pressed:
        timestamp = time.strftime('%Y%m%d-%H%M%S')
        filename = 'image.bmp'
        subprocess.call(['fswebcam', '-r', '160x90', '--no-banner', filename])
        time.sleep(5)
        subprocess.run(['sudo', 'service', 'udev', 'restart'])
        time.sleep(5)
        subprocess.run(['sudo', 'fbi', '-T', '1', '-noverbose', '-a', '/home/robot/image.bmp'])
        time.sleep(10)
#To Run this program, in the ssh do: sudo python3 /home/robot/ev3/ev3/tests/code/WebcamDisplay.py

