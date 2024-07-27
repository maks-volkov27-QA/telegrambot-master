import telebot
import config
import time
 
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)

 
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🔎 Найти лучшего QA!")
 
    markup.add(item1)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы помочь самому лучшему HR, найти самого лучшего QA. Жми на поиск🙂".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Привет':
            bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы помочь самому лучшему HR, найти самого лучшего QA.".format(message.from_user, bot.get_me()),
        parse_mode='html')
        elif message.text == '🔎 Найти лучшего QA!':
 
            markup = types.InlineKeyboardMarkup(row_width=6)
            item1 = types.InlineKeyboardButton("Сайт", url='https://qaman.ru')
            item2 = types.InlineKeyboardButton("Git", url='https://github.com/DanilaQA')
            item3 = types.InlineKeyboardButton("Telegram", url='https://t.me/VKGBDA')
            item4 = types.InlineKeyboardButton("WhatsApp", url='https://wa.me/79998221800')
            item5 = types.InlineKeyboardButton("📧", callback_data='e')
            item6 = types.InlineKeyboardButton("📱", callback_data='n')
 
            markup.add(item1, item2,item3,item4,item5,item6)
 
            bot.send_message(message.chat.id, '👨‍💻 Запускаю поиск лучших QA специалистов')
            time.sleep(1)
            bot.send_message(message.chat.id, 'Loading...█▒▒▒▒▒▒▒▒▒')
            time.sleep(0.1)
            bot.send_message(message.chat.id, 'Loading...███▒▒▒▒▒▒▒')
            time.sleep(0.9)
            bot.send_message(message.chat.id, 'Loading...█████▒▒▒▒▒')
            time.sleep(0.2)
            bot.send_message(message.chat.id, 'Loading...███████▒▒▒')
            time.sleep(0.8)
            bot.send_message(message.chat.id, 'Loading...██████████')
            time.sleep(1)
            bot.send_message(message.chat.id, 'Done ✅ / Анкета №367299823 Вам отлично подойдет!')
            time.sleep(2)
            bot.send_photo(message.chat.id, 'https://avatars.githubusercontent.com/u/94226069?v=4')
            bot.send_message(message.chat.id, 'Бурлаченко Данила Алексеевич. Умен, красив, честен. Прокачан в скилы и в юмор. Не знает синонимов к слову "унывать", вокруг себя создает позитив. Всегда рад помочь советом или действием.')
            time.sleep(5)
            bot.send_message(message.chat.id, 'Сайт визитка, социальные сети и контактные данные анкеты', reply_markup=markup)
            
        else:
            bot.send_message(message.chat.id, 'Нажми на поиск😉')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'e':
                bot.send_message(call.message.chat.id, 'mail@qaman.ru')
            elif call.data == 'n':
                bot.send_message(call.message.chat.id, '+79998221800')
           
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="👋Пиши и звони👋")
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)