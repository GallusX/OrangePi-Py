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

    from opigallus import* #Импортируем библиотеку
    from opigalluss.display import ssd1306 #имортируем девайс
    from opigalluss.draw import canvas #импортируем библиотеку для вывода на исплей
    from PIL import ImageFont, ImageDraw #импортируем библиотеку которая будет рисовать 

    disp = ssd1306(port=0, address=0x3C, width=128, height=64)  #инициализируем дисплей
    with canvas(disp) as draw: #дальше уже работаем с pillow 
        font = ImageFont.load_default()#загружаем дефолтные настройки шрифта
        font = ImageFont.truetype('/НАЗВАНИЕ ШРИФТА', size=18)#Шрифт вы предвадительно скачиваетеи скидываете в системную папку со всеми шрифтами 
        draw.rectangle((0, 0, 128, 64), outline=0, fill=0)#Очищаем поверхность дисплея
        draw.text((0, 0), "Hello world!", font=font, fill=255)#Выводим текст
        
![photo_2023-01-21_12-54-35](https://user-images.githubusercontent.com/109997469/213861709-a8f1a529-b42a-4f00-a1bc-a1e19c210605.jpg)

