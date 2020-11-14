from django.core.management.base import BaseCommand
from django.conf import settings
import os
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.utils.request import Request

from bot.models.Profile import Profile
from bot.models.Message import Message


def log_errors(f):

    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_message = f'Произошла ошибка: {e}'
            print(error_message)
            raise e

    return inner


@log_errors
def do_echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text

    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username
        }
    )
    m = Message(
        profile=p,
        text=text
    )
    m.save()

    reply_text = f'Ваш ID = {chat_id} \n Message ID:{m.pk} \n {text}'
    update.message.reply_text(
        text=reply_text
    )


@log_errors
def do_count(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    count = Message.objects.filter(profile=p).count()

    # count = 0
    update.message.reply_text(
        text=f'У вас {count} сообщений',
    )

@log_errors
def do_secret(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )

    update.message.reply_text(
        text=f'Потерпи сколо заработает',
    )


@log_errors
def do_users(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    p, _ = Profile.objects.get_or_create(
        external_id=chat_id,
        defaults={
            'name': update.message.from_user.username,
        }
    )
    users = list(Profile.objects.values('name'))
    update.message.reply_text(
        text=f'{users}'
    )


class Command(BaseCommand):
    help = 'Телеграм-бот',

    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0
        )
        bot = Bot(
            request=request,
            token=os.getenv('bot_token'),
            base_url=os.getenv('bot_proxy')
        )
        print(bot.get_me())

        updater = Updater(
            bot=bot,
            use_context=True
        )

        updater.dispatcher.add_handler(CommandHandler('count', do_count))
        updater.dispatcher.add_handler(CommandHandler('secret_command', do_secret))
        updater.dispatcher.add_handler(CommandHandler('get_users', do_users))

        message_handler = MessageHandler(Filters.text, do_echo)
        updater.dispatcher.add_handler(message_handler)

        updater.start_polling()
        updater.idle()
