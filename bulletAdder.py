#! python
# Program that adds bullets to the list

import pyperclip

text = pyperclip.paste()
listOfText = text.split("\n")

for i in range(len(listOfText)-1):
    listOfText[i] = '*' + listOfText[i]
    print('* ' + listOfText[i])
text = '\n'.join(listOfText)
pyperclip.copy(text)
