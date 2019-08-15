def displayInventory(inventory):
    print('Inventory:')
    total_items= 0
    for x, y in inventory.items():
        print(str(y) + ' ' + x)
        total_items = total_items + y
    print('Total number of items: ' + str(total_items))

def addToInventory(inventory, addedItems):
    print('Inventory:')
    for i in addedItems:
        if i in inventory:
            inventory[i] = inventory[i] + 1
        else:
            inventory[i] = 1
    total_items= 0
    for x, y in inventory.items():
        print(str(y) + ' ' + x)
        total_items = total_items + y
    print('Total number of items: ' + str(total_items))

invent = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(invent, dragonLoot)
