# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:49:28 2019

@author: Minimol
"""

import pprint
# qstn no:1
dict = {}
print(dict)

# Qstn no: 2
dict= {'foo' : 42}
print(dict)

#Qstn no:4
spam = {'bar': 100}
try:
    print(spam['foo'])
except KeyError:
    print('KeyError , Please check the key')

print(spam['bar'])

# qstn no : 5 & 6
spam = {'cat' : 'puppy', 'dog': 'blacky'}
val = 'cat' in spam.keys()
print(val)
val = 'cat' in spam
print(val)
val = 'cat' in spam.values()
print(val)


# Qstn no:7

spam = { 'size': ' big', 'cat' : 'puppy' ,'dog': 'blacky'}
if 'color' not in spam:
    spam['color'] = 'black'
print(spam)

spam.setdefault('smell' , 'good')
pprint.pprint(spam)
