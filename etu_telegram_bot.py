#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Create by vast-z on 2018/2/23 
# Copyright Aiesst © 2017

print("hello world")

import telegram
import time
from telegram.ext import CommandHandler
from telegram.ext import Updater

bot = telegram.Bot(token='549671536:AAFT7P_ywV06OASR5WQZMe7siZUbTUmaG9M')

print(bot.getMe())

updater = Updater(token='549671536:AAFT7P_ywV06OASR5WQZMe7siZUbTUmaG9M')
dispatcher = updater.dispatcher

def start(bot, update):
    print("start", update.message.chat_id)
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a etu bot, please talk to me!")

def kick(bot, update):
    print("kick", update.message.chat_id)
    print("kick", update.message.from_user.id)
    bot.kickChatMember(chat_id=update.message.chat_id, user_id=update.message.from_user.id)
    print("kick success")

start_handler = CommandHandler('start', start)
kick_handler = CommandHandler('kick', kick)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(kick_handler)

updater.start_polling()


while True:
    # time.sleep(3)
    # bot.sendMessage(chat_id=377355186, text="Hello, I'm a etu bot")
    # print("send success..")
    continue
