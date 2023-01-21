# OrangePi-GpioPy
## ДЛЯ ИСПОЛЬЗОВАНИЯ БИБЛИОТЕКИ НЕОБХОДИМО УСТАНОВИТЬ WiringOP, i2c-tools

     apt-get update
     apt-get install -y git
     git clone https://github.com/orangepi-xunlong/wiringOP.git
     cd wiringOP
     ./build clean
     ./build 
    
    
    sudo apt install i2c-tools

после установки проверяем работоспособность

    gpio readall 
    
Должен выдать список пинов:
![Снимок](https://user-images.githubusercontent.com/109997469/213883530-d5d7c2ce-801f-48ce-9de8-79f0aba6fc40.PNG)


покажет все порты, назначения и состояния
теперь проверяем i2c-tools
вводим:

     i2cdetect -y 0
     ![image](https://user-images.githubusercontent.com/109997469/213883773-4279298a-b6df-4503-9e6e-e637b833b0b4.png)
     i2cdetect -y 1
     ![image](https://user-images.githubusercontent.com/109997469/213883811-e12ca8b4-7e7f-4477-a6a4-486ea482e288.png)
везде прочерки потому что к плате ничего не подключено 

     
## ДЛЯ ИСПОЛЬЗОВАНИЯ SSD1306 НЕОБХОДИМО УСТАНОВИТЬ 2 БИБЛИОТЕКИ

    pip install pillow
    pip install smbus2
## Устанавливаем библиотеку 

    pip install opigallus

Небольшая библиотека для обучения

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
    



## На счет шрифтов 


чтобы менять размер текста на экране (ImageFont.truetype) нужно выбрать и скачать нужный вам шрифт и закинуть в папку /usr/share/fonts
если такой папки нету создаем её



## ПРМИЕР ИСПОЛЬЗОВАНИЯ ssd1306

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

