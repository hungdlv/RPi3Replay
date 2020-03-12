import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(32,GPIO.OUT)
GPIO.output(32,GPIO.HIGH)

GPIO.setup(36,GPIO.OUT)
GPIO.output(36,GPIO.HIGH)

GPIO.setup(38,GPIO.OUT)
GPIO.output(38,GPIO.HIGH)

GPIO.setup(40,GPIO.OUT)
GPIO.output(40,GPIO.HIGH)

try:
    GPIO.output(32,GPIO.LOW)
    print("First Relay ON")
    time.sleep(2)

    GPIO.output(36,GPIO.LOW)
    print("Second Relay ON")
    time.sleep(2)

    GPIO.output(38,GPIO.LOW)
    print("Third Relay ON")
    time.sleep(2)

    GPIO.output(40,GPIO.LOW)
    print("Fourth Relay ON")
    time.sleep(5)