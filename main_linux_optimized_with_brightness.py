from telebot import TeleBot, types
import subprocess
import time
from datetime import datetime

# Конфигурация
BOT_TOKEN = "7950188859:AAGv3TEMPDfzc_oDXxGgSjTTmTvyd_HHSco"
bot = TeleBot(BOT_TOKEN)

# НАСТРОЙКА ЯРКОСТИ ЗДЕСЬ (меняйте это значение)
BRIGHTNESS = -15  # Для улицы: -20, для темных помещений: +20, по умолчанию: 0

def print_time(message):
    """Логирование времени с миллисекундами"""
    current_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"[{current_time}] {message}")

def capture_image():
    """Захват изображения с настройкой яркости"""
    try:
        # Базовые параметры захвата
        command = [
            'fswebcam',
            '-r', '640x480',
            '--no-banner',
            '--jpeg', '90',
            '--skip', '3',
            '--frames', '5',
            '--set', 'sharpness=100',
            '--set', 'saturation=100'
        ]
        
        # Добавляем настройку яркости
        if BRIGHTNESS != 0:
            command.extend(['--set', f'brightness={BRIGHTNESS}'])
        
        command.append('temp_capture.jpg')
        
        result = subprocess.run(command, capture_output=True, timeout=8)
        
        if result.returncode == 0:
            with open('temp_capture.jpg', 'rb') as f:
                image_data = f.read()
            subprocess.run(['rm', 'temp_capture.jpg'])
            return image_data
        else:
            print_time(f"Ошибка fswebcam: {result.stderr}")
            return None

    except subprocess.TimeoutExpired:
        print_time("Таймаут захвата изображения")
        return None
    except Exception as e:
        print_time(f"Ошибка захвата: {e}")
        return None

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Приветственное сообщение"""
    welcome_text = (
        "👋 Привет! Я бот для захвата изображений\n\n"
        "📸 Отправь /photo или нажми кнопку чтобы сделать снимок\n\n"
        f"Текущая настройка яркости: {BRIGHTNESS}%"
    )
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('📸 Сделать фото')
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)
    print_time("Пользователь запустил бота")

@bot.message_handler(commands=['photo'])
@bot.message_handler(func=lambda message: message.text == '📸 Сделать фото')
def send_photo(message):
    """Снимок с предустановленной яркостью"""
    print_time(f"Съемка с яркостью: {BRIGHTNESS}%")
    start_time = time.time()
    
    bot.send_message(message.chat.id, "📸 Делаю снимок...")
    
    image_data = capture_image()
    
    if image_data:
        try:
            bot.send_photo(message.chat.id, image_data, caption="📷 Вот ваш снимок!")
            total_time = time.time() - start_time
            print_time(f"Фото отправлено за {total_time:.2f} сек")
            
        except Exception as e:
            print_time(f"Ошибка отправки: {e}")
            bot.send_message(message.chat.id, "❌ Ошибка при отправке фото")
    else:
        print_time("Не удалось получить изображение")
        bot.send_message(message.chat.id, "❌ Ошибка доступа к камере")

@bot.message_handler(func=lambda message: True)
def handle_other_messages(message):
    """Обработчик неизвестных команд"""
    help_text = (
        "🤖 Доступные команды:\n"
        "/start - Запустить бота\n"
        "/photo - Сделать фото\n\n"
        "Или используй кнопку '📸 Сделать фото'"
    )
    bot.send_message(message.chat.id, help_text)

if __name__ == "__main__":
    print_time(f"Бот запущен с яркостью: {BRIGHTNESS}%")
    bot.infinity_polling()