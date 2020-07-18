#!/usr/bin/env python

# Controls the motion sensor
#
# move file to /usr/local/bin/motion.py
# sudo chmod +x /usr/local/bin/motion.py
#
# run using:
#   /usr/local/bin/motion.py

# modules
import RPi.GPIO as GPIO
import subprocess
# import argparse
import time

# globals
MOTION_PIN = 25

# parser = argparse.ArgumentParser()

# group = parser.add_mutually_exclusive_group()
# group.add_argument("-l", "--light", action="store_true")
# group.add_argument("-o", "--off", action="store_true")

# Disable warnings
GPIO.setwarnings(False)

# turn on gpio pin MOTION pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTION_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(MOTION_PIN, GPIO.RISING)

# args = parser.parse_args()

def my_callback(self):
    print 'Motion detected!'
    time.sleep(2)

GPIO.add_event_callback(MOTION_PIN, my_callback)

while True:
        time.sleep(1000)
