#!/usr/bin/env python

# Controls low profile, metal, normally open, momenatry pushbutton's blue LED ring
# The part is from mouser.com
#
# move file to /usr/local/bin/pb_led.py
# sudo chmod 755 /usr/local/bin/pb_led.py
# run as:
# /usr/local/bin/power_ring_led.py --light
import RPi.GPIO as GPIO
import subprocess
import argparse

LED_PIN = 23

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument("-l", "--light", action="store_true")
group.add_argument("-o", "--off", action="store_true")

# Disable warnings
GPIO.setwarnings(False)

# turn on gpio pin LED pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
args = parser.parse_args()
if args.light:
        GPIO.output(LED_PIN, True)
elif args.off:
        GPIO.output(LED_PIN, False)
