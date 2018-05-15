from requests import Session
from signalr import Connection
import threading
from loggingManager import *
from uploadImageManager import *
from displayManager import *
from servoManager import *
import time

def log(message, withTimestamp=False):
    logInfo('signalrManager', message, withTimestamp)

HUB_HOST_URL = "http://likkleapi-staging.azurewebsites.net/signalr"
HUB_NAME = 'PeepneeHub'

## SignalR event handlers
def mailRequestAccepted():
    dropPackageInside()
    openMailbox()
    time.sleep(5)
    closeMailbox()
    showHomeScreen()

def mailRequestDeclined():
    packageRejected()
    time.sleep(5)
    showHomeScreen()

def repeatMailRequest():
    repeatSteps()
    time.sleep(5)
    goOnMarkerAndPushButton()

def updateDefaultOwnerSettings(openAfterDefaultTime, secondsToDefaultBehaviour):
    log("Kewl? Update settings to openAfterDefaultTime: {0} and secondsToDefaultBehaviour: {1}".format(openAfterDefaultTime, secondsToDefaultBehaviour))

def print_error(error):
    log('error: ', error)
## SignalR event handlers

## Invoke SignalR events
def sendNewMailRequest():
    t1 = threading.Thread(target=sendNewMailRequestInSeparateThread, args=[])
    t1.setDaemon(True)
    t1.start()
## Invoke SignalR events

def sendNewMailRequestInSeparateThread():
    with Session() as session:
        upload_result = uploadImage()

        #create a connection
        connection = Connection(HUB_HOST_URL, session)

        #get PeepneeHub hub
        peepneeHub = connection.register_hub(HUB_NAME)

        peepneeHub.client.on('mailRequestAccepted', mailRequestAccepted)
        peepneeHub.client.on('mailRequestDeclined', mailRequestDeclined)
        peepneeHub.client.on('repeatMailRequest', repeatMailRequest)
        peepneeHub.client.on('updateDefaultOwnerSettings', updateDefaultOwnerSettings)

        #process errors
        connection.error += print_error

        #start a connection
        log("Connection was started", True)
        with connection:
            peepneeHub.server.invoke('newMailRequest', upload_result['link'], "OCR PARSED TEXT")
            connection.wait(16)
            log("Connection to SignalR hub was closed!", True)
