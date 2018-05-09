import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
servoPin=13
GPIO.setup(servoPin, GPIO.OUT)
pwm=GPIO.PWM(servoPin,50)
pwm.start(7.6)
for i in range(0,20):
	desiredPosition=input("Where do you want the servo(0-180)?")
	DC=1./18.*(desiredPosition)+3
	pwm.ChangeDutyCycle(DC)
pwm.stop()
GPIO.cleanup()
