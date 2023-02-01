# OrangePi-Py
## Устанавливаем всё необходимое
WiringOP:

     apt-get update
     apt-get install -y git
     apt-get install python3
     apt-get install pip
     apt-get install python3-dev
     git clone https://github.com/orangepi-xunlong/wiringOP.git
     cd wiringOP
     ./build clean
     ./build
     
I2c-toos:

    sudo apt install i2c-tools

Библиотеки для python:

    pip install pillow
    pip install smbus2
    
И OpiGallus:

Через pip:

    pip install opigallus

Через git с примерами и шрифтами

     git clone https://github.com/GallusX/OrangePi-Py
     cd OrangePi-Py
     python3 setup.py install

Небольшая библиотека для обучения

И для простого программирования GPIO выходов на OrangePi на языке Python

И управления oled дисплеем ssd1306
    
## После установки проверяем работоспособность

    gpio readall 
    
Должен выдать список пинов:
![Снимок](https://user-images.githubusercontent.com/109997469/213883530-d5d7c2ce-801f-48ce-9de8-79f0aba6fc40.PNG)


покажет все порты, назначения и состояния


Теперь проверяем i2c-tools


Вводим:

     i2cdetect -y 0
   ![image](https://user-images.githubusercontent.com/109997469/213883773-4279298a-b6df-4503-9e6e-e637b833b0b4.png)
   
     i2cdetect -y 1
   ![image](https://user-images.githubusercontent.com/109997469/213883811-e12ca8b4-7e7f-4477-a6a4-486ea482e288.png)
   
везде прочерки потому что к плате ничего не подключено (Может ещё появится UU и 30 или 20 но не обращайте на это внимание) 

## Подключаем ssd1306 к плате 

СМОТРИМ РАСАПИНОВКИ ДИСПЛЕЯ И ORANGEPI ВСЁ ПОДКЛЮЧАЕМ ЧИСТО ПО РАСПИНОВКЕ 

Всё зависит от модели orangepi и ssd1306 на всех моделях распиновки разные

gnd - на любой gnd orangepi 

vcc - на 3.3v orangepi

sda - sda на orangepi он там один 

sck - sck на orangepi он там один

Это в моем случае 

На некоторых моделях ssd1306 могут быть другие пины и их может быть больше

## ВКЛЮЧАЕМ I2C 

ЕСЛИ У ВАС ПОДКЛЮЧЕН ssd1306 И ПОСЛЕ КОМАНДЫ i2cdetect -y 0 ВСЁ РАВНО ВЕЗДЕ ПРОЧЕРКИ НУЖНО ВКЛЮЧИТЬ I2c В СИСТЕМЕ

### Система Debian, Ubuntu, Armbian:

Вводим:

    sudo orangepi-config
Выбираем System
![image](https://user-images.githubusercontent.com/109997469/213906914-51f89a4f-5ee3-4221-88d6-2c47605d18d3.png)

Выбираем Bootenv
![image](https://user-images.githubusercontent.com/109997469/213906949-f1910652-02a9-4935-b4db-95b8a5d70cc6.png)

Здесь добавляем строчку 
     
     overlays=i2c0 i2c1 i2c2
     

![image](https://user-images.githubusercontent.com/109997469/213907001-27a01747-ceac-42ec-af10-1ebc0052389d.png)

Нажимаем save и перезагружаем orangepi 

После перезагрузки вводим i2cdetect -y 0 и получаем
![image](https://user-images.githubusercontent.com/109997469/213907053-fcd40395-d340-4002-b09e-a4cab1bc4565.png)

3с это адресс нашего дисплея

## Как пользоваться
Выбираем пин для вывода:

    gpio_out(НОМЕР ПИНА) 
Подаем сигнал на пин:

    gpio_up(НОМЕР ПИНА)
Отключаем сигнал на пин:

    gpio_down(НОМЕР ПИНА)
Добавляем реле в систему:

    gpio_rele(НОМЕР ПИНА)
Включаем реле:

    gpio_rup(НОМЕР ПИНА)
Отключаем реле:

    gpio_rdown(НОМЕР ПИНА)
Добавляем кнопку в систему:
     
     gpio_button(НОМЕР ПИНА)
Включаем подтягивающий резистор на 1:
     
     gpio_pull_up(НОМЕР ПИНА)
Включаем подтягивающий резистор на 0:

     gpio_pull_down(НОМЕР ПИНА)
Узнаем значение кнопки для обработчика кнопок:
     
     butclick(НОМЕР ПИНА)

## Насчет шрифтов 


чтобы менять размер текста на экране (ImageFont.truetype) нужно выбрать и скачать нужный вам шрифт и закинуть в папку /usr/share/fonts
если такой папки нет создаем её (Один хорошо подходящий шрифт оставил в папке fonts в репозитории просто перенесите его в /usr/share/fonts)



## ПРИМЕР ИСПОЛЬЗОВАНИЯ ssd1306

В папке examples есть примеры по работе с ssd1306

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
       
------------------------------------
Изображение выводится так:

        image =Image.open('/Путь к картинке').convert("RGBA")
        draw.bitmap((0, 0), image, fill=255)
        
![photo_2023-01-21_12-54-35](https://user-images.githubusercontent.com/109997469/213861709-a8f1a529-b42a-4f00-a1bc-a1e19c210605.jpg)



По всем вопросам:

Telegram: @Gallusis
