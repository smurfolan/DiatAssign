import os
from imgurpython import ImgurClient
from loggingManager import *

CLIENT_ID = 'ba35f2338629ae3'
CLIENT_SECRET = '135b0802c89ea1fac80ce5a0f6cdf3d6713e825d'

PATH = "/home/pi/Desktop/GitRepo/DiatAssign/Main/latestShot.jpg"

def log(message, withTimestamp=False):
    logInfo('uploadImageManager', message, withTimestamp)

def uploadImage():
    try:
        log("Uploading image to Imgur.com...", True)
        client = ImgurClient(CLIENT_ID, CLIENT_SECRET)
        uploaded_image = client.upload_from_path(PATH, config=None, anon=True)
        log("Image successfully uploaded to Imgur.com!", True)

        return uploaded_image
    except BaseException as e:
        log('Failed to upload image to Imgur.com: ' + str(e))

