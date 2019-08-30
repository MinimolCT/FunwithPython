# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:44:44 2019

@author: Minimol
"""

def addToInventory(inventory, addedItems):
    # your code goes here
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i] = inventory[i] + 1
    return inventory
        
    
    
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL IN THE CODE HERE
        print(str(v) + ' ' + k)
        item_total = item_total + int(v)
    print("Total number of items: " + str(item_total))
   
    

inv = {'gold coin': 42, 'rope': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)