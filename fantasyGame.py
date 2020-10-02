def displayInventory(dict):
    total = 0
    print('Inventory:')
    for k, v in dict.items():
        print(f'{v} {k}')
        total += v
    print(f'Total items: {total}')


def addInventory(list, dict):
    for item in list:
        if item in dict.keys():
            dict[item] += 1
        else:
            dict.setdefault(item, 1)


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
displayInventory(inventory)
addInventory(dragonLoot, inventory)
displayInventory(inventory)
