import time

def logInfo(source, infoMessage, withTimestamp):
    if withTimestamp:
        print('\n\n[{0} @ {1}]: {2}\n\n'.format(source, time.strftime("%H:%M:%S"), infoMessage))
    else:
        print('\n\n[{0}]: {1}\n\n'.format(source, infoMessage))
