'''
@description: download music from netease
@param: {int} id
@return: {str} url
'''
import requests

def downloadMusic(id):
    url = 'https://netease.herokuapp.com/song/url?id={}&realIP=116.25.146.177'.format(id)
    res = requests.get(url).json()
    # for debug only!
    # print (res['data'][0]['url'])
    return res['data'][0]['url']


# for debug only!
'''
if __name__ == '__main__':
    downloadMusic(1867217766)
'''