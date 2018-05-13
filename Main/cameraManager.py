from picamera import PiCamera
from time import sleep
from loggingManager import *

def log(message, withTimestamp=False):
    logInfo("cameraManager", message, withTimestamp)

def takePictureWithTheCamera():
    camera = PiCamera()
    try:
        log("About to take a picture...")
        camera.start_preview()
        sleep(5)
        camera.capture('/home/pi/Desktop/GitRepo/DiatAssign/Main/latestShot.jpg', use_video_port=True)
        camera.stop_preview()
        log("Picture taken!")
    finally:
        camera.close()
