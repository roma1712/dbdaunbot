import telebot
import constants
from requests import get

bot = telebot.TeleBot("1424440257:AAGsf3PxldRiAvLizaw362pKSQ8b8UJAW7k")


@bot.message_handler(content_types=['text', 'audio', 'video', 'voice', 'photo', 'sticker'])
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
		bot.send_message(message.from_user.id,
                         "Цветок только у твоей мамаше ахахах еблан опять тебя по фактам раскидал")
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
		bot.send_message(message.from_user.id,
                         "Господи сын шлюхи,сдохшей в канаве и умертвленной твоим отчимом,соизволь написать побольше букв")
	elif 'бокс' in message.text.lower():
		bot.send_photo(message.from_user.id, get(
            "https://sun9-34.userapi.com/icEy8U9BKkM4Ud0s2SD72tbmMSIZ7-9bnSy2dA/2cdUQjpy60s.jpg").content)
	elif '/лизах' in message.text.lower():
		bot.send_photo(message.from_user.id,
                       get("https://sun9-45.userapi.com/c856124/v856124691/24cd50/bCE4R3sFEZw.jpg").content)
		bot.send_message(message.from_user.id, "Лиза Хлопкова , inst:_sergeeva76_, VK:https://vk.com/sssergeeva76")
	elif '/дб' in message.text.lower():
		bot.send_photo(message.from_user.id,
                       get("https://sun9-33.userapi.com/c857628/v857628268/188863/L3ptZ3l59bc.jpg").content)
		bot.send_message(message.from_user.id, "Дима Баранов , inst:dimooooooon8271, VK:https://vk.com/didibek")
	elif '/ярик' in message.text.lower():
		bot.send_photo(message.from_user.id,
                       get("https://sun9-57.userapi.com/c855616/v855616340/91075/bzyIHJPDtz0.jpg").content)
		bot.send_message(message.from_user.id, "Ярик Бондаренко , inst:footballercs_11, VK:https://vk.com/id404167028")
	elif '/кристинак' in message.text.lower():
		bot.send_photo(message.from_user.id, get(
            "https://sun9-40.userapi.com/iVohXW_PwM2mMNK9A8Y8fSb8TDgio-_o46b9eQ/FcbNo0Al2Dk.jpg").content)
		bot.send_message(message.from_user.id,
                         " Кристина Касаткина inst:k_baby_doll_5i4, VK:https://vk.com/id434274288")
	elif '/лейла' in message.text.lower():
		bot.send_photo(message.from_user.id, get(
            "https://sun9-66.userapi.com/4QthDe5aDLzXfgNScobMx8CBjAsSQ_Tinpe0uQ/HVKcmwslhe8.jpg").content)
		bot.send_message(message.from_user.id, "Лейла Обухова , inst:lil_lleyla, VK:https://vk.com/leylek_17")
	elif message.text.lower() == "/всетесты":		
		bot.send_message(message.chat.id, name_test)
		bot.register_next_step_handler(message, fifa)
		
	elif message.text.lower() == "/свойтест":
		bot.send_message(message.chat.id,"Напишите как будет называться ваш тест.Обязательно через / ,маленькими буквами.Например : /тестромы ,без пробела!!!")              
		bot.register_next_step_handler(message,func)
	else:
		bot.send_message(message.chat.id,constants.random_message())
score = 0
qwer = ""
name_test = ""
quess = ""
qs1 = ""
vr1 = ""
an1 = ""
fool = ""
qs2 = "" 
vr2 = ""
an2 = ""
qs3 = "" 
vr3 = ""
an3 = ""
qs4 = "" 
vr4 = ""
an4 = ""
qs5 = "" 
vr5 = ""
an5 = ""
qs6 = "" 
vr6 = ""
an6 = ""
qs7 = "" 
vr7 = ""
an7 = ""
qs8 = "" 
vr8 = ""
an8 = ""
qs9 = "" 
vr9 = ""
an9 = ""
qs10 = "" 
vr10= ""
an10 = ""
a = ""
b = ""
c = ""
d = ""
e = ""
f = ""
h = ""
g = ""
i  = ""
j = ""
a1 = ""
b1= ""
c1 = ""
d1= ""
e1= ""
f1= ""
h1= ""
g1= ""
i1  = ""
j1 = ""


