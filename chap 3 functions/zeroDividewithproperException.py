# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:09:59 2019

@author: Minimol
"""
# Try and except for exception handling
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))