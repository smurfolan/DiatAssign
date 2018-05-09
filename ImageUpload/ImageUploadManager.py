from imgurpython import ImgurClient

client_id = 'ba35f2338629ae3'
client_secret = '135b0802c89ea1fac80ce5a0f6cdf3d6713e825d'

PATH = "/home/pi/Desktop/Camera/latestShot.jpg"

client = ImgurClient(client_id, client_secret)

uploaded_image = client.upload_from_path(PATH, config=None, anon=True)

print(uploaded_image['width'])
print(uploaded_image['height'])
print(uploaded_image['type'])
print(uploaded_image['link'])
