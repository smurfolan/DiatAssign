import epd2in9
import ImageDraw
from PIL import Image
import time
import ImageFont

HOME_SCREEN = 'semPetroviHome_132_by_300.jpg'
SHOW_THE_PACKAGE = 'showThePackage_132_by_300.jpg'

def showHomeScreen():
    displayPicture(HOME_SCREEN)
    return

def requestForPackgeToBeShown():
    displayPicture(SHOW_THE_PACKAGE)
    return

def countDownFrom(number):
    epd = epd2in9.EPD()
    epd.init(epd.lut_partial_update)

    epd.clear_frame_memory(0xFF)
    epd.display_frame()
    epd.clear_frame_memory(0xFF)
    epd.display_frame()

    time_image = Image.new('1', (100, 100), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(time_image)
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 56)
    image_width, image_height = time_image.size

    counter = number
    while (counter >= 0):
        draw.rectangle((0, 0, image_width, image_height), fill = 255)
        draw.text((0, 0), '0{0}'.format(str(counter)), font = font, fill = 0)
        epd.set_frame_memory(time_image.rotate(270), 0, 120)
        epd.display_frame()

        counter = counter - 1
        time.sleep(1)

def displayPicture(pictureName):

    epd = epd2in9.EPD()
    epd.init(epd.lut_full_update)

    image = Image.open(pictureName)

    epd.clear_frame_memory(0xFF)
    epd.set_frame_memory(image, 0, 0)
    epd.display_frame()

    epd.delay_ms(2000)

    return
