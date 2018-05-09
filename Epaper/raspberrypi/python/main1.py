import epd2in9
import time
import Image
import ImageDraw
import ImageFont

def main():
    epd = epd2in9.EPD()
    epd.init(epd.lut_full_update)

    # Clear display
    image = Image.new('1', (epd2in9.EPD_WIDTH, epd2in9.EPD_HEIGHT), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)

    # Create new image with some text
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 16)

    draw.text((0,0), 'RENI', font = font, fill = 0)
    draw.text((0,20), time.strftime('%d/%m/%Y'), font = font, fill = 0)

    # Show new created image rotated by 90 degrees
    img = image  #.rotate(90,expand=True)
##
 # there are 2 memory areas embedded in the e-paper display
 # and once the display is refreshed, the memory area will be auto-toggled,
 # i.e. the next action of SetFrameMemory will set the other memory area
# therefore you have to set the frame memory twice.
##
    epd.clear_frame_memory(0xFF)
    epd.display_frame()
    epd.clear_frame_memory(0xFF)
    epd.display_frame()

    # for partial update
    epd.init(epd.lut_partial_update)
   # img = Image.open('monocolor.bmp')
##
# there are 2 memory areas embedded in the e-paper display
# and once the display is refreshed, the memory area will be auto-toggled,
# i.e. the next action of SetFrameMemory will set the other memory area
# therefore you have to set the frame memory twice.
##
    epd.set_frame_memory(img, 0, 0)
    epd.display_frame()
    epd.set_frame_memory(img, 0, 0)
    epd.display_frame()

if __name__ == '__main__':
     main()
