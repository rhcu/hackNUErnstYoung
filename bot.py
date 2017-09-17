# -*- coding: utf-8 -*-
from telegram.ext import Updater         #  python-telegram-bot package
from telegram.ext import CommandHandler
from telegram.ext import Filters, MessageHandler
import requests
def start(bot, update):
    # Sends a message 
    bot.sendMessage(chat_id=update.message.chat_id, text="Hello. Please, ask a question.")
    
def echo(bot, update):

    text = update.message.text
    url="https://pure-meadow-64064.herokuapp.com/"
    data = {
        "text":text
    }
    resp = requests.post(url, data=data)

    
    bot.sendMessage(chat_id=update.message.chat_id, text=resp.text)

updater = Updater(token='361363530:AAE2nuPcGJ9eGgxh0Dk76B2Lk8pAZnSgXOs')  # Token given by BotFather
dp = updater.dispatcher
# on different commands - answer in Telegram
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, echo))
updater.start_polling()
updater.idle()
