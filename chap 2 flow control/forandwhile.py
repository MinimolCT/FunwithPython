# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:54:35 2019

@author: Minimol
"""

# program to show for loop and while loop

print('Printing numbers using for loop')
for i in range (11):
    print(i)
i = 0
print('Printing numbers using while loop')
while i <= 10:
    print(i)
    i = i + 1
    
# now the usage of break and continue

print('Program come out of the loop when it encounters a break. Here it breaks at 5')
for i in range (11):
    if i == 5:
        print('Encountered a break')
        break
    print(i)
print('Program skips one iteration of the loop when it encounters a continue. Here it breaks at 5')
for i in range (11):
    if i == 5:
        print('Encountered continue')
        continue
        
    print(i)