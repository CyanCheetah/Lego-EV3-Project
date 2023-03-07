#!/usr/bin/env python3
import subprocess
import time
# Run the `sudo fbi` command to display an image
filename = 'img.bmp' #Change filename to whatever name it is in. also change directory below. 
subprocess.run(['sudo', 'fbi', '-T', '1', '-noverbose', '-a', '/home/robot/ev3/'+filename])

time.sleep(5)

#CyanCheetah
#To Run this program, in the ssh do: sudo python3 /home/robot/ev3/ev3/tests/code/Display.py
#Or whatever the path of the pthon program is
