# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:48:36 2019

@author: Minimol
"""

# Collatz Sequence

def collatz( number):
    if number % 2 == 0:
        print (number // 2)
        return number // 2
    else :
        print (3 * number + 1 )
        return 3 * number + 1
    
print ( 'Enter a number ')
num = int(input())
val = collatz(num)
while True:
    if val == 1:
        break
    else : 
        val = collatz(val)