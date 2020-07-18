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
# import argparse
import time

# globals
BELL_PIN = 24

# parser = argparse.ArgumentParser()

# group = parser.add_mutually_exclusive_group()
# group.add_argument("-l", "--light", action="store_true")
# group.add_argument("-o", "--off", action="store_true")

# Disable warnings
GPIO.setwarnings(False)

# turn on gpio pin BELL pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(BELL_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(BELL_PIN, GPIO.RISING)

# args = parser.parse_args()

def my_callback(self):
    print 'Doorbell pushed!'
    time.sleep(2)

GPIO.add_event_callback(BELL_PIN, my_callback)

while True:
     time.sleep(1000) # don't riun all the time

