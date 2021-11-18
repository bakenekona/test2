import telebot

TOKEN = "2020234609:AAHIpPURs54SfQd3OCr8JF5J89ilnZYc4JQ"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду парсить заголовки с Хабра')
bot.polling()