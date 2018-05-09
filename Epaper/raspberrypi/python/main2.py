import RPi.GPIO as GPIO
import epd2in9
import time
import Image
import ImageDraw
import ImageFont

from displayManager import *
from signalrManager import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
    initSignalrConnection()
    showHomeScreen()

    while True:
        button_state = GPIO.input(23)
        if button_state == False:
            requestForPackgeToBeShown()
            time.sleep(3)
            countDownFrom(6)

if __name__ == '__main__':
    main()
