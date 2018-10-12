inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

max_fruits = max(inventory, key = lambda fruit : inventory[fruit])

print(max_fruits)