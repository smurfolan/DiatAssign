import RPi.GPIO as GPIO
import epd2in9
import time
import Image
import ImageDraw
import ImageFont

from displayManager import *
from signalrManager import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

def buttonPress(channel):
    print("Button pressed")

GPIO.add_event_detect(23, GPIO.RISING, callback=buttonPress)

def main():
    # initSignalrConnection()
    showHomeScreen()

    t_end = time.time()+3
    while time.time() < t_end:
        print("Holla")
   # while True:
       # button_state = GPIO.input(23)

        # Button was clicked
    #    if button_state == False:

     #       goOnMarkerAndPushButton()

      #      t_end = time.time() + 3
           # while time.time() < t_end:
            #    print("Holla")
                # if GPIO.input(23): #GPIO.wait_for_edge(23, GPIO.FALLING):
                # takingPicture()

           # print("Out of while loop")
           # break
            # We wait for 5 seconds.
            # If no push was registered in that time we move to home screen.
           # pointInTime = time.time()
           # if (button_state == False) and (time.time()-pointInTime < 6):
           #     takingPicture()
           # showHomeScreen()
           # countDownFrom(6)
   # print("Out of WHile(1) loop")
    print("Calling GPIO.cleanup()")
    GPIO.cleanup()
if __name__ == '__main__':
    main()
