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

    for i in range(5):
        keyboardRow = []
        for j in range(2):
            button = array[i * 2 + j]
            keyboardRow.append(button)
            count += 1
            if count >= len(array):
                break

    inlineKeyboardMarkup['inline_keyboard'].append(keyboardRow)

    return inlineKeyboardMarkup

    # for debug only!

"""
print(generateInlineKeyboardMarkup([{
    'text': '1',
    'callback_data': '1'
}, {
    'text': '2',
    'callback_data': '2'
}, {
    'text': '3',
    'callback_data': '3'
}, {
    'text': '4',
    'callback_data': '4'
}]))
"""