from requests import Session
from signalr import Connection

with Session() as session:
    #create a connection
    connection = Connection("http://likkleapi-staging.azurewebsites.net/signalr", session)

    #get BoongalooGroupsActivityHub hub
    boongalooGroupsActivityHub = connection.register_hub('BoongalooGroupsActivityHub')

    #create new chat message handler
    def group_was_left_by_user(leftGroupId):
        print('OMG! Group that was left: ', leftGroupId)

    #create error handler
    def print_error(error):
        print('error: ', error)

    #receive new chat messages from the hub
    boongalooGroupsActivityHub.client.on('groupWasLeftByUser', group_was_left_by_user)

    #process errors
    connection.error += print_error

    #start a connection
    connection.qs = {'userId':'5b8e69b6-fc13-494d-9228-4215de85254f'}

    print("Connection was started")
    with connection:
            connection.wait(13)
