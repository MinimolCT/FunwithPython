# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:23:51 2019

@author: Minimol
"""
# magic 8 ba
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