def func(message):
    global quess
    global name_test
    quess = message.text.lower()
    name_test += quess
    bot.send_message(message.chat.id, "Напишите свой первый вопрос")
    bot.register_next_step_handler(message, fun)


def fun(message):
    global qs1
    qs1 = message.text.lower()
    bot.send_message(message.chat.id, "Какие будут варианты ответа?\nОформление такое:1)Кола,2)Спрайт,3)Фанта")
    bot.register_next_step_handler(message, funs)


def funs(message):
    global vr1
    vr1 = message.text.lower()
    bot.send_message(message.chat.id, "Какой будет правильный ответ.Выбери только цифру")
    bot.register_next_step_handler(message, fuck)


def fuck(message):
    global an1
    an1 = message.text.lower()
    bot.send_message(message.chat.id, "Напишите свой второй вопрос")
    bot.register_next_step_handler(message, fue)
def fue(message):
    global qs2
    qs2 = message.text.lower()
    bot.send_message(message.chat.id, "Какие будут варианты ответа?\nОформление такое:1)Кола,2)Спрайт,3)Фанта")
    bot.register_next_step_handler(message, fad)


def fad(message):
    global vr2
    vr2 = message.text.lower()
    bot.send_message(message.chat.id, "Какой будет правильный ответ.Выбери только цифру")
    bot.register_next_step_handler(message, ful)


def ful(message):
    global an2
    an2 = message.text.lower()
    bot.send_message(message.chat.id, "Напиши третий вопрос")
    bot.register_next_step_handler(message, ac)


def ac(message):
    global qs3
    qs3 = message.text.lower()
    bot.send_message(message.chat.id, "Какие будут варианты ответа?\nОформление такое:1)Кола,2)Спрайт,3)Фанта")
    bot.register_next_step_handler(message,asc)
def asc(message):
    global vr3
    vr3 = message.text.lower()
    bot.send_message(message.chat.id, "Какой будет правильный ответ.Выбери только цифру")
    bot.register_next_step_handler(message, sos)


def sos(message):
    global an3
    an3 = message.text.lower()
    bot.send_message(message.chat.id, "Напиши четвертый вопрос")
    bot.register_next_step_handler(message, puc)


def puc(message):
    global qs4
    qs4 = message.text.lower()
    bot.send_message(message.chat.id, "Какие будут варианты ответа?\nОформление такое:1)Кола,2)Спрайт,3)Фанта")
    bot.register_next_step_handler(message, sis)


def sis(message):
    global vr4
    vr4 = message.text.lower()
    bot.send_message(message.chat.id, "Какой будет правильный ответ.Выбери только цифру")
    bot.register_next_step_handler(message,took)
def took(message):
    global an4
    an4 = message.text.lower()
    bot.send_message(message.chat.id, "Напиши пятый вопрос")
    bot.register_next_step_handler(message, sick)


def sick(message):
    global qs5
    qs5 = message.text.lower()
    bot.send_message(message.chat.id, "Какие будут варианты ответа?\nОформление такое:1)Кола,2)Спрайт,3)Фанта")
    bot.register_next_step_handler(message, fock)


def fock(message):
    global vr5
    vr5 = message.text.lower()
    bot.send_message(message.chat.id, "Какой будет правильный ответ.Выбери только цифру")
    bot.register_next_step_handler(message, acs)


def acs(message):
    global an5
    an5 = message.text.lower()
    bot.send_message(message.chat.id, "Напиши шестой вопрос")
    bot.register_next_step_handler(message,big)
def big(message):
    global qs6
    qs6 = message.text.lower()
    bot.send_message(message.chat.id, "Какие будут варианты ответа?\nОформление такое:1)Кола,2)Спрайт,3)Фанта")
    bot.register_next_step_handler(message, fas)


