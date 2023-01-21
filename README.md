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

    pip install opigpiogalluss

Не большая библиотека для обучения

И для простого программирования GPIO выходов на OrangePi на языке Python 
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
