from picamera import PiCamera
from time import sleep

camera = PiCamera()

print("About to take a picture...")
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/Camera/latestShot.jpg', use_video_port=True)
camera.stop_preview()
print("Picture taken!")
