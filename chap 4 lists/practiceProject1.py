# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 08:45:08 2019

@author: Minimol
"""

# practice project 1

def commaCode(spamList):
    newList= ''
    for i in range ( len(spamList)-2):
        newList = newList + spamList[i] + ', '
    newList= newList+ spamList[-2] + ' and ' + spamList[-1]   
    return newList
    
    
    
#spam = ['apples', 'bananas', 'tofu', 'cats']
spam = []
print ('Enter the limit for your list')
limit= int(input())
print('Enter the list items')
for i in range(limit):
    spam.append(input())
    
newList = commaCode(spam)
print (newList)
