from typing import re

from django.core.management.base import BaseCommand
import os
import telebot
from telebot import types

from bot.models.Profile import Profile
from bot.models.Message import Message


bot =


@bot.message_handler(commands=['admin'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на админку", url="https://ya.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Для перехода в админ-панель нажми на кнопку ниже", reply_markup=keyboard)


@bot.message_handler(commands=['register'])
def do_register(message):
    chat_id = message.chat.id
    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': message.from_user.username,
        }
    )
    bot.send_message(chat_id, 'Вы зарегистрированы с системе')


@bot.message_handler(commands=['count'])
def do_count(message):
    chat_id = message.chat.id
    profile = Profile.objects.get(external_id=chat_id)
    count = Message.objects.filter(profile=profile).count()
    bot.send_message(chat_id, f'У вас {count} сообщений')


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


class Command(BaseCommand):
    help = 'Телеграм-бот',

    def handle(self, *args, **options):
        bot.infinity_polling()
