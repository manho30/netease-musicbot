import math
import os
from queue import Queue
import time
import threading

import eyed3
import requests
import telepot
from telepot.exception import TelegramError
from telepot.loop import MessageLoop
from tqdm import tqdm

from config import TOKEN, MAX_DOWNLOAD
import download
import keyboard
import music
import parse

bot = telepot.Bot(TOKEN)

# Queue for holding song requests
song_queue = Queue()
max_downloads = MAX_DOWNLOAD
current_downloads = 0
download_lock = threading.Lock()

def handle_text(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if chat_type == 'private':
        if msg['text'] == '/start':
            bot.sendMessage(chat_id, 'Hi! I am a bot that can send you musics from Netease Cloud Music. ' +
                            'Simply send me a musics name and I will send you the musics.')
        else:
            handle_private_message(msg)
    elif chat_type in ('group', 'supergroup'):
        bot.leaveChat(chat_id)


def handle_private_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    bot.sendChatAction(chat_id, 'typing')
    searching = bot.sendMessage(chat_id, 'Searching musics for ' + msg['text'])
    try:
        res = music.search(msg['text'])
        result, button = parse.parse(res, 0, 10)
        bot.editMessageText(telepot.message_identifier(searching), result, parse_mode='Markdown',
                            reply_markup=keyboard.generate(button))
    except Exception as e:
        bot.editMessageText(telepot.message_identifier(searching), 'No result found!')


def handle_callback(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    if 'song' in query_data:
        bot.sendChatAction(from_id, 'typing')
        global process
        process = bot.sendMessage(from_id, 'Your request is processing...')
        query_data = query_data.replace('song:', '')
        if query_data in open('music_log.txt').read():
            send_music_from_server(query_data, process, from_id)
        else:
            add_song_to_queue(query_data, process, from_id)


def add_song_to_queue(query_data, process, from_id):
    song_queue.put((query_data, process, from_id))
    queue_length = song_queue.qsize()
    if queue_length > max_downloads:
        process = bot.editMessageText(telepot.message_identifier(process),
                            f'Your request is in the queue. Please wait patiently.')

def send_music_from_server(query_data, process, from_id):
    with open('music_log.txt', 'r') as log:
        for line in log:
            if query_data in line:
                file_id = line.split(' ')[1].rstrip('\n')
                break
    bot.sendChatAction(from_id, 'upload_document')
    bot.sendDocument(from_id, file_id)
    bot.deleteMessage(telepot.message_identifier(process))


def download_and_send_music(query_data, process, from_id):
    music_url = download.music(query_data)
    downloading = bot.editMessageText(telepot.message_identifier(process), 'Downloading...')
    music_data = music.data(query_data).split(',')
    with open(f"musics/{music_data[1]}.mp3", 'wb') as f:  # Open the file in binary mode
        response = requests.get(music_url, stream=True)
        total_size = int(response.headers.get('Content-Length', 0))
        block_size = 1024 * 1024 * 3 # 3MB
        start_time = time.time()
        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024, ncols=80)
        downloaded_size = 0
        download_speed = 0
        for data in response.iter_content(block_size):
            f.write(data)
            progress_bar.update(len(data))
            downloaded_size += len(data)
            elapsed_time = time.time() - start_time
            if elapsed_time > 0:
                download_speed = downloaded_size / elapsed_time
            try:
                percentage = int(downloaded_size / total_size * 100)
                def generate_bar(value):
                    bar_length = 10
                    num_blocks = int(value / (100 / bar_length))
                    return '█' * num_blocks + 'ㅤ' * (bar_length - num_blocks)
                downloading = bot.editMessageText(
                    telepot.message_identifier(downloading),
                    text =f"Downloading... {percentage}%\n"
                    f"|{generate_bar(percentage)}| {download_speed / 1024:.2f} KB/s\n"
                    f"Estimated time: {math.ceil((total_size - downloaded_size) / download_speed)}s"
                )
            except TelegramError:
                pass
        progress_bar.close()
    with open(f"./thumbnail/{query_data}.jpg", 'wb') as f:  # Open the file in binary mode
        f.write(requests.get(music_data[3]).content)
    try:
        audiofile = eyed3.load(f"musics/{music_data[1]}.mp3")
        if audiofile is not None:
            audiofile.tag = audiofile.tag or eyed3.id3.Tag()
            audiofile.tag.artist = music_data[0]
            audiofile.tag.title = music_data[1]
            audiofile.tag.images.set(3, open(f"thumbnail/{query_data}.jpg", "rb").read(), "image/jpeg")
            audiofile.tag.save()
            duration = math.ceil(audiofile.info.time_secs) - 1
        else:
            raise Exception('Failed to load audio file')
    except Exception as e:
        os.system(
            f'ffmpeg -i "musics/{music_data[1]}.mp3" -i "thumbnail/{query_data}.jpg" -map 0:0 -map 1:0 -c '
            f'copy -id3v2_version 3 -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" "musics/'
            f'{music_data[1]}.mp3" '
        )
    downloaded = bot.editMessageText(telepot.message_identifier(downloading), 'Download completed...')
    uploading = bot.editMessageText(telepot.message_identifier(downloaded), f'Uploading to Telegram...\nSize: {os.path.getsize(f"./musics/{music_data[1]}.mp3") / 1000000:.2f} MB')
    if duration < 32:
        copyright_note = "\n\n🚫 This song requires VIP which limit by Netease Music. I can't download the full song."
    else:
        copyright_note = ''
    try:
        sent_music = bot.sendAudio(from_id, open(f"./musics/{music_data[1]}.mp3", 'rb'),
                                   title=music_data[1],
                                   performer=music_data[0],
                                   caption=f'🎵 {music_data[1]} - {music_data[0]}'
                                           f'\n📀 {music_data[2]}'
                                           f'\n📈 Size: {os.path.getsize(f"./musics/{music_data[1]}.mp3") / 1000000:.2f} MB'
                                           f'{copyright_note}'
                                           f'\n\n📻 @netease_musicbot',
                                   duration=duration
                                   )
    except Exception as e:
        sent_music = None
        bot.editMessageText(telepot.message_identifier(uploading), 'Upload failed!')
    if sent_music is not None:
        bot.deleteMessage(telepot.message_identifier(uploading))
        if os.path.exists('music_log.txt'):
            with open('music_log.txt', 'a') as f:
                f.write(query_data + ' ' + str(sent_music['audio']['file_id']) + '\n')
    else:
        bot.editMessageText(telepot.message_identifier(uploading), 'Upload failed!')
def process_queue():
    global current_downloads
    while True:
        if current_downloads < max_downloads and not song_queue.empty():
            with download_lock:
                current_downloads += 1
            query_data, process, from_id = song_queue.get()
            try:
                download_and_send_music(query_data, process, from_id)
            except Exception as e:
                pass
            finally:
                with download_lock:
                    current_downloads -= 1
        else:
            time.sleep(0.1)
def bot_thread():
    print('Listening ...')
    MessageLoop(bot, {'chat': handle_text,
                      'callback_query': handle_callback}).run_as_thread()
    while True:
        time.sleep(0.1)



# Start the threads
threading.Thread(target=bot_thread).start()
threading.Thread(target=process_queue).start()
