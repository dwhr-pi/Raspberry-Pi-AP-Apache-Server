#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
import cgi
import time
import piezo
from tendo import singleton

me = singleton.SingleInstance()

print "Content-Type: text/html\n"

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

r = 11
g = 13
b = 15

buz = piezo.buzzer(19)

GPIO.setup(r, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
    
def red_team():
    GPIO.output(r, 0)
    GPIO.output(g, 1)
    GPIO.output(b, 1)
    buz.play('gameshow', 3)

def green_team():
    GPIO.output(r, 1)
    GPIO.output(g, 0)
    GPIO.output(b, 1)
    buz.play('gameshow', 3)

def blue_team():
    GPIO.output(r, 1)
    GPIO.output(g, 1)
    GPIO.output(b, 0)
    buz.play('gameshow', 3)

def off():
    GPIO.output(r, 1)
    GPIO.output(g, 1)
    GPIO.output(b, 1)

data = cgi.FieldStorage()
option = data.getvalue('a')
if option == "red_team":
    red_team()
elif option == "green_team":
    green_team()
elif option == "blue_team":
    blue_team()

time.sleep(5)
off()
