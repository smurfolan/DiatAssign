from requests import Session
from signalr import Connection

HUB_URL = "http://likkleapi-staging.azurewebsites.net/signalr"
HUB_NAME = 'BoongalooGroupsActivityHub'

### create new chat message handler
def groupWasLeftByUserHandler(leftGroupId):
    print('OMG! Group that was left: ', leftGroupId)

def signalrErrorHandler(error):
    print('error: ', error)

def initSignalrConnection():
    with Session() as session:
        #create a connection
        connection = Connection(HUB_URL, session)

        #get BoongalooGroupsActivityHub hub
        boongalooGroupsActivityHub = connection.register_hub(HUB_NAME)

        #receive new message from the hub
        boongalooGroupsActivityHub.client.on('groupWasLeftByUser', groupWasLeftByUserHandler)

        #process errors
        connection.error += signalrErrorHandler

        #start a connection
        connection.qs = {'userId':'5b8e69b6-fc13-494d-9228-4215de85254f'}

        print("Connection was started")
        with connection:
            connection.wait(13)
