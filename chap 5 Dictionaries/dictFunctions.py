# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:53:05 2019

@author: Minimol
"""

#Using the keys(), values(), and items() methods, a for loop can iterate over the keys, values, 
#or key-value pairs in a dictionary, respectively.

spam = {'color': 'red', 'age': 42 , 'size' : 'big' , 'efficiency' : 'high'}

print()
print(spam)

print()
#'Printing the values')

for v in spam.values():
        print(v)
        
#'Printing the keys')
print()
for k in spam.keys():
        print(k)
print()
#Printing the items together')       
for i in spam.items():
        print(i)
print()
#Printing the values and items seperately through mutiple assignment')
for k, v in spam.items():
        print('Key: ' + k + ' Value: ' + str(v))