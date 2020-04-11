import RPi.GPIO as GPIO
import random
import time

pins = [
        {'pin_num': 32, 'color': 'red'},
        {'pin_num': 36, 'color': 'yellow'},
        {'pin_num': 38, 'color': 'green'},
        {'pin_num': 40, 'color': 'blue'}
    ]

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# setup all pins based on above configuration
for pin in pins:
    GPIO.setup(pin['pin_num'], GPIO.OUT, initial=GPIO.HIGH)

def toggle_color(color: str, state: str):
    for pin in pins:
        if pin['color'] == color:
            if state == 'on':
                GPIO.output(pin['pin_num'], GPIO.LOW)
            elif state == 'off':
                GPIO.output(pin['pin_num'], GPIO.HIGH)

def color_on(color: str):
    toggle_color(color, 'on')

def color_off(color: str):
    toggle_color(color, 'off')

def all_on():
    for pin in pins:
        GPIO.output(pin['pin_num'], GPIO.LOW)

def all_off():
    for pin in pins:
        GPIO.output(pin['pin_num'], GPIO.HIGH)


def pin_on(pin_num: int):
    GPIO.output(pin_num, GPIO.LOW)


def pin_off(pin_num: int):
    GPIO.output(pin_num, GPIO.HIGH)

def strobe_reg(period=0.5):
    while True:
        all_on()
        time.sleep(period)
        all_off()
        time.sleep(period)


def strobe_rand(min_time=0, max_time=1.2):
    while True:
        all_on()
        time.sleep(random.uniform(min_time, max_time))
        all_off()
        time.sleep(random.uniform(min_time, max_time))


def wave_reg(period=0.1):
    while True:
        for pin in pins:
            GPIO.output(pin['pin_num'], GPIO.HIGH)
            time.sleep(period)

        for pin in reversed(pins):
            GPIO.output(pin['pin_num'], GPIO.LOW)
            time.sleep(period)


def wave_rand(min_time=0, max_time=0.4):
    while True:
        period = random.uniform(min_time, max_time)
        for pin in pins:
            GPIO.output(pin['pin_num'], GPIO.HIGH)
            time.sleep(period)

        period = random.uniform(min_time, max_time)
        for pin in reversed(pins):
            GPIO.output(pin['pin_num'], GPIO.LOW)
            time.sleep(period)


def wave_rand_ex(min_time=0, max_time=0.4):
    while True:
        for pin in pins:
            GPIO.output(pin['pin_num'], GPIO.HIGH)
            time.sleep(random.uniform(min_time, max_time))

        for pin in reversed(pins):
            GPIO.output(pin['pin_num'], GPIO.LOW)
            time.sleep(random.uniform(min_time, max_time))