# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:13:52 2019

@author: Minimol
"""

import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)