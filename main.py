import telebot
from settings import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)

bot.polling(none_stop=True, interval=0)
