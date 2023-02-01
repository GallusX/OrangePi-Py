from opigallus import*
from opigallus.display import ssd1306
from opigallus.draw import canvas
from PIL import ImageFont, ImageDraw, Image
import time
import socket

disp = ssd1306(port=0, address=0x3C, width=128, height=64)  # rev.1 users set port=0
with canvas(disp) as draw:
    font = ImageFont.load_default()
    image =Image.open('0.png').convert("RGBA")
    draw.bitmap((0, 0), image, fill=255)
