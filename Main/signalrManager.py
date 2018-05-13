from requests import Session
from signalr import Connection
import threading
from loggingManager import *
from uploadImageManager import *

def log(message, withTimestamp=False):
    logInfo('signalrManager', message, withTimestamp)

HUB_HOST_URL = "http://likkleapi-staging.azurewebsites.net/signalr"
HUB_NAME = 'PeepneeHub'

## SignalR event handlers
def mailRequestAccepted():
    log('OMG! Open box using the servoManager. Count 5 seconds and close the box again using the manager.')

def mailRequestDeclined():
    log('Hmm! Using the displayManager show message for declined mail.')

def repeatMailRequest():
    log('What? Using the displayManager show message repeat is needed. The show home screen.')

def updateDefaultOwnerSettings(openAfterDefaultTime, secondsToDefaultBehaviour):
    log("Kewl? Update settings to openAfterDefaultTime: {0} and secondsToDefaultBehaviour: {1}".format(openAfterDefaultTime, secondsToDefaultBehaviour))

def print_error(error):
    log('error: ', error)
## SignalR event handlers

## Invoke SignalR events
def sendNewMailRequest():
    upload_result = uploadImage()
    log("Sending newMailRequest event to the mobile device (Imgurl url:{0}, OCR text:{1})".format(upload_result['link'], "OCR PARSED TEXT"))
    #peepneeHub.server.invoke('newMailRequest', upload_result['link'], "OCR PARSED TEXT")
## Invoke SignalR events

def initRealTimeUpdatesConnection():
    t1 = threading.Thread(target=startSignalrConnection, args=[])
    t1.setDaemon(True)
    t1.start()

def startSignalrConnection():
    with Session() as session:
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
            #peepneeHub.server.invoke('mailRequestAccepted')
            #peepneeHub.server.invoke('updateDefaultOwnerSettings', 0, 13)
            connection.wait(13)
            log("Connection to SignalR hub was closed!", True)
