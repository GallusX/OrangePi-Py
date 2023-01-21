# OrangePi-GpioPy
## ДЛЯ ИСПОЛЬЗОВАНИЯ БИБЛИОТЕКИ НЕОБХОДИМО УСТАНОВИТЬ WiringOP

    git clone https://github.com/zhaolei/WiringOP.gi

    cd WiringOP

    chmod +x ./build

    sudo ./build

после установки проверяем работоспособность

    gpio readall

покажет все порты, назначения и состояния
## ДЛЯ ИСПОЛЬЗОВАНИЯ SSD1306 НЕОБХОДИМО УСТАНОВИТЬ 2 БИБЛИОТЕКИ

    pip install pillow
    pip install smbus2
## Устанавливаем библиотеку 

    pip install OPiGallus

Не большая библиотека для обучения

И для простого программирования GPIO выходов на OrangePi на языке Python
И управления oled дисплеем ssd1306
## Как пользоваться
Ввыбираем пин для вывода:

    gpout(НОМЕР ПИНА) 
Подаем сигнал на пин:

    gpoup(НОМЕР ПИНА)
Отключаем сигнал на пин:

    gpdown(НОМЕР ПИНА)
Добавляем реле в систему:

    gprele(НОМЕР ПИНА)
Включаем реле:

    gprup(НОМЕР ПИНА)
Отключаем реле:

    gprdown(НОМЕР ПИНА)
##ПРМИЕР ИСПОЛЬЗОВАНИЯ ssd1306

    from opigalus import*
    from opigalluss.display import ssd1306
    from opigalluss.draw import canvas
    from PIL import ImageFont, ImageDraw
    import time

    disp = ssd1306(port=0, address=0x3C, width=128, height=64)  # rev.1 users set port=0
    with canvas(disp) as draw:
        font = ImageFont.load_default()
        font = ImageFont.truetype('/21158.ttf', size=18)
        draw.rectangle((0, 0, 128, 64), outline=0, fill=0)
        draw.text((0, 0), "MAKS LOH 228", font=font, fill=255)
