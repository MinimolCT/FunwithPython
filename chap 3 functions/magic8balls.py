# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:15:55 2019

@author: Minimol
"""


# magic 8 balls program
import random
def getAnswer(answerNumber):
       if answerNumber == 1:
           return 'It is certain'
       elif answerNumber == 2:
           return 'It is decidedly so'
       elif answerNumber == 3:
           return 'Yes'
       elif answerNumber == 4:
           return 'Reply hazy try again'
       elif answerNumber == 5:
           return 'Ask again later'
       elif answerNumber == 6:
           return 'Concentrate and ask again'
       elif answerNumber == 7:
           return 'My reply is no'
       elif answerNumber == 8:
           return 'Outlook not so good'
       elif answerNumber == 9:
           return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)