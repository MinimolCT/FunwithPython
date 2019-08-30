# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:08:29 2019

@author: Minimol
"""

# try and execpt code in printing oart
# once the execution jumps to the code in the except clause, 
#it does not return to the try clause
def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')