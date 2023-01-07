# OrangePi3-GpioPy
ДЛЯ ИСПОЛЬЗОВАНИЯ БИБЛИОТЕКИ НЕОБХОДИМО УСТАНОВИТЬ WiringOP
git clone https://github.com/zhaolei/WiringOP.git -b h3
#cd WiringOP
#chmod +x ./build
#sudo ./build
#после установки проверяем работоспособность
#gpio readall
#покажет все порты, назначения и состояния
И устанавливаем библиотеку 
pip install opigpiogalluss
Не большая библиотека для обучения
И для простого программирования GPIO выходов на OrangePi 3 lts на языке Python 
gpout(НОМЕР ПИНА)-Ввыбираем пин для вывода 
gpout(НОМЕР ПИНА)-подаем сигнал
gpout(НОМЕР ПИНА)-отключаем сигнал
