import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from signalrManager import *
from displayManager import *
from cameraManager import *
import threading
from loggingManager import *

def log(message, withTimestamp=False):
    logInfo('buttonEventDetectSample', message, withTimestamp)

inputPin = 23
GPIO.setup(inputPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

## Define button status variables
firstButtonClickRegistered = False
firstButtonClickRegisteredAt = time.time()
secondButtonClickRegistered = False
## Define button status variables

def expectSecondClickFor(secondsToWait):
    log("Started waiting for {0} seconds...".format(secondsToWait))
    t_end = time.time() + secondsToWait
    while time.time() < t_end:
        continue
    log("Waiting for second click finished")

    if not secondButtonClickRegistered:
        log("Showing home screen..")
        showHomeScreen()
        log("Home screen shown!")
        resetButtonStates()

def resetButtonStates():
    global firstButtonClickRegistered
    global secondButtonClickRegistered

    firstButtonClickRegistered = False
    secondButtonClickRegistered = False

def buttonPressHandler(channel):
    global firstButtonClickRegistered
    global secondButtonClickRegistered
    global firstButtonClickRegisteredAt
    log("BUTTON CLICKED")
    if not firstButtonClickRegistered:
        firstButtonClickRegistered = True
        log("Showing the 'Please stepback and push' message...")
        goOnMarkerAndPushButton()
        log("Message shown!")
        # Start counting the seconds till the second click. If no click was registered
        t1 = threading.Thread(target=expectSecondClickFor, args=[6])
        #Background thread will finish with the main program
        t1.setDaemon(True)
        #Start expectSecondClickFor(n) in a separate thread
        t1.start()
        log("Update datetime first time button was clicked")
        firstButtonClickRegisteredAt = time.time()

    elif (firstButtonClickRegistered) and (not secondButtonClickRegistered) and (time.time()-firstButtonClickRegisteredAt > 3):
        log(time.time()-firstButtonClickRegisteredAt)
        secondButtonClickRegistered = True

        log("Showing the 'We are taking picture' message...")
        takingPicture()
        log("Message shown!")
        takePictureWithTheCamera()
        # TODO:Upload it and send it to Mobile app in different thread
        countDownFrom(6)
        # TODO:Maybe reset buttons after the countdown

GPIO.add_event_detect(23,GPIO.RISING,callback=buttonPressHandler)

initRealTimeUpdatesConnection()

while(1):
      log("Showing home screen..")
      showHomeScreen()
      log("Home screen shown!")

      keypressed = raw_input('\n\n\n\n\n\n***** MENU ***** \n1. Press \'q\' to quit\n2. Press \'r\' to reset (NOT implemented yet)\n***** MENU *****\n\n\n\n\n\n ')

      if keypressed == 'q':
           GPIO.cleanup()
           break
      elif keypressed == 'r':
           GPIO.cleanup()
           log("Here we should [r]eset the script.")
      elif keypressed != 'q' and keypressed != 'r':
           log("You pressed other key:" + keypressed)
      else:
           log("Unknown input")
