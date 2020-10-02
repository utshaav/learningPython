def returnList(a):
    b = ""
    for item in a:
        if (item == a[-1]):
            b += "and " + str(item)
        else:
            b += str(item) + ", "

    print(b)


def returnGrid(a):

    for i in range(len(a[1])):
        b = ""
        for j in range(len(a)):
            b += str(a[j][i])
        print(b)


grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]


returnList(['apple', 'banana', 'tofu', 'cats'])
returnGrid(grid)
