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
	else:
		bot.send_message(message.chat.id,constants.random_message())
	if 'лох' in message.text.lower():
		bot.send_message(message.from_user.id, "Лошара твоя мамка!")
@bot.message_handler(commands=['admin'])
def admin_command(message):
		bot.send_message(message.from_user.id, "Введите пароль")
		if message.text.lower() == "db0605":
			bot.send_message(message.from_user.id, "Босс все в норме , вам кофе чай или водку?")
		
		else:
			bot.send_message(message.from_user.id, "Вы не босс!")

bot.polling(none_stop = True)