def fas(message):
    global vr6
    vr6 = message.text.lower()
    bot.send_message(message.chat.id, "Какой будет правильный ответ.Выбери только цифру")
    bot.register_next_step_handler(message, full)


def full(message):
    global an6
    an6 = message.text.lower()
    bot.send_message(message.chat.id, "Напиши седьмой вопрос")
    bot.register_next_step_handler(message, act)


def act(message):
    global qs7
    qs7 = message.text.lower()
    bot.send_message(message.chat.id, "Какие будут варианты ответа?\nОформление такое:1)Кола,2)Спрайт,3)Фанта")
    bot.register_next_step_handler(message,book)
def book(message):
    global qs7
    qs7 = message.text.lower()
    bot.send_message(message.chat.id, "Какой будет правильный ответ.Выбери только цифру")
    bot.register_next_step_handler(message, fav)


def fav(message):
    global vr7
    vr7 = message.text.lower()
    bot.send_message(message.chat.id, "Напиши восьмой вопрос")
    bot.register_next_step_handler(message, fulq)


def fulq(message):
    global qs8
    qs8 = message.text.lower()
    bot.send_message(message.chat.id, "Какие будут варианты ответа?\nОформление такое:1)Кола,2)Спрайт,3)Фанта")
    bot.register_next_step_handler(message, acz)


def acz(message):
    global vr8
    vr8 = message.text.lower()
    bot.send_message(message.chat.id, "Какой будет правильный ответ.Выбери только цифру")
    bot.register_next_step_handler(message,vova)
def vova(message):
    global an8
    an8 = message.text.lower()
    bot.send_message(message.chat.id, "Напиши девятый вопрос")
    bot.register_next_step_handler(message, fcva)


def fcva(message):
    global qs9
    qs9 = message.text.lower()
    bot.send_message(message.chat.id, "Какие будут варианты ответа?\nОформление такое:1)Кола,2)Спрайт,3)Фанта")
    bot.register_next_step_handler(message, fula)


def fula(message):
    global vr9
    vr9 = message.text.lower()
    bot.send_message(message.chat.id, "Какой будет правильный ответ.Выбери только цифру")
    bot.register_next_step_handler(message, acg)


def acg(message):
    global an9
    an9 = message.text.lower()
    bot.send_message(message.chat.id, "Напиши десятый вопрос")
    bot.register_next_step_handler(message,lol)
def lol(message):
    global qs10
    qs10 = message.text.lower()
    bot.send_message(message.chat.id, "Какие будут варианты ответа?\nОформление такое:1)Кола,2)Спрайт,3)Фанта")
    bot.register_next_step_handler(message, vovs)

def vovs(message):
    global vr10
    vr10 = message.text.lower()
    bot.send_message(message.chat.id, "Какой будет правильный ответ.Выбери только цифру")
    bot.register_next_step_handler(message, fig)


def fig(message):

    global an10
    global a 
    global b
    global c
    global d
    global e
    global f
    global g
    global i 
    global h 
    global j
    global a1 
    global b1 
    global c1 
    global d1 
    global e1 
    global f1 
    global g1 
    global h1 
    global i1 
    global j1
    global vovc
    global name
    global sur
    an10 = message.text.lower()
    bot.send_message(message.chat.id, "Создано!Теперь зайдите в /всетесты")
    a = sur + quess  + vovc + qs1  + name +  vr1
    b = vovc + qs2  + name + vr2
    c = vovc + qs3 + name + vr3
    d = vovc + qs4  + name + vr4
    e = vovc + qs5  + name + vr5
    f = vovc + qs6  + name + vr6
    g = vovc + qs7  + name + vr7
    h = vovc + qs8  + name + vr8
    i = vovc + qs9 + name + vr9
    j = vovc + qs10  + name + vr10

    a1 = an1
    b1 = an2
    c1 = an3
    d1 = an4
    e1= an5
    f1 = an6
    g1 = an7
    h1 = an8
    i1 = an9
    j1 = an10
def fifa(message):
    global fool
    fool = message.text.lower()
    if fool == quess:
        bot.send_message(message.chat.id, a)
        bot.register_next_step_handler(message, nom)


