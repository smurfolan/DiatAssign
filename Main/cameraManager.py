from picamera import PiCamera
from time import sleep

def takePictureWithTheCamera():
    camera = PiCamera()
    try:
        print("About to take a picture...")
        camera.start_preview()
        sleep(5)
        camera.capture('/home/pi/Desktop/GitRepo/DiatAssign/Main/latestShot.jpg', use_video_port=True)
        camera.stop_preview()
        print("Picture taken!")
    finally:
        camera.close()