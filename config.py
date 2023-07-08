import re
import time

import requests

TOKEN = ''
MAX_DOWNLOAD = 2
BACKEND_URL = 'https://netease.api.manho30.me/'

# full format for url: http or https://xxxx.xxx/, must end with /
regex = re.compile(r'^https?://.*\/$')

if not regex.match(BACKEND_URL) or requests.get(BACKEND_URL).status_code != 200:
    print("Invalid Back-End url, Bot quited...")
    time.sleep(2)
    exit(1)

if not TOKEN:
    print('Please set your token in config.py')
    time.sleep(2)
    exit(1)
