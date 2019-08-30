# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:55:44 2019

@author: Minimol
"""

print ('Hello, Whats your name?')
name = input()
if name == 'Mini':
    print ('you are welcome, Mini')
    print('enter your password')
    passw = input()
    if passw == 'Minimol' or passw =='minimol':
        print ('Access granted')
    else:
        print('Access denied')
else:
    print ('You are not authorised to access this page')
