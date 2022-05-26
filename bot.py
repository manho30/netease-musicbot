from tkinter import Button
import telepot
from telepot.loop import MessageLoop
from searchMusic import searchMusic as search
from parseMusicList import parseMusicList as parse
from keyboard import generateInlineKeyboardMarkup as generate
bot = telepot.Bot('5187758392:AAGb0ZAzUHdyjKCfxky4GxMwKT0ud5o3EqQ')



def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    
    if chat_type == 'private':
        if msg['text'] == '/start':
            bot.sendChatAction(chat_id, 'typing')
            bot.sendMessage(chat_id, 'Hi! I am a bot can send you music from Netease Cloud Music. ' +
                                      'Simply send me a music name and I will send you the music.')
                                      
        else:
            # the rest of message will be searching for the music handle by searchMusic.py
            bot.sendChatAction(chat_id, 'typing')
            searching = bot.sendMessage(chat_id, 'Searching music for ' + msg['text'])
            
            result, button = parse(search(msg['text']), 0, 10)
            
            bot.editMessageText(telepot.message_identifier(searching), result, parse_mode='Markdown', reply_markup=generate(button))
            
MessageLoop(bot, handle).run_forever()
