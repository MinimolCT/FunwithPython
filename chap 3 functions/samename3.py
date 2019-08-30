# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 15:24:18 2019

@author: Minimol
"""

# This program Clears the local and global scope of a variable.

# If there is a global statement for that variable in a function, it is a global variable.
def spam():
    global eggs
    eggs = 'spam' # this is the global

# Otherwise, if the variable is used in an assignment statement in the function, 
#it is a local variable.
def bacon():
    eggs = 'bacon' # this is a local
    print(eggs)
    
# But if the variable is not used in an assignment statement, it is a global variable.    
def ham():
    print(eggs) # this is the global

# If a variable is being used in the global scope (that is, outside of all functions),
# then it is always a global variable.
eggs = 42 # this is the global
print( eggs)
spam()
ham()
bacon()
print(eggs)  # prints spam because it is altered by spam function