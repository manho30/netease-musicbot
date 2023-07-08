import requests

from config import BACKEND_URL

def data(id):
    url = f'{BACKEND_URL}song/detail?ids={id}'
    res = requests.get(url)
    res = res.json()
    return res['songs'][0]['ar'][0]['name'] + ',' + res['songs'][0]['name'] + ',' + res['songs'][0]['al']['name'] + ',' + res['songs'][0]['al']['picUrl']


'''
function for search musics
@param: {str} name
@return: {object} musicInfo
'''
def search(name):
    url = f'{BACKEND_URL}cloudsearch?keywords={name}'
    res = requests.get(url)

    res = res.json()
    # print(res)
    # is there any musics inside the search result?
    if len(res['result']['songs']) > 0:
        return res
    else:
        return False

