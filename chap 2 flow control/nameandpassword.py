# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:16:28 2019

@author: Minimol
"""

print('Enter your name')
while True:
    name= input()
    if name == 'Mini':
        print('Welcome Mini, Enter your password')
        while True:
            passw = input()
            if passw == 'password':
                break
            else :
                print('Sorry, Incorrect password. Please Re-Enter')
        print('Access Granted')
        break
    print('Not authorised ,Re-Enter your name')
           
        
        
    
    