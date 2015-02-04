#!/usr/bin/python
import time
import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)

GPIO_TRIGGER = 16
GPIO_ECHO    = 18

Motor1A = 36
Motor1B = 38
Motor1E = 40

Motor2A = 33
Motor2B = 35
Motor2E = 37

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

print "Ultrasonic Measurement"

GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

GPIO.output(GPIO_TRIGGER, False)

def measure():
  time.sleep(0.333)
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()
  
  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()

  elapsed = stop-start
  distance = (elapsed * 34300)/2

  return distance


def forward():
  GPIO.output(Motor1A,GPIO.HIGH)
  GPIO.output(Motor1B,GPIO.LOW)
  GPIO.output(Motor1E,GPIO.HIGH)
  GPIO.output(Motor2A,GPIO.HIGH)
  GPIO.output(Motor2B,GPIO.LOW)
  GPIO.output(Motor2E,GPIO.HIGH)
def turn():
  GPIO.output(Motor1A,GPIO.LOW)
  GPIO.output(Motor1B,GPIO.HIGH)
  GPIO.output(Motor1E,GPIO.HIGH)
  GPIO.output(Motor2A,GPIO.HIGH)
  GPIO.output(Motor2B,GPIO.LOW)
  GPIO.output(Motor2E,GPIO.HIGH)

try:

  while True:

    distance = measure()
    print "Distance : %.1f" % distance
    time.sleep(.5)


    if distance >= 10:
     forward()
    else:
     turn()

except KeyboardInterrupt:

 GPIO.cleanup()
