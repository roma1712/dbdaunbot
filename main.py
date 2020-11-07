import telebot
import constants
from requests import get

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
	elif message.text.lower() == "мать":
		bot.send_message(message.from_user.id, "твоя сдохла")
	elif message.text.lower() == "мать сдохла":
		bot.send_message(message.from_user.id, "твоя")
	elif 'лох' in message.text.lower():
		bot.send_message(message.from_user.id, "Закрой свой рот пидорасня ,лох только ты")
	elif 'похуй' in message.text.lower():
		bot.send_message(message.from_user.id, "Похуй будешь говорить на похронах мамаши...")
	elif 'сам' in message.text.lower():
		bot.send_message(message.from_user.id, "сам")
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
	elif 'ярослава' in message.text.lower():
		bot.send_message(message.from_user.id, "Пусть Ярослава Нечаева скинет свои сиськи в лс")
	elif message.text.lower() == "Касаткина":
		bot.send_message(message.from_user.id, "Иди нахуй Кристина блять")
	elif message.text.lower() == "я ярик":
		bot.send_message(message.from_user.id, "Мой господин!")
	elif message.text.lower() == "я лиза хлопкова":
		bot.send_message(message.from_user.id, "Моя королева!")
	elif len(message.text.lower()) == 1:
		bot.send_message(message.from_user.id, "Господи сын шлюхи,сдохшей в канаве и умертвленной твоим отчимом,соизволь написать побольше букв")
	elif 'бокс' in message.text.lower():
		bot.send_photo(message.from_user.id,get("https://sun9-34.userapi.com/icEy8U9BKkM4Ud0s2SD72tbmMSIZ7-9bnSy2dA/2cdUQjpy60s.jpg").content)
	elif '/лизах' in message.text.lower():
		bot.send_photo(message.from_user.id,get("https://sun9-45.userapi.com/c856124/v856124691/24cd50/bCE4R3sFEZw.jpg").content)
		bot.send_message(message.from_user.id,"Лиза Хлопкова , inst:_sergeeva76_, VK:https://vk.com/sssergeeva76")
	elif '/дб' in message.text.lower():
		bot.send_photo(message.from_user.id,get("https://sun9-33.userapi.com/c857628/v857628268/188863/L3ptZ3l59bc.jpg").content)
		bot.send_message(message.from_user.id,"Дима Баранов , inst:dimooooooon8271, VK:https://vk.com/didibek")
	elif '/ярик' in message.text.lower():
		bot.send_photo(message.from_user.id,get("https://sun9-57.userapi.com/c855616/v855616340/91075/bzyIHJPDtz0.jpg").content)
		bot.send_message(message.from_user.id,"Ярик Бондаренко , inst:footballercs_11, VK:https://vk.com/id404167028")
	elif '/кристинак' in message.text.lower():
		bot.send_photo(message.from_user.id,get("https://sun9-40.userapi.com/iVohXW_PwM2mMNK9A8Y8fSb8TDgio-_o46b9eQ/FcbNo0Al2Dk.jpg").content)
		bot.send_message(message.from_user.id," ,Кристина Касаткина inst:k_baby_doll_5i4, VK:https://vk.com/id434274288")
	elif '/лейла' in message.text.lower():
		bot.send_photo(message.from_user.id,get("https://sun9-66.userapi.com/4QthDe5aDLzXfgNScobMx8CBjAsSQ_Tinpe0uQ/HVKcmwslhe8.jpg").content)
		bot.send_message(message.from_user.id,"Лейла Обухова , inst:lil_lleyla, VK:https://vk.com/leylek_17")

	

	else:
		bot.send_message(message.chat.id,constants.random_message())
achieve = ""
score = 0
guess1 = ""
guess2 = ""
guess3 = ""
guess4 = ""
guess5 = ""
def ques1(message):
	if message.text.lower() == "/тестромакасаткин":
			bot.send_message(message.chat.id,"Вопроc 1:Какой любимый день недели?")
			bot.register_next_step_handler(message,ques2)
def ques2(message):
	global score
	guess1 = message.text.lower()
	if guess1 == "суббота":
		score += 1
		bot.send_message(message.chat.id, "Вопроc 2:Что любит больше(ночь,день или утро)")
		bot.register_next_step_handler(message, ques3)
	else:
		bot.send_message(message.chat.id, "Вопроc 2:Что любит больше(ночь,день или утро)")
		bot.register_next_step_handler(message, ques3)
def ques3(message):
	global score
	quess2 = message.text.lower()
	if quess2 == "ночь":
		score += 1
		bot.send_message(message.chat.id, "Вопроc 3:Что любит больше:чай или кофе")
		bot.register_next_step_handler(message, ques4)
	else:
		bot.send_message(message.chat.id, "Вопроc 3:Что любит больше:чай или кофе")
		bot.register_next_step_handler(message, ques4)

def ques4(message):
	global score
	quess3 = message.text.lower()
	if quess3 == "кофе":
		score += 1
		bot.send_message(message.chat.id, "Вопроc 4:Деньги или любовь")
		bot.register_next_step_handler(message, ques5)
	else:
			bot.send_message(message.chat.id, "Вопроc 4:Деньги или любовь")
			bot.register_next_step_handler(message, ques5)
def ques5(message):
	global score
	quess4 = message.text.lower()
	if quess4 == "деньги":
		score += 1
		bot.send_message(message.chat.id, "Вопрос 5: Любимый цвет")
		bot.register_next_step_handler(message, ques6)
	else:
		bot.send_message(message.chat.id, "Вопрос 5: Любимый цвет")
		bot.register_next_step_handler(message, ques6)
def ques6(message):
	global score
	global achieve
	quess5 = message.text.lower()
	if quess5 == "черный":
		score += 1
		bot.send_message(message.chat.id, "Вы набрали" ,str(score),"очков!")
		achieve = "Тест Ромы пройден на",score,"очков"
	else:
		bot.send_message(message.chat.id, "Вы набрали" ,str(score),"очков!")
		achieve = "Тест Ромы пройден на", score, "очков"
def welc(message):
	if message.text.lower() == "/achieve":
		bot.send_message(message.chat.id, achieve)

	

bot.polling(none_stop = True)
