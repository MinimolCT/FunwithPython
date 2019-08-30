# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:21:55 2019

@author: Minimol
"""

# inventory.py
#stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL IN THE CODE HERE
        print(str(v) + ' ' + k)
        item_total = item_total + int(v)
    print("Total number of items: " + str(item_total))

stuff = {}
print('Enter enter the number of items to include')
limit = int(input())
print('Enter the items as : Key , then press ENTER then Value')
for i in range(limit):
    keyName = input()
    valName = input()
    stuff.setdefault(str(keyName) , valName)
    
print(stuff)
displayInventory(stuff)