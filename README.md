# OrangePi-Py

Упрощённая библиотека для работы с GPIO и OLED-дисплеями (SSD1306) на OrangePi через Python.

![GPIO](https://user-images.githubusercontent.com/109997469/213883530-d5d7c2ce-801f-48ce-9de8-79f0aba6fc40.PNG)

## Установка

### Зависимости

```bash
apt-get update  
apt-get install -y git python3 python3-dev pip  
apt-get install i2c-tools
```

### WiringOP

```bash
git clone https://github.com/orangepi-xunlong/wiringOP.git  
cd wiringOP  
./build clean  
./build
```

### Python-библиотеки

```bash
pip install pillow smbus2
```

### Установка OrangePi-Py

Через pip:

```bash
pip install opigallus
```

Или с клонированием репозитория:

```bash
git clone https://github.com/GallusX/OrangePi-Py  
cd OrangePi-Py  
python3 setup.py install
```

---

## Проверка GPIO

```bash
gpio readall
```

---

## Проверка I2C

```bash
i2cdetect -y 0  
i2cdetect -y 1
```

Если видны прочерки — устройств нет. Если виден `0x3C`, `0x20` или `UU` — устройство подключено.

---

## Активация I2C

```bash
sudo orangepi-config
```

- **System → Bootenv**
- Добавить:

```bash
overlays=i2c0 i2c1 i2c2
```

Перезагрузите:

```bash
reboot
```

---

## Активация SPI

```bash
sudo orangepi-config
```

- **System → Bootenv**
- Добавить:

```bash
spi_spidev1  
param_spidev_spi_bus=0  
param_spidev_spi_cs=0  
param_spidev_max_freq=1000000
```

Если у вас один SPI, укажите только `spi_spidev1`.

Проверка:

```bash
ls -l /dev/*spi*
```

Установка библиотеки:

```bash
pip install spidev
```

---

## Подключение SSD1306

| Пин дисплея | Пин OrangePi |
|-------------|--------------|
| GND         | GND          |
| VCC         | 3.3V         |
| SDA         | SDA          |
| SCL         | SCL          |

---

## Пример работы с GPIO

```python
from opigallus import *

gpio_out(13)
gpio_up(13)
gpio_down(13)

gpio_rele(11)
gpio_rup(11)
gpio_rdown(11)

gpio_button(15)
gpio_pull_up(15)
gpio_pull_down(15)

if butclick(15):
    print("Нажато!")
```

---

## Пример работы с SSD1306

```python
from opigallus import *
from opigalluss.display import ssd1306
from opigalluss.draw import canvas
from PIL import ImageFont

disp = ssd1306(port=0, address=0x3C, width=128, height=64)

with canvas(disp) as draw:
    font = ImageFont.truetype("/usr/share/fonts/FreeSans.ttf", size=18)
    draw.text((0, 0), "Hello world!", font=font, fill=255)
```

---

## Вывод изображения

```python
from PIL import Image
image = Image.open('/path/to/image.png').convert("RGBA")
draw.bitmap((0, 0), image, fill=255)
```

![Пример дисплея](https://user-images.githubusercontent.com/109997469/213861709-a8f1a529-b42a-4f00-a1bc-a1e19c210605.jpg)

---

## Шрифты

Чтобы использовать свои шрифты:

```bash
sudo mkdir -p /usr/share/fonts
sudo cp ./fonts/Ваш_шрифт.ttf /usr/share/fonts/
```

---

## Обратная связь

**Telegram:** [@galluis](https://t.me/galluis)

---

> OrangePi-Py — проект для обучения и упрощения управления GPIO и дисплеями на Orange Pi.  
> Автор: GallusX  