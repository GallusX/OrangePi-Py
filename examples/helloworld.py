#Импорт библиотек-------------------------
from opigallus import*                   #
from opigallus.display import ssd1306    # 
from opigallus.draw import canvas        #    
from PIL import ImageFont, ImageDraw     #
#Импорт библиотек-------------------------
disp = ssd1306(port=0, address=0x3C, width=128, height=64)#инициализируем дисплей
#ssd1306(port=Это номер порта где вам выдает адресс экрана i2cdetect -y 0 или i2cdetect -y 1, address=Это адресс дисплея который выдается в i2cdetect,
#width=,height=) - это размеры дисплея всегда оставляйте 128х64 даже есть у вас 128х32 всё будет работать нормально
with canvas(disp) as draw:#Создаем холст на дисплее//Дальше работаем с pillow 
    font = ImageFont.load_default()#Загружаем стандартные настройки шрифта
    font = ImageFont.truetype('/oled', size=23)#Загружаем шрифт//скидываем в папку /usr/share/fonts если такой папки нет создаем её
    #ШРИФТ oled Я ОСТАВИЛ В ПАПКЕ fonts ДЛЯ ТОГО ЧТОБЫ КОД ЗАРАБОТАЛ ПЕРЕНЕСИТЕ ШРИФТ В ПАПКУ /usr/share/fonts ЕСЛИ ТАКОЙ НЕТ ТО СОЗДАЙТЕ ЕЁ
    draw.rectangle((0, 0, 128, 64), outline=0, fill=0)#Очищаем дисплей
    draw.text((0, 0), "Hello world!", font=font, fill=255)#Пишем текст
    #Где (0,0) это координаты где вы будет выводится текст 
    
