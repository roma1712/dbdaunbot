import telebot
import constants


bot = telebot.TeleBot("1424440257:AAGsf3PxldRiAvLizaw362pKSQ8b8UJAW7k")
@bot.message_handler(content_types=['text','audio','video','voice','photo','sticker'])

def send_welcome(message):
	if message.text.lower() == "я серый":
		bot.send_message(message.from_user.id, "Мой господин!")
	elif message.text.lower() == "я рома":
		bot.send_message(message.from_user.id, "Мой господин!")
	elif message.text.lower() == "я дб":
		bot.send_message(message.from_user.id, "Пошел нахуй выродок!")
	elif message.text.lower() == "/admin":
		bot.send_message(message.from_user.id, "Введите пароль для этого нажмите /parol")
	elif message.text.lower() == "/parol":
		bot.send_message(message.from_user.id, "Вводи")
		if message.text() == "db0605":
			bot.send_message(message.from_user.id, "Босс все в норме")
			return
		else:
			bot.send_message(message.from_user.id, "Ты не босс иди нахуй!")
	else:
		bot.send_message(message.chat.id,constants.random_message())
	if 'лох' in message.text.lower():
		bot.send_message(message.from_user.id, "Лошара твоя мамка!")

	

bot.polling(none_stop = True)
