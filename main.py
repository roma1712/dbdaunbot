import telebot
import constants

bot = telebot.TeleBot("1424440257:AAGsf3PxldRiAvLizaw362pKSQ8b8UJAW7k")
@bot.message_handler(content_types=['text','audio','video','voice','photo','sticker'])
def get(message):
	if message.text.lower() == "db0605":
		bot.send_message(message.from_user.id, "Босс все в норме , вам кофе чай или водку?")
		if message.text.lower() == "водку":
			bot.send_message(message.from_user.id, "Отлично")
		else:
			bot.send_message(message.from_user.id, "Паршиво")
	else:
		bot.send_message(message.from_user.id, "Вы не босс!")
def send_welcome(message):
	if message.text.lower() == "я серый":
		bot.send_message(message.from_user.id, "Мой господин!")
	elif message.text.lower() == "я рома":
		bot.send_message(message.from_user.id, "Мой господин!")
	elif message.text.lower() == "я дб":
		bot.send_message(message.from_user.id, "Пошел нахуй выродок!")
	elif message.text.lower() == "/admin":
		bot.send_message(message.from_user.id, "Введите пароль")
		bot.register_next_stand_handler(message.from_user.id, get(/admin))
	else:
		bot.send_message(message.chat.id,constants.random_message())
	if 'лох' in message.text.lower():
		bot.send_message(message.from_user.id, "Лошара твоя мамка!")

bot.polling(none_stop = True)
