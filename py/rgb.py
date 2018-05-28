'''
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

sleep_time = 0.1

GPIO.setup(r, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)

def white():
    GPIO.output(r, 0)
    GPIO.output(g, 0)
    GPIO.output(b, 0)

def red():
    GPIO.output(r, 0)
    GPIO.output(g, 1)
    GPIO.output(b, 1)

def green():
    GPIO.output(r, 1)
    GPIO.output(g, 0)
    GPIO.output(b, 1)

def blue():
    GPIO.output(r, 1)
    GPIO.output(g, 1)
    GPIO.output(b, 0)

def off():
    GPIO.output(r, 1)
    GPIO.output(g, 1)
    GPIO.output(b, 1)
def purple():
    GPIO.output(r, 0)
    GPIO.output(g, 1)
    GPIO.output(b, 0)
def turquoise():
    GPIO.output(r, 1)
    GPIO.output(g, 0)
    GPIO.output(b, 0)
def orange():
    GPIO.output(r, 0)
    GPIO.output(g, 0)
    GPIO.output(b, 1)
def rainbow():
    for i in range(10):
        red()
        time.sleep(sleep_time)
        purple()
        time.sleep(sleep_time)
        orange()
        time.sleep(sleep_time)
        green()
        time.sleep(sleep_time)
        turquoise()
        time.sleep(sleep_time)
        blue()
        time.sleep(sleep_time)
    off()
def police():
    buz = piezo.buzzer(19)
    buz.play("police_siren", 2)
def siren():
    for i in range(10):
        red()
        time.sleep(0.5)
        blue()
        time.sleep(0.5)
    off()

data = cgi.FieldStorage()
option = data.getvalue('a')
if option == "off": off()
elif option == "white": white()
elif option == "red": red()
elif option == "green": green()
elif option == "blue": blue()
elif option == "purple": purple()
elif option == "turquoise": turquoise()
elif option == "orange": orange()
elif option == "rainbow": rainbow()
elif option == "police": police()
elif option == "siren": siren()
'''
