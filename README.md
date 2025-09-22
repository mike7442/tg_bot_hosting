# Telegram Bot для захвата изображений с камеры

Бот для захвата фото с веб-камеры через Telegram.

## Установка
```bash
sudo apt install fswebcam python3 python3-venv
cd /home/mike7442/my_TG_bots
python3 -m venv venv
source venv/bin/activate
pip install pyTelegramBotAPI
Настройка
Создайте бота в BotFather

Замените токен в main.py:

python
BOT_TOKEN = "ваш_токен"
BRIGHTNESS = -15  # -20 для улицы, +20 для темноты
Запуск
Вручную:

bash
python3 main.py
Как службу:

bash
sudo cp CamBot.service.txt /etc/systemd/system/CamBot.service
sudo systemctl daemon-reload
sudo systemctl enable --now CamBot
Управление службой
bash
sudo systemctl start CamBot    # Запуск
sudo systemctl stop CamBot     # Остановка
sudo systemctl restart CamBot  # Перезапуск
sudo systemctl status CamBot   # Статус
commands.html
Откройте в браузере для быстрого копирования команд терминала.

Решение проблем
Проверка камеры:

bash
ls /dev/video*
Просмотр логов:

bash
sudo journalctl -u CamBot -f
Переустановка:

bash
cd /home/mike7442/my_TG_bots
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install pyTelegramBotAPI
