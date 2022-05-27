'''
@author: manho
@param {array of arrays}
@param {int} row
@return {array of arrays}
'''


def generateInlineKeyboardMarkup(array):
    inlineKeyboardMarkup = {
        'inline_keyboard': []
    }
    count = 0
    for i in range(2):
        keyboardRow = []
        for j in range(5):
            button = array[i * 5 + j]
            keyboardRow.append(button)
            count += 1
            if count >= len(array):
                break
        inlineKeyboardMarkup['inline_keyboard'].append(keyboardRow)
    print(inlineKeyboardMarkup)
    return inlineKeyboardMarkup

'''
for debug only!
print(generateInlineKeyboardMarkup([{'text': '1', 'callback_data': '1867217766'}, {'text': '2', 'callback_data': '1848190450'}, {'text': '3', 'callback_data': '1939215517'}, {'text': '4', 'callback_data': '1860614598'}, {'text': '5', 'callback_data': '1930790961'}, {'text': '6', 'callback_data': '1874972712'}, {'text': '7', 'callback_data': '1889702364'}, {'text': '8', 'callback_data': '1878315329'}, {'text': '9', 'callback_data': '1885427474'}, {'text': '10', 'callback_data': '1846094285'}, {'text': '11', 'callback_data': '1863090822'}, {'text': '12', 'callback_data': '1885179171'}, {'text': '13', 'callback_data': '1941664399'}, {'text': '14', 'callback_data': '1906045793'}, {'text': '15', 'callback_data': '1896469403'}, {'text': '16', 'callback_data': '1898189387'}, {'text': '17', 'callback_data': '1828747550'}, {'text': '18', 'callback_data': '1470130616'}, {'text': '19', 'callback_data': '1844562141'}, {'text': '20', 'callback_data': '1886384894'}, {'text': '21', 'callback_data': '1868872629'}, {'text': '22', 'callback_data': '1881719700'}, {'text': '23', 'callback_data': '1832643077'}, {'text': '24', 'callback_data': '1906045789'}, {'text': '25', 'callback_data': '1844566133'}, {'text': '26', 'callback_data': '1834675802'}, {'text': '27', 'callback_data': '1945241420'}, {'text': '28', 'callback_data': '1844584034'}, {'text': '29', 'callback_data': '1934914514'}, {'text': '30', 'callback_data': '1854473737'}]))
'''