import telebot, time

#для работы с местоположением 
import geopy
from geopy.geocoders import Nominatim

#для работы с языками
#прочитать библиотеку по лучше чтобы можно было переводить на другие языки тоже 
from deep_translator import GoogleTranslator # type: ignore

#для работы и подключения к БД
import sqlite3

token = '7641093127:AAE-iZfQF2RCOkPEDTn-miEUP_eoclMbHUo'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Доброго времени суток')
    time.sleep(1)
    bot.send_message(message.chat.id, 'чем могу быть полезен')

@bot.message_handler(commands=['language'])
def choose_lang(message):
    bot.send_message(message.chat.id, 'Выберите язык: Du, En, Ru')

@bot.message_handler()
def lang(message):
    if message.text.lower() =='du':
        text = 'Немецкий язык выбран'
        translated = GoogleTranslator(source='russian', target='german').translate(text)
        bot.reply_to(message, translated)
    elif message.text.lower() == 'en':
        text = 'Английский язык выбран'
        translated = GoogleTranslator(source='russian', target='english').translate(text)
        bot.reply_to(message, translated)
    elif message.text.lower() == 'ru':
        text = 'Русский язык выбран'
        translated = GoogleTranslator(source='russian', target='russian').translate(text)
        bot.reply_to(message, translated)


bot.infinity_polling()