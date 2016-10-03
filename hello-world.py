import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler

TOKEN = '294405374:AAFh8tWTIMn-i4D0WknWZ5pSTvW7qssLJNI'

mBot = telegram.Bot(token = TOKEN)
mBot_updater = Updater(mBot.token)

# Handler for /start
def start(bot = mBot, update = mBot_updater):
    print('Conversation started...')
    print(update.message.chat_id)
    bot.sendMessage(chat_id = update.message.chat_id, text = 'Hi, I am @LobyBot')

# Handler for /help
def help(bot = mBot, update = mBot_updater):
    print('Getting help...')
    bot.sendMessage(chat_id = update.message.chat_id, text = 'I don\'t have many functional tasks so far...')

start_handler = CommandHandler('start', start)
help_handler = CommandHandler('?', help)

dispatcher = mBot_updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)

mBot_updater.start_polling()

while True:
    pass

# if __name__ == '__main__':
