import selenium.webdriver
from selenium.webdriver.common.by import By
import telebot
from telebot import types
bot = telebot.TeleBot('-_-')
lst = []
driver = selenium.webdriver.Chrome() # Firefox()

driver.get('https://rasp.rea.ru/?q=15.27д-мо02%2F23б#today')
driver.maximize_window()

all_cards = driver.find_elements(By.XPATH, '//*[@id="zoneTimetable"]/div')
str1 = ""
my_file = open("rasp.txt", "w+")
for row in all_cards:
    # my_file.write(row.text)
    str1+=row.text
# str1 = str1.replace("\n", " ")
rasp = str1
rasp = rasp.replace("\n", " ")
rasp = rasp.split()
pn = []
vt = []
sr = []
ch = []
pt = []
sub = []
last = 0
rasp1 = []
cf = ['1','2','3','4','5','6']
for i in range (len(rasp)):
    if rasp[i] == 'пара' and rasp[i+2] == 'пара':
        rasp1.append(rasp[i])
        rasp1.append('-')
    else:
        rasp1.append(rasp[i])
print(rasp1)

for i in range (len(rasp1)):
    if (rasp1[i] != 'ВТОРНИК,'):
        pn.append(rasp1[i])
        last = i +1
    else:
        break
for i in range (last, len(rasp1)):
    if (rasp1[i] != 'СРЕДА,'):
        vt.append(rasp1[i])
        last = i + 1
    else:
        break
for i in range (last, len(rasp1)):
    if (rasp1[i] != 'ЧЕТВЕРГ,'):
        sr.append(rasp1[i])
        last = i + 1
    else:
        break
for i in range (last, len(rasp1)):
    if (rasp1[i] != 'ПЯТНИЦА,'):
        ch.append(rasp1[i])
        last = i + 1
    else:
        break
for i in range (last, len(rasp1)):
    if (rasp1[i] != 'СУББОТА,'):
        pt.append(rasp1[i])
        last = i + 1
    else:
        break
for i in range (last, len(rasp1)):
        sub.append(rasp1[i])
        last = i + 1
# for i in range(last,len(rasp)):
#     while(rasp[i] != 'СРЕДА,'):
#         vt.append(rasp[i])
#         last = i

print(pn)
print(vt)
print(sr)
print(ch)
print(pt)
print(sub)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.from_user.id, "👋 Привет! Используй команды  \n /start /button", reply_markup=markup)

@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("расписание на неделю")
    markup.add(item1)
    item2=types.KeyboardButton("расписание на понедельник")
    markup.add(item2)
    item3=types.KeyboardButton("расписание на вторник")
    markup.add(item3)
    item4=types.KeyboardButton("расписание на среду")
    markup.add(item4)
    item5=types.KeyboardButton("расписание на четверг")
    markup.add(item5)
    item5=types.KeyboardButton("расписание на пятницу")
    markup.add(item5)
    item6=types.KeyboardButton("расписание на субботу")
    markup.add(item6)
    bot.send_message(message.chat.id,'Нажмите нужную вам кнопку',reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="расписание на неделю":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,str1 ,reply_markup=markup)
    elif message.text=="расписание на понедельник":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,"\n".join([str(x) for x in pn]) ,reply_markup=markup)
    elif message.text=="расписание на вторник":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,"\n".join([str(x) for x in vt]) ,reply_markup=markup)
    elif message.text=="расписание на среду":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,"\n".join([str(x) for x in sr]) ,reply_markup=markup)
    elif message.text=="расписание на четверг":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,"\n".join([str(x) for x in ch]) ,reply_markup=markup)
    elif message.text=="расписание на пятницу":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,"\n".join([str(x) for x in pt]) ,reply_markup=markup)
    elif message.text=="расписание на субботу":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,"\n".join([str(x) for x in sub]) ,reply_markup=markup)


# @bot.message_handler(commands=['расписание'])
# def rasp(message):
#     # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     # btn1 = types.KeyboardButton("расписание")
#     # markup.add(btn1)
#     if message.text == "👋 Поздороваться":
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton('расписание на неделю')
#         btn2 = types.KeyboardButton('расписание на понедельник')
#         btn3 = types.KeyboardButton('расписание на вторник')
#         btn4 = types.KeyboardButton('расписание на среду')
#         btn5 = types.KeyboardButton('расписание на четверг')
#         btn6 = types.KeyboardButton('расписание на пятницу')
#         btn7 = types.KeyboardButton('расписание на субботу')
#         markup.add(btn1,btn2, btn3,btn4,btn5,btn6,btn7)
#         bot.send_message(message.from_user.id, 'выберите интересующую категорию')
#     elif message.text == 'расписание на неделю':
#         bot.send_message(message.from_user.id, str1)
#         # bot.send_message(message.from_user.id, str1, parse_mode='Markdown')

@bot.message_handler(commands=['понедельник'])
def pon(message):
        bot.send_message(message.from_user.id, "\n".join([str(x) for x in pn]))

@bot.message_handler(commands=['вторник'])
def vtr(message):
    bot.send_message(message.from_user.id, "\n".join([str(x) for x in vt]))
@bot.message_handler(commands=['среда'])
def sred(message):
    bot.send_message(message.from_user.id, "\n".join([str(x) for x in sr]))
@bot.message_handler(commands=['четверг'])
def chet(message):
    bot.send_message(message.from_user.id, "\n".join([str(x) for x in ch]))
@bot.message_handler(commands=['пятница'])
def pyat(message):
    bot.send_message(message.from_user.id, "\n".join([str(x) for x in pt]))
@bot.message_handler(commands=['суббота'])
def subb(message):
    bot.send_message(message.from_user.id, "\n".join([str(x) for x in sub]))
bot.polling(none_stop=True, interval=0)
