'''
function for search music
@param: {str} name
@return: {object} musicInfo
'''

author = 'manho'

import requests

def searchMusic(name):
    url = 'https://netease.herokuapp.com/search?keywords={}'.format(name)
    res = requests.get(url)
    # for debug only!
    # print (res.json())
    return res.json()
    
    
# for debug only!
'''
if __name__ == '__main__':
    searchMusic('yihuik')
'''