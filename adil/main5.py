# 7337205665:AAENC7Ta24lz6UiMCEMZSNU6WA5P3gxDmGc

import telebot
import random

API_TOKEN = '7337205665:AAENC7Ta24lz6UiMCEMZSNU6WA5P3gxDmGc'

bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML')

# обработка команды старт
@bot.message_handler(commands=['start'])
def send_welcom(message):
    bot.reply_to(message, f'Добро пожаловать! Это бот "tetris_adil13_bot" v0.1')

@bot.message_handler(commands=['help'])
def send_help(message):
    help_txt = (
        "<b>Доступные команды:</b>\n"
        "/start - Начать взаимодействие с ботом\n"
        "/rand - отправка случайной картинки\n"
        "/help - информация о доступных командах\n"
    )
    bot.reply_to(message, help_txt)


@bot.message_handler(commands=['rand'])
def rand_ing(message):
    try:
        random_index = random.randint(0,2)
        image_path = f"./img/image{random_index}.jpg"
        with open(image_path, 'rb') as image_file:
            bot.send_photo(message.chat.id, image_file)
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка {e}")


# обработка остальных сообщений
@bot.message_handler()
def handle_unknown_command(message):
    bot.reply_to(message, "<b>Научись писать!!!</b>")


bot.polling()