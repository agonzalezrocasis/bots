#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Basic example for a bot that uses inline keyboards.
# This program is dedicated to the public domain under the CC0 license.

import logging
import smtplib
from email.mime.text import MIMEText

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(bot, update):
    keyboard = [[InlineKeyboardButton("Send email", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')],

                [InlineKeyboardButton("Option 3", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose one of the options shown above:', reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query

    bot.editMessageText(text="Selected option: %s" % query.data,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)

    if query.data == '1':
        print('Send email')

        msg = MIMEText(html, '<h5 style="color: gray;">Hi there! I am @LobyBot</h5>')
        msg['Subject'] = 'Greetings from @LobyBot'
        msg['From'] = 'betbatesc@gmail.com'
        msg['To'] = 'agonzalez@rocasis.mx'

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.login('betbatesc@gmail.com', '2008090274')
        s.send_message(msg)
        s.quit()
        print('Email sent')



def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")


def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))


# Create the Updater and pass it your bot's token.
updater = Updater("294405374:AAFh8tWTIMn-i4D0WknWZ5pSTvW7qssLJNI")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_error_handler(error)

# Start the Bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()
