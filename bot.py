import telebot
from telebot.types import Message

TOKEN = '624978899:AAHo3bgD0eSC0v8dXXArn_J20FLyxxd34vU'
STICKER = 'CAADAgADKQEAAnmyPgQ-rNllRYk49QI'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def command_handler(message: Message):
    bot.reply_to(message, 'I alive!!!')

@bot.message_handler(commands=['help'])
def command_handler(message: Message):
    bot.reply_to(message, 'can i halp you?')

@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_gigits(message: Message):
    if 'tratata' in message.text:
        bot.reply_to(message, 'taratata')
        return
    bot.reply_to(message, 'tratata')

@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_sticker(message.chat.id, STICKER)

bot.polling(timeout=60)
