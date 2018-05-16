import time

def logInfo(source, infoMessage, withTimestamp):
    if withTimestamp:
        print('\n[{0} @ {1}]: {2}\n'.format(source, time.strftime("%H:%M:%S"), infoMessage))
    else:
        print('\n[{0}]: {1}\n'.format(source, infoMessage))
