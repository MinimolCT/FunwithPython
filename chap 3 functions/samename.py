# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:17:25 2019

@author: Minimol
"""

def spam():
       eggs = 'spam local'
       print(eggs) # prints 'spam local'
def bacon():

       eggs = 'bacon local'
       print(eggs) # prints 'bacon local'
       spam()
       print(eggs) # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global'