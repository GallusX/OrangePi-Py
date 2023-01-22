import smbus2 as smbus


class disp(object):


    def __init__(self, port=0, address=0x3C, cmd_mode=0x00, data_mode=0x40):
        self.cmd_mode = cmd_mode
        self.data_mode = data_mode
        self.bus = smbus.SMBus(port)
        self.addr = address

    def command(self, *cmd):

        assert(len(cmd) <= 32)
        self.bus.write_i2c_block_data(self.addr, self.cmd_mode, list(cmd))

    def data(self, data):

        for i in range(0, len(data), 32):
            self.bus.write_i2c_block_data(self.addr,
                                          self.data_mode,
                                          list(data[i:i+32]))



class ssd1306(disp):

    def __init__(self, port=0, address=0x3C, width=128, height=32):
        super(ssd1306, self).__init__(port, address)
        self.width = width
        self.height = height
        self.pages = int(self.height / 8)

        self.command(
            const.DISPLAYOFF,
            const.SETDISPLAYCLOCKDIV, 0x80,
            const.SETMULTIPLEX,       0x3F,
            const.SETDISPLAYOFFSET,   0x00,
            const.SETSTARTLINE,
            const.CHARGEPUMP,         0x14,
            const.MEMORYMODE,         0x00,
            const.SEGREMAP,
            const.COMSCANDEC,
            const.SETCOMPINS,         0x12,
            const.SETCONTRAST,        0xCF,
            const.SETPRECHARGE,       0xF1,
            const.SETVCOMDETECT,      0x40,
            const.DISPLAYALLON_RESUME,
            const.NORMALDISPLAY,
            const.DISPLAYON)

    def display(self, image):

        assert(image.mode == '1')
        assert(image.size[0] == self.width)
        assert(image.size[1] == self.height)

        self.command(
            const.COLUMNADDR, 0x00, self.width-1,  # Column start/end address
            const.PAGEADDR,   0x00, self.pages-1)  # Page start/end address

        pix = list(image.getdata())
        step = self.width * 8
        buf = []
        for y in range(0, self.pages * step, step):
            i = y + self.width-1
            while i >= y:
                byte = 0
                for n in range(0, step, self.width):
                    byte |= (pix[i + n] & 0x01) << 8
                    byte >>= 1

                buf.append(byte)
                i -= 1

        self.data(buf)


class const:
    CHARGEPUMP = 0x8D
    COLUMNADDR = 0x21
    COMSCANDEC = 0xC8
    COMSCANINC = 0xC0
    DISPLAYALLON = 0xA5
    DISPLAYALLON_RESUME = 0xA4
    DISPLAYOFF = 0xAE
    DISPLAYON = 0xAF
    EXTERNALVCC = 0x1
    INVERTDISPLAY = 0xA7
    MEMORYMODE = 0x20
    NORMALDISPLAY = 0xA6
    PAGEADDR = 0x22
    SEGREMAP = 0xA0
    SETCOMPINS = 0xDA
    SETCONTRAST = 0x81
    SETDISPLAYCLOCKDIV = 0xD5
    SETDISPLAYOFFSET = 0xD3
    SETHIGHCOLUMN = 0x10
    SETLOWCOLUMN = 0x00
    SETMULTIPLEX = 0xA8
    SETPRECHARGE = 0xD9
    SETSEGMENTREMAP = 0xA1
    SETSTARTLINE = 0x40
    SETVCOMDETECT = 0xDB
    SWITCHCAPVCC = 0x2
