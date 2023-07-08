'''
@descrition: parse the object returned by searchMusic() into a number list 
@param: {object} musicInfo
@param: {int} start
@param: {int} end
@return: {string}
@return: {object}
'''




def parse(musicInfo, start, end):
    # print the first element of the list
    txt = 'I found the following musics for you:\n'
    
    button = []
    
    for i in range(start, end):
        
        # if i is equal to the index, then change the caractor to '└'
        if i == end - 1:
            txt += '└ *{}* *{}*\n'.format(i + 1, musicInfo['result']['songs'][i]['name'])
            txt += '     └ {}\n'.format(musicInfo['result']['songs'][i]['ar'][0]['name'])
            
            button.append({
                'text': '{}'.format(i + 1),
                'callback_data': 'song:{}'.format(musicInfo['result']['songs'][i]['id'])
            })
            
            break
        
        txt += '├ *{}* *{}*\n'.format(i + 1, musicInfo['result']['songs'][i]['name'])
        txt += '│ └ {}\n'.format(musicInfo['result']['songs'][i]['ar'][0]['name'])
        
        button.append({
            'text': '{}'.format(i + 1),
            'callback_data': 'song:{}'.format(musicInfo['result']['songs'][i]['id'])
        })
    print(button)
    print(txt)
    return txt, button