from loggingManager import *
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

pwm=GPIO.PWM(13,50)
pwm.start(0)

def log(message, withTimestamp=False):
    logInfo('servoManager', message, withTimestamp)

def SetAngle(angle):
        global pwm

	duty = angle/18 + 2
	GPIO.output(13, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(13, False)
	pwm.ChangeDutyCycle(0)

def openMailbox():
    log('Opening mailbox...', True)
    SetAngle(90)
    # changeServoPosition(80)
    log('Mailbox is now open!', True)

def closeMailbox():
    log('Closing mailbox...', True)
    SetAngle(180)
    # changeServoPosition(180)
    log('Mailbox is now closed!', True)
