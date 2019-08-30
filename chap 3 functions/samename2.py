# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:23:03 2019

@author: Minimol
"""

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)