# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

while True:
    print('Enter your name')
    name= input()
    if name == 'Mini':
        print('Welcome Mini, Enter your password')
        while True:
            passw = input()
            if passw == 'password':
                break
            else :      
                print ('Wrong password, Re-Enter')
        print ('Access granted')
        break
    else:
        print('Not authoriesd ,Re- enter your name')
     
      