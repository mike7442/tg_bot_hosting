Telegram Bot для захвата изображений с камеры

Простой Telegram бот для захвата изображений с веб-камеры сервера с возможностью настройки яркости. Идеально подходит для мониторинга через Telegram.

Быстрый старт

Клонирование и настройка
git clone <ваш-репозиторий>
cd my_TG_bots/CamBot

Установка зависимостей
sudo apt update
sudo apt install fswebcam python3 python3-pip python3-venv

Создание виртуального окружения
cd /home/mike7442/my_TG_bots
python3 -m venv venv
source venv/bin/activate
pip install pyTelegramBotAPI

Настройка бота
Создайте бота через BotFather в Telegram
Получите токен бота

Отредактируйте main.py:
Замените токен в main.py:
BOT_TOKEN = "ваш_токен_от_BotFather" # Замените на реальный токен
BRIGHTNESS = -15 # Настройте яркость под ваши условия

Запуск бота
BOT_TOKEN = "ваш_токен"
BRIGHTNESS = -15 # -20 для улицы, +20 для темноты

Вручную:
python3 main.py

Структура проекта
my_TG_bots/
├── CamBot/
│ ├── main.py # Основной код бота
│ └── CamBot.service.txt # Конфигурация systemd службы
├── commands.html # Помощник команд для терминала
└── venv/ # Виртуальное окружение Python

Настройка автозапуска (systemd служба)

Установка службы:
sudo cp CamBot.service.txt /etc/systemd/system/CamBot.service
sudo systemctl daemon-reload
sudo systemctl enable CamBot.service
sudo systemctl start CamBot.service

Комментированный сервис-файл (CamBot.service.txt):
[Unit]
Description=Telegram Bot Service # Описание службы
After=network.target # Запускать после подключения сети

[Service]
Type=simple # Тип службы - простой процесс
User=mike7442 # Пользователь от которого запускать
Group=mike7442 # Группа пользователя
WorkingDirectory=/home/mike7442/my_TG_bots/CamBot # Рабочая директория
ExecStart=/bin/bash -c "source /home/mike7442/my_TG_bots/venv/bin/activate && exec python /home/mike7442/my_TG_bots/CamBot/main.py" # Команда запуска с активацией виртуального окружения
Restart=always # Всегда перезапускать при сбоях
RestartSec=5 # Пауза перед перезапуском (5 сек)
Environment=PYTHONUNBUFFERED=1 # Небуферизованный вывод Python

[Install]
WantedBy=multi-user.target # Запускать при загрузке системы

Управление службой

Используйте commands.html для быстрого копирования команд или следующие команды:

Запуск службы:
sudo systemctl start CamBot

Остановка службы:
sudo systemctl stop CamBot

Перезапуск службы:
sudo systemctl restart CamBot

Проверка статуса:
sudo systemctl status CamBot

Включение автозапуска:
sudo systemctl enable CamBot

Помощник команд commands.html

Я создал специальную HTML-страницу commands.html для удобства работы с сервером. Она содержит все необходимые команды для управления ботом - просто откройте файл в браузере и кликайте на команды для автоматического копирования в буфер обмена.

Как использовать:
Откройте commands.html в браузере
Кликните на нужную команду - она скопируется автоматически
Вставьте в терминал сервера (Ctrl+V или правой кнопкой)

Настройка яркости

В файле main.py вы можете настроить параметр яркости под свои условия:
BRIGHTNESS = -15 # Значения от -100 до 100

Рекомендации:
-20 - для очень ярких условий (улица)
0 - стандартная настройка
+20 - для темных помещений

Решение проблем

Если бот не запускается:
Проверьте токен бота в main.py
Убедитесь, что камера подключена: ls /dev/video*
Проверьте права доступа к камере

Если служба не работает:
sudo systemctl status CamBot
sudo journalctl -u CamBot -n 50

Проблемы с зависимостями:
Переустановка виртуального окружения
cd /home/mike7442/my_TG_bots
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install pyTelegramBotAPI

Поддержка

Если возникли проблемы:
Проверьте логи: sudo journalctl -u CamBot -f
Убедитесь, что токен бота корректен
Проверьте доступность камеры

Примечание: Не забудьте заменить токен бота на реальный перед запуском!
