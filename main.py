import telebot
import constants


bot = telebot.TeleBot("1424440257:AAGsf3PxldRiAvLizaw362pKSQ8b8UJAW7k")
@bot.message_handler(content_types=['text'])
def send_welcome(message):
	bot.send_message(message.chat.id,constants.random_message())
	if message.text == "Я Cерый":
		bot.send_message(message.chat.id, "Да мой господин!")
	elif message.text == "Я Рома"
		bot.send_message(message.chat.id, "Да мой господин!")
	elif message.text == "Я ДБ":
		bot.send_message(message.chat.id, "Да пошел ты нахуй")

bot.polling(none_stop = True)
