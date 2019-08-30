# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 07:21:26 2019

@author: Minimol
"""

# practiec questions 2,3,4,5

spam = [ 2 , 4, 6, 8 , 10]
spam . insert(2, 'Hello')
print(spam)
print( spam[int(int('3' * 2) // 11)])
print( spam[-1])
print(spam[:2])

# practice qstns 6,7 & 8

bacon = [3.14, 'cat', 11, 'cat', True]
print (bacon )
print ('Index o f item  : cat is ' + str(bacon.index('cat')))
bacon.append(99)
print (bacon)
bacon.remove('cat')
print (bacon)