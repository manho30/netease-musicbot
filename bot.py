import telepot
from telepot.loop import MessageLoop
from searchMusic import searchMusic as search
from parseMusicList import parseMusicList as parse
from keyboard import generateInlineKeyboardMarkup as generate
from downloadMusic import downloadMusic as download
from time import sleep
import requests
import eyed3

bot = telepot.Bot('5187758392:AAGb0ZAzUHdyjKCfxky4GxMwKT0ud5o3EqQ')

def handleText(msg):
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
        
        
def handleCallback(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    if 'song' in query_data:
        # send a message and reply to the callback 
        bot.sendChatAction(from_id, 'typing')
        process =bot.sendMessage(from_id, 'Your request is processing...')
        
        # save the music
        # bot.download_file(url, 'music.mp3')
        
        # send a message to the callback
        bot.answerCallbackQuery(query_id, text='Downloaded')
        
        query_data = query_data.replace('song:', '')
        
        # get the music url
        url = download(query_data.split(' ')[0])
        # download to local
        r = requests.get(url, stream=True)
        
        downloading = bot.editMessageText(telepot.message_identifier(process), 'Downloading...')
        
        
        with open(query_data.split(' ')[1], 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk:
                    f.write(chunk)
                    
        music = eyed3.load(query_data.split(' ')[1])
        music.tag.artist = query_data.split(' ')[2]
        music.tag.save()
        
        uploading = bot.editMessageText(telepot.message_identifier(downloading), 'Download completed! Uploading to Telegram...')
        
        sentMusic = bot.sendAudio(from_id, open(query_data.split(' ')[1], 'rb'))
        print(telepot.message_identifier(uploading))
        if sentMusic != None:
            bot.editMessageText(telepot.message_identifier(uploading), 'Upload completed!')
        else:
            bot.editMessageText(telepot.message_identifier(uploading), 'Upload failed!')
            

MessageLoop(bot, {
    'chat': handleText,
    'callback_query': handleCallback
}).run_forever()
