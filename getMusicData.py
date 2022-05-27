import requests
def getMusicData(id):
    url = 'https://netease.herokuapp.com/search?keywords={}'.format(id)
    res = requests.get(url)
    res = res.json()
    return res['result']['songs'][0]['artists'][0]['name'] + ',' + res['result']['songs'][0]['name']
    
if __name__ == '__main__':
    print(getMusicData(1867217766))
    