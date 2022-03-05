# Imports
import RPi.GPIO as GPIO
from packages.speak import Speak
from packages.listen import Listen
from data import pins


class Main:
    pins = pins()

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

    def lights(self):
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)


if __name__ == "__main__":
    Main()
