import RPi.GPIO as gpio
import time

def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(2, gpio.OUT)
 gpio.setup(3, gpio.OUT)
 gpio.setup(4, gpio.OUT)
 gpio.setup(17, gpio.OUT)
 gpio.setup(27, gpio.OUT)
 gpio.setup(22, gpio.OUT)

def forward(tf):
 init()
 gpio.output(2, True)
 gpio.output(3, False)
 gpio.output(4, True)
 gpio.output(17, False)
 gpio.output(27, True)
 gpio.output(22, True)

time.sleep(tf)
gpio.cleanup()

print "forward"
forward(4)
