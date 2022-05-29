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
    
    res = res.json()
    # is there any music inside the search result?
    if len(res['result']['songs']) > 0:
       return res
    else:
        return False
    
    
# for debug only!
'''
if __name__ == '__main__':
    searchMusic('yihuik')
'''