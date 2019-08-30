# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:20:04 2019

@author: Minimol
"""

import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])