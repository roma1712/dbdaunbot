import telebot
import constants

password = "db0605"
bot = telebot.TeleBot("1424440257:AAGsf3PxldRiAvLizaw362pKSQ8b8UJAW7k")
@bot.message_handler(content_types=['text','audio','video','voice','photo','sticker'])
def send_welcome(message):
	if message.text.lower() == "я серый":
		bot.send_message(message.from_user.id, "Мой господин!")
	elif message.text.lower() == "я рома":
		bot.send_message(message.from_user.id, "Мой господин!")
	elif message.text.lower() == "я дб":
		bot.send_message(message.from_user.id, "Пошел нахуй выродок!")
	elif message.text.lower() == "admin":
		bot.send_message(message.from_user.id, "Введите пароль")
		if message.text.lower() == password:
			bot.send_message(message.from_user.id, "Босс,все под контролем!")
			bot.send_message(message.from_user.id, "Что выберете?Кофе,чай или водку?")
			if message.text.lower() == "водку":
				bot.send_message(message.from_user.id, "Отлично босс!")
			else:
				bot.send_message(message.from_user.id, "Паршивый выбор")
		else:
			break
	else:
		bot.send_message(message.chat.id,constants.random_message())
	if 'лох' in message.text.lower():
		bot.send_message(message.from_user.id, "Лошара твоя мамка!")
	

bot.polling(none_stop = True)
