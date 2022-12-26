import io

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import requests
TOKEN = "5838353732:AAHbtP3oLFbzC89HOi2Ky18S9kSC8dUFE14"

bot = telebot.TeleBot(token=TOKEN, parse_mode=None)

@bot.message_handler(commands=["start"])
def welcome_message(message):
    welcome_message = "привет, этот бот достает котов из интеренета!"

    bot.reply_to(message, welcome_message, reply_markup=keyboard())



@bot.message_handler(content_types=["text"])
def message_handle(message):
    if message.text == 'дай котика':
        cat = get_cat()
        bot.send_photo(message.chat.id, cat)
def keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton("дай котика")
    keyboard.add(button)
    return keyboard


def get_cat():

    zagalowki = {"content-type": 'image/jpeg'}
    reply = requests.get("https://thiscatdoesnotexist.com/", headers=zagalowki)


    image = reply.content

    image = io.BytesIO(image)
    return image
bot.infinity_polling()