def nom(message):
    global score
    global qwer
    qwer = message.text.lower()
    if qwer == a1:
        score += 1
        bot.send_message(message.chat.id, b)
        bot.register_next_step_handler(message, nos)
    else:
        score += 0
        bot.send_message(message.chat.id, b)
        bot.register_next_step_handler(message, nos)
def nos(message):
    global score
    global rot 
    rot = message.text.lower()
    if rot == b1:
        score += 1
        bot.send_message(message.chat.id, d)
        bot.register_next_step_handler(message, noq)
    else:
        score += 0
        bot.send_message(message.chat.id, d)
        bot.register_next_step_handler(message, noq)
def noq(message):
    global score
    global smell
    smell = message.text.lower()
    if smell == d1:
        score += 1
        bot.send_message(message.chat.id, e)
        bot.register_next_step_handler(message, now)
    else:
        score += 0
        bot.send_message(message.chat.id, e)
        bot.register_next_step_handler(message, now)
def now(message):
    global score
    global smel
    smel = message.text.lower()
    if smel == e1:
        score += 1
        bot.send_message(message.chat.id, f)
        bot.register_next_step_handler(message, noe)
    else:
        score += 0
        bot.send_message(message.chat.id, f)
        bot.register_next_step_handler(message, noe)
def noe(message):
    global score
    global sme
  
    sme = message.text.lower()
    if sme == f1:
        score += 1
        bot.send_message(message.chat.id,g)
        bot.register_next_step_handler(message, noy)
    else:
        score += 0
        bot.send_message(message.chat.id, g)
        bot.register_next_step_handler(message, noy)
def noy(message):
    global score
    global sm
    
    sm = message.text.lower()
    if sm == g1:
        score += 1
        bot.send_message(message.chat.id, h)
        bot.register_next_step_handler(message, nog)
    else:
        score += 0
        bot.send_message(message.chat.id, h)
        bot.register_next_step_handler(message, nog)
def nog(message):
    global score
    global sma
    
    sma = message.text.lower()
    if sma == h1:
        score += 1
        bot.send_message(message.chat.id, i)
        bot.register_next_step_handler(message, nol)
    else:
        score += 0
        bot.send_message(message.chat.id, i)
        bot.register_next_step_handler(message, nol)
def nol(message):
    global score
    global smf
   
    smf = message.text.lower()
    if smf == i1:
        score += 1
        bot.send_message(message.chat.id, j)
        bot.register_next_step_handler(message, nok)
    else:
        score += 0
        bot.send_message(message.chat.id, j)
        bot.register_next_step_handler(message, nok)
def nok(message):
    global score
    global smc
    smc = message.text.lower()
    if smc == j1:
        score += 1
        bot.register_next_step_handler(message, nvb)
    else:
        score += 0
        bot.register_next_step_handler(message, nvb)

def nvb(message):
	global score
	if score == 0:
		bot.send_message(message.chat.id, "Вы набрали 0 баллов")
	if score == 1:
		bot.send_message(message.chat.id, "Вы набрали 1 баллов")
	if score == 2:
		bot.send_message(message.chat.id, "Вы набрали 2 баллов")
	if score == 3:
		bot.send_message(message.chat.id, "Вы набрали 3 баллов")
	if score == 4:
		bot.send_message(message.chat.id, "Вы набрали 4 баллов")
	if score == 5:
		bot.send_message(message.chat.id, "Вы набрали 5 баллов")
	if score == 6:
		bot.send_message(message.chat.id, "Вы набрали 6 баллов")
	if score == 7:
		bot.send_message(message.chat.id, "Вы набрали 7 баллов")
	if score == 8:
		bot.send_message(message.chat.id, "Вы набрали 8 баллов")
	if score == 9:
		bot.send_message(message.chat.id, "Вы набрали 9 баллов")
	if score == 10:
		bot.send_message(message.chat.id, "Вы набрали 10 баллов")
	
	
		
		




bot.polling(none_stop=True)
