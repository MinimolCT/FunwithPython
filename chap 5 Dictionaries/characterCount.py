# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:53:05 2019

@author: Minimol
"""

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

print()
print(message)
print()
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)