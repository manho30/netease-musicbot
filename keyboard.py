'''
@author: manho
@param {array of arrays}
@param {int} row
@return {array of arrays}
'''
def generate(array):
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