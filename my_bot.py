
import telebot

bot = telebot.TeleBot('1619204043:AAH56vPdnCBvS4P-z8cENZJ0VKXk4bAkOO8')

@bot.message_handler(commands = ['start', 'help'])
def send_message(message):
    bot.reply_to(message, f'Привет, я бот')

@bot.message_handler( content_types = ['text'])
def get_text_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'ХЗ')

bot.polling(none_stop = True)

