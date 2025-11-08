import telebot

bot = telebot.TeleBot('7273657237:AAGeVKsoo22igzDSUj_xE3Ulo8UKbQB6yFA')

@bot.message_handler(commands=['привет'])
def main(message):
    bot.send_message(message.chat.id, f'привет,Даша, а ты знала что сеня тебя очень любит? только тссс')

bot.polling(none_stop=True)