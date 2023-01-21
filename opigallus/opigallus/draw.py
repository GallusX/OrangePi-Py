from PIL import Image, ImageDraw

class canvas(object):
    def clear ():
        with canvas(ssd1306(port=0, address=0x3C, width=128, height=64)) as draw:
            draw.rectangle((0, 0, 128, 64), outline=0, fill=0)
    
    def __init__(self, device):
        self.draw = None
        self.image = Image.new('1', (device.width, device.height))
        self.device = device

    def __enter__(self):
        self.draw = ImageDraw.Draw(self.image)
        return self.draw

    def __exit__(self, type, value, traceback):
        if type is None:
            self.device.display(self.image)
        del self.draw   
        return False    
