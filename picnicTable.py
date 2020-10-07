def printPicnic(itemsDict, leftWidth, rightWidth):
    print("PICNIC ITEM".center(leftWidth + rightWidth, '-'))

    for k, v in itemsDict.items():
        print(k.ljust(leftWidth) + str(v).rjust(rightWidth))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def PrintTable(tableData):
    max = 0
    for list in tableData:
        for content in list:
            if max < len(content):
                max = len(content)

    text = ""
    for i in range(len(tableData[1])):
        for j in range(len(tableData)):
            text += tableData[j][i].rjust(max)
        text += '\n'
    print(text)


PrintTable(tableData)
