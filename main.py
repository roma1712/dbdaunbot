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
	elif message.text.lower() == "даун":
		bot.send_message(message.from_user.id, "Ты нахуя своей сдохшей мамке говоришь про себя?")
	elif message.text.lower() == "иди нахуй":
		bot.send_message(message.from_user.id, "i fucked cum in your mother")
	elif message.text.lower() == "жопой нюхаешь цветы":
		bot.send_message(message.from_user.id, "Цветок только у твоей мамаше ахахах еблан опять тебя по фактам раскидал")
	elif message.text.lower() == "мне похуй":
		bot.send_message(message.from_user.id, "ммм батя сдох сразу похуй стало,да?")
	elif 'лох' in message.text.lower():
		bot.send_message(message.from_user.id, "Закрой свой рот пидорасня ,лох только ты")
	elif 'похуй' in message.text.lower():
		bot.send_message(message.from_user.id, "Похуй будешь говорить на похронах мамаши...")
	elif 'сам' in message.text.lower():
		bot.send_message(message.from_user.id, "сам")
	elif 'люблю' in message.text.lower():
		bot.send_message(message.from_user.id, "Я тебя тоже люблю)))))")
	elif 'лиза' in message.text.lower():
		bot.send_message(message.from_user.id, "Какая Лиза:Хлопкова,Волгапкина или Бурдейная")
	elif 'лизу' in message.text.lower():
		bot.send_message(message.from_user.id, "Какую Лизу : Хлопкову , Волгапкину или Бурдейную")
	elif 'настя' in message.text.lower():
		bot.send_message(message.from_user.id, "Чо за Настя?")
	elif 'зеленская' in message.text.lower():
		bot.send_message(message.from_user.id, "Если ты реально она , звони ")
	elif 'хлопкову' in message.text.lower():
		bot.send_message(message.from_user.id, "Я ее тоже люблю ,брат,стрела тебе")
	elif 'волгапкину' in message.text.lower():
		bot.send_message(message.from_user.id, "Сочувствую")
	elif 'бурдейную' in message.text.lower():
		bot.send_message(message.from_user.id, "АХАХАХАХАХАХА ну и уебище ты")
	elif '/start' in message.text.lower():
		bot.send_message(message.from_user.id, "ахахах уебище думало нажмешь старт все заработает?Сын шлюханки...")
	elif 'кристина' in message.text.lower():
		bot.send_message(message.from_user.id, "Если ты Касаткин ,то иди нахуй блять")
	elif 'ярослава' in message.text.lower():
		bot.send_message(message.from_user.id, "Пусть Ярослава Нечаева скинет свои сиськи в лс")
	elif 'Касаткина' in message.text.lower():
		bot.send_message(message.from_user.id, "Иди нахуй Кристина блять")
	elif 'Касаткин' in message.text.lower():
		bot.send_message(message.from_user.id, "Он мой босс!")
	elif 'Рома' in message.text.lower():
		bot.send_message(message.from_user.id, "Он мой босс!")
	elif 'привет' in message.text.lower():
		bot.send_message(message.from_user.id, "Привет своей мамке скажешь")
	else:
		bot.send_message(message.chat.id,constants.random_message())
	

	

bot.polling(none_stop = True)
