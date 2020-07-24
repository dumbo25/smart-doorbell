#!/usr/bin/env python

# Controls low profile, metal, normally open, momentary pushbutton's blue LED ring
# The part is from mouser.com
# https://www.mouser.com/ProductDetail/E-Switch/PVT4FW4SS341?qs=MLItCLRbWszrh7bO8ezdSg%3D%3D
#
# move file to /usr/local/bin/pb_bell.py
# sudo chmod +x /usr/local/bin/pb_bell.py
#
# run using:
#   /usr/local/bin/pb_bell.py

# modules
import RPi.GPIO as GPIO
import subprocess
import time

# globals
BELL_PIN = 24
VOLUME = 75

# On commands like play, prev and next, mpc outputs a line similar to:
#
#    volume: n/a repeat: off random: off single: off consume: off
#
# adding the following to any mpc command suppresses that output

limitMPCoutput = " | grep \"[-,'[']\""

# Disable warnings
GPIO.setwarnings(False)

# turn on gpio pin BELL pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(BELL_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(BELL_PIN, GPIO.RISING)

# set volume
cmd = "mpc volume " + str(VOLUME) + limitMPCoutput
subprocess.call(cmd, shell=True)

# clear playlist
cmd = "mpc clear " + limitMPCoutput
subprocess.call(cmd, shell=True)

# add ring tone
cmd = "mpc insert /home/pi/ring2.m4a" + limitMPCoutput
subprocess.call(cmd, shell=True)

# run this when the button is pressed
def my_callback(self):
    cmd = "mpc play 1 " + limitMPCoutput
    subprocess.call(cmd, shell=True)
    time.sleep(1)

GPIO.add_event_callback(BELL_PIN, my_callback)

# loop forever and sleep most of the time
while True:
        time.sleep(1000)
