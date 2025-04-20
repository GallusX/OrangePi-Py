# OrangePi-Py

## Устанавливаем всё необходимое

### WiringOP:

```bash
apt-get update
apt-get install -y git
apt-get install python3
apt-get install pip
apt-get install python3-dev
git clone https://github.com/orangepi-xunlong/wiringOP.git
cd wiringOP
./build clean
./build
```

### i2c-tools:

```bash
sudo apt install i2c-tools
```

### Библиотеки для Python:

```bash
pip install pillow
pip install smbus2
```

### И OpiGallus:

**Через pip:**

```bash
pip install opigallus
```

**Через git с примерами и шрифтами:**

```bash
git clone https://github.com/GallusX/OrangePi-Py
cd OrangePi-Py
python3 setup.py install
```

Небольшая библиотека для обучения и простого программирования GPIO-выходов на OrangePi на языке Python, а также для управления OLED-дисплеем SSD1306.

---

## После установки проверяем работоспособность

```bash
gpio readall
```

Команда выведет список пинов:

![Снимок](https://user-images.githubusercontent.com/109997469/213883530-d5d7c2ce-801f-48ce-9de8-79f0aba6fc40.PNG)

Отобразятся все порты, их назначения и состояния.

---

Теперь проверяем i2c-tools. Вводим:

```bash
i2cdetect -y 0
```

![image](https://user-images.githubusercontent.com/109997469/213883773-4279298a-b6df-4503-9e6e-e637b833b0b4.png)

```bash
i2cdetect -y 1
```

![image](https://user-images.githubusercontent.com/109997469/213883811-e12ca8b4-7e7f-4477-a6a4-486ea482e288.png)

Если везде прочерки — значит, к плате ничего не подключено. Иногда появляется `UU`, `0x30` или `0x20` — это может означать, что I2C не включён.

---

## Подключаем SSD1306 к плате

Смотрите распиновки дисплея и OrangePi. Всё подключаем строго по распиновке!

Распиновка может отличаться в зависимости от модели OrangePi и самого дисплея SSD1306.

- GND — к любому GND на OrangePi
- VCC — к 3.3V на OrangePi
- SDA — к SDA (он один)
- SCL — к SCL (он один)

Это в моём случае. На некоторых моделях SSD1306 могут быть дополнительные пины.

---

## Включаем I2C

**Если после подключения SSD1306 и команды `i2cdetect -y 0` всё ещё везде прочерки — нужно включить I2C в системе.**

### Для систем Debian, Ubuntu, Armbian:

```bash
sudo orangepi-config
```

Выбираем:

- **System**

![image](https://user-images.githubusercontent.com/109997469/213906914-51f89a4f-5ee3-4221-88d6-2c47605d18d3.png)

- **Bootenv**

![image](https://user-images.githubusercontent.com/109997469/213906949-f1910652-02a9-4935-b4db-95b8a5d70cc6.png)

Добавляем строку:

```bash
overlays=i2c0 i2c1 i2c2
```

![image](https://user-images.githubusercontent.com/109997469/213907001-27a01747-ceac-42ec-af10-1ebc0052389d.png)

Нажимаем **Save** и перезагружаем OrangePi:

```bash
reboot
```

После перезагрузки вводим:

```bash
i2cdetect -y 0
```

![image](https://user-images.githubusercontent.com/109997469/213907053-fcd40395-d340-4002-b09e-a4cab1bc4565.png)

`3C` — это адрес нашего дисплея.

---

## Включаем SPI

### Для систем Debian, Ubuntu, Armbian:

```bash
sudo orangepi-config
```

Выбираем:

- **System**
- **Bootenv**

Добавляем строки:

```bash
spi_spidev1
param_spidev_spi_bus=0
param_spidev_spi_cs=0
param_spidev_max_freq=1000000
```

![image](https://user-images.githubusercontent.com/109997469/230782067-76ea013a-6e83-46d6-b4da-6332011303ca.png)

**Важно!** На некоторых платах OrangePi только один SPI. Смотрите по распиновке.  
Если только один — пишите `spi_spidev1`.  
Если два — пишите:

```bash
spi_spidev
spi_spidev1
```

![image](https://user-images.githubusercontent.com/109997469/230782448-e6fff34f-cd6c-4a65-981b-5188bce39ba4.png)

Пример: на OrangePi 3 LTS доступен только `spi1`, поэтому пишем `spi_spidev1`.

Перезагружаем:

```bash
reboot
```

Проверяем:

```bash
ls -l /dev/*spi*
```

Если всё настроено правильно, появятся SPI-порты:

![image](https://user-images.githubusercontent.com/109997469/230782225-661cc89e-4001-47ed-9e64-026533415297.png)

Устанавливаем библиотеку:

```bash
pip install spidev
```

---

## Как пользоваться

```python
gpio_out(НОМЕР_ПИНА)         # Устанавливаем пин как выход
gpio_up(НОМЕР_ПИНА)          # Подаём сигнал
gpio_down(НОМЕР_ПИНА)        # Убираем сигнал

gpio_rele(НОМЕР_ПИНА)        # Добавляем реле
gpio_rup(НОМЕР_ПИНА)         # Включаем реле
gpio_rdown(НОМЕР_ПИНА)       # Выключаем реле

gpio_button(НОМЕР_ПИНА)      # Подключаем кнопку
gpio_pull_up(НОМЕР_ПИНА)     # Подтягивающий резистор к +3.3В
gpio_pull_down(НОМЕР_ПИНА)   # Подтягивающий резистор к GND

butclick(НОМЕР_ПИНА)         # Получаем значение кнопки
```

---

## Насчёт шрифтов

Чтобы менять размер текста на экране (`ImageFont.truetype`) — выберите и скачайте нужный шрифт, затем скопируйте его в:

```
/usr/share/fonts
```

Если папки нет — создайте её.  
Один подходящий шрифт уже лежит в папке `fonts` в репозитории — просто перенесите его.

---

## Пример использования SSD1306

```python
from opigallus import *
from opigalluss.display import ssd1306
from opigalluss.draw import canvas
from PIL import ImageFont, ImageDraw

disp = ssd1306(port=0, address=0x3C, width=128, height=64)

with canvas(disp) as draw:
    font = ImageFont.load_default()
    font = ImageFont.truetype('/usr/share/fonts/Ваш_шрифт.ttf', size=18)
    draw.rectangle((0, 0, 128, 64), outline=0, fill=0)
    draw.text((0, 0), "Hello world!", font=font, fill=255)
```

---

## Изображение на дисплее

```python
from PIL import Image
image = Image.open('/путь/к/изображению.png').convert("RGBA")
draw.bitmap((0, 0), image, fill=255)
```

![photo_2023-01-21_12-54-35](https://user-images.githubusercontent.com/109997469/213861709-a8f1a529-b42a-4f00-a1bc-a1e19c210605.jpg)

---

## По всем вопросам:

Telegram: [@galluis](https://t.me/galluis)