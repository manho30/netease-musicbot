'''
@description: dowenload music thumbnail to local
@param: {int} id
'''
import requests
def downloadThumbnail(id):
    url = 'https://netease.herokuapp.com/song/detail?ids={}'.format(id)
    res = requests.get(url).json()
    # for debug only!
    # print (res['songs'][0]['al']['picUrl'])
    url = res['songs'][0]['al']['picUrl']
    r = requests.get(url, stream=True)
    with open('music.jpg', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
                f.flush()