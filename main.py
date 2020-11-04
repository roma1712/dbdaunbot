import telebot
import constants


bot = telebot.TeleBot("1424440257:AAGsf3PxldRiAvLizaw362pKSQ8b8UJAW7k")
@bot.message_handler(content_types=['text'])
def send_welcome(message):
	bot.send_message(message.chat.id,constants.random_message())
def send_welcom(message):
	if message.text == "Я Cерый":
		bot.send_message(message.chat.id, "Да мой господин!")

bot.polling(none_stop = True)
