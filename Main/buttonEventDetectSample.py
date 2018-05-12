import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from displayManager import *
from cameraManager import *
import threading

inputPin = 23
GPIO.setup(inputPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

## Define button status variables
firstButtonClickRegistered = False
firstButtonClickRegisteredAt = time.time()
secondButtonClickRegistered = False
## Define button status variables

def expectSecondClickFor(secondsToWait):
    print("Started waiting for", secondsToWait, " seconds..")
    t_end = time.time() + secondsToWait
    while time.time() < t_end:
        continue
    print("	Waiting for second click finished")

    if not secondButtonClickRegistered:
        print("\nShowing home screen..")
        showHomeScreen()
        print("           Home screen shown!")
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
    print("									BUTTON CLICKED")
    if not firstButtonClickRegistered:
        firstButtonClickRegistered = True
        print("\nShowing the _Please stepback and push_ message...")
        goOnMarkerAndPushButton()
        print("		Message shown!")
        # Start counting the seconds till the second click. If no click was registered
        t1 = threading.Thread(target=expectSecondClickFor, args=[6])
        #Background thread will finish with the main program
        t1.setDaemon(True)
        #Start expectSecondClickFor(n) in a separate thread
        t1.start()
        print("Update datetime first time button was clicked")
        firstButtonClickRegisteredAt = time.time()

    elif (firstButtonClickRegistered) and (not secondButtonClickRegistered) and (time.time()-firstButtonClickRegisteredAt > 3):
        print(time.time()-firstButtonClickRegisteredAt)
        secondButtonClickRegistered = True

        print("\nShowing the _We are taking picture_ message...")
        takingPicture()
        print("		Message shown!")
        takePictureWithTheCamera()
        countDownFrom(6)

GPIO.add_event_detect(23,GPIO.RISING,callback=buttonPressHandler)

while(1):
      print("\nShowing home screen..")
      showHomeScreen()
      print("		Home screen shown!")







      keypressed = raw_input('1. Press \'q\' to quit\n2. Press \'r\' to reset ')
      if keypressed == 'q':
           GPIO.cleanup()
           break
      elif keypressed == 'r':
           GPIO.cleanup()
           print("Here we should [r]eset the script.")
      elif keypressed != 'q' and keypressed != 'r':
           print("You pressed other key:" + keypressed)
      else:
           print("Unknown input")
