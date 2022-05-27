import telepot
from telepot.loop import MessageLoop
from searchMusic import searchMusic as search
from parseMusicList import parseMusicList as parse
from keyboard import generateInlineKeyboardMarkup as generate
from downloadMusic import downloadMusic as download
from getMusicData import getMusicData as getData
from time import sleep
import requests
import eyed3
import os


bot = telepot.Bot('5480116977:AAGE0NAiG_kBG5M6Ljn1LrXAifvu5kkS-9s')

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
            
    elif chat_type == 'group' or chat_type == 'supergroup':
        # exit the group since there is some bloody bug in telepot
        bot.leaveChat(chat_id)
        
def handleCallback(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    if 'song' in query_data:
        # send a message and reply to the callback 
        bot.sendChatAction(from_id, 'typing')
        process =bot.sendMessage(from_id, 'Your request is processing...')
        
        query_data = query_data.replace('song:', '')
        
        # check is the requested music is recorded in 'music_log.txt'
        if query_data in open('music_log.txt').read():
            log = open('music_log.txt', 'r')
            # separate the music id and file id
            for line in log:
                if query_data in line:
                    file_id = line.split(' ')[1].replace('\n', '')
                    break
            log.close()
            bot.sendChatAction(from_id, 'upload_document')
            bot.sendDocument(from_id, file_id)
            bot.editMessageText(telepot.message_identifier(process), 'Uploaded successfully✅')
        else:
            # get the music urls
            url = download(query_data)
            # download to local
            r = requests.get(url, stream=True)
        
            downloading = bot.editMessageText(telepot.message_identifier(process), 'Downloading...')
        
            musicData = getData(query_data)
            with open(musicData.split(',')[1], 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024): 
                    if chunk:
                        f.write(chunk)
                        
                                          
            music = eyed3.load(musicData.split(',')[1])
            music.tag.artist = musicData.split(',')[0]
            music.tag.save()
            
            downloaded = bot.editMessageText(telepot.message_identifier(downloading), '''Download completed...''')
            sleep(2)
            
            uploading = bot.editMessageText(telepot.message_identifier(downloaded), '''Uploading to Telegram...''')
            
            bot.sendChatAction(from_id, 'upload_voice')
            
            sentMusic = bot.sendAudio(from_id, open(musicData.split(',')[1], 'rb'))
            print(telepot.message_identifier(uploading))
            if sentMusic != None:
                bot.editMessageText(telepot.message_identifier(uploading), 'Uploaded successfully✅')
                # delete the local music
                os.remove(musicData.split(',')[1])
            
                if os.path.exists('music_log.txt'):
                    with open('music_log.txt', 'a') as f:
                        f.write(query_data + ' ' + str(sentMusic['audio']['file_id']) + '\n')
            else:
                bot.editMessageText(telepot.message_identifier(uploading), 'Upload failed!')
            

MessageLoop(bot, {
    'chat': handleText,
    'callback_query': handleCallback
}).run_forever()0