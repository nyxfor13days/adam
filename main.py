# Imports
from time import sleep

try:
    import RPi.GPIO as GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
except ImportError:
    print("Error: RPi.GPIO not found")

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from packages.speak import Speak
from packages.listen import Listen
from data import pins


class Main:
    pins = pins()
    lemmatizer = WordNetLemmatizer()

    def __init__(self, speech):
        command = self.speech_processing(speech)


    def speech_processing(self, speech):
        # ToDo: improve tokenizer for words like can't, won't, etc.
        tokenized_sentence = word_tokenize(speech)
        processed_command = []

        for word in tokenized_sentence:
            processed_command.append(self.lemmatizer.lemmatize(word))

        return processed_command

    def lights(self, command):
        light_pins = self.pins['lights']

        for pin in light_pins:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

        if "light" in command:
            if "on" in command:
                for pin in light_pins:
                    GPIO.output(pin, GPIO.HIGH)

                    if GPIO.input(pin) == GPIO.HIGH:
                        print("The light is on")

            elif "off" in command:
                for pin in light_pins:
                    GPIO.output(pin, GPIO.LOW)

                    if GPIO.input(pin) == GPIO.LOW:
                        print("The light is off")


if __name__ == "__main__":
    try:
        while True:
            command = input("Command: ")
            Main(command)

    except KeyboardInterrupt:
        sleep(0.3)
        print("\n\nExiting...")

    finally:
        sleep(0.3)
        print("Cleaning Up...")
        GPIO.cleanup()
