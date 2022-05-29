# Python Telegram Music Bot
This is a simple music bot for Telegram.
Using this bot you can listen to music from Netease Cloud Music in Telegram.


This bot will download the music into local, and edit the
song name, song artist, and song album. In the end, it will send back to the user.
## Installation
1. Clone the repository
```
$ git clone https://github.com/manho30/musicbot.py.git
$ cd musicbot.py
```
2. Install dependencies
```
$ pip install -r requirements.txt
```
3. Change the `TOKEN` variable in `config.py` to your bot's token.
``` python
TOKEN = 'insert your token here'
```
4. Run the bot
```
$ python3 bot.py
```

## Deploy to Heroku
1. Clone the repository
```
$ git clone
$ cd musicbot.py
```
2. Install dependencies
```
$ pip install -r requirements.txt
```
3. Change the `TOKEN` variable in `config.py` to your bot's token.
``` python
TOKEN = 'insert your token here'
```
4. Push the changes to Heroku
```
$ heroku login
$ heroku git:remote -a <HEROKU PROJECT NAME>
$ git push heroku master
```
5. Run the bot
```
heroku ps:scale bot=1 
```
## Dependencies
* Python 3.6+
* [requests](https://2.python-requests.org/en/master/)
* [telepot](https://telepot.readthedocs.io/en/latest/index.html)
* [eyed3`](https://eyed3.readthedocs.io/en/latest/index.html)


## Cache system
The cache is used to store the song's `file_id` when it's uploaded to Telegram so that next time while another user requests the same song, the bot can just sent with the `file_id` instead of downloading the song again.

TO BE INFO:
* The cache is not awailable for other bots.
* All the songs that requested by user will direct recprd to the cache.
* The other info will never be stored in the cache.