import telebot
import constants


bot = telebot.TeleBot("1424440257:AAGsf3PxldRiAvLizaw362pKSQ8b8UJAW7k")
@bot.message_handler(content_types=['text'])
def send_welcome(message):
	bot.send_message(message.chat.id,constants.random_message())
	if message.text.lower() == "привет":
		bot.send_message(message.from_user.id, "И тебе привет!")
	if 'бот' in message.text.lower():
		bot.send_message(message.from_user.id, "Сам ты бот!")

bot.polling(none_stop = True)
