# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 08:08:10 2019

@author: Minimol
"""

# difference between append()  and insert ()
#practice qstn 10

print('Print original list')
spam = [ 'cat', 'rat', 'fish' ]
print (spam)
print()


print('List after appending elephant')
spam.append('elephant')
print(spam)
print()


print('List after inserting duck at index number 2')
spam .insert(2, 'duck')
print(spam)
print()
# Two methods to remove the list values from a list
#practice qstn 11

print('List after removing cat')
spam.remove('rat')
print(spam)
print()


print( 'List after deleting value at index number 1')
del spam[1]
print(spam)
print()