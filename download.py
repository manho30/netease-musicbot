import requests

from config import BACKEND_URL
'''
@description: download musics from netease
@param: {int} id
@return: {str} url
'''
def music(id):
    url = f'{BACKEND_URL}song/url/v1?id={id}&level=jymaster'
    res = requests.get(url).json()
    # for debug only!
    # print (res['data'][0]['url'])
    return res['data'][0]['url']

'''
@description: dowenload musics thumbnail to local
@param: {int} id
'''
def thumbnail(id):
    url = f'{BACKEND_URL}song/detail?ids={id}'
    res = requests.get(url).json()
    url = res['songs'][0]['al']['picUrl']
    r = requests.get(url, stream=True)
    with open('musics.jpg', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()