# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:27:40 2019

@author: Minimol
""" 
 
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]




def printTable(tableList):
    colWidths = []
    colWidths = [0] * len(tableList)
   # print(colWidths)
    # Finding the max width of strings in each coloumn
    for i in range(0 , len(tableList[1])) :  
        for j in range(0 , len(tableList)) :  
            if len(tableList[j][i]) > colWidths[j] : 
                colWidths[j] = len(tableList[j][i])
        print()  
   # print(colWidths)
    
    for i in range(0 , len(tableList[1])) :  
        for j in range(0 , len(tableList)) :  
            print('     ' + tableList[j][i] . rjust(colWidths[j]) , end=" ") 
        print()   


print()
print('List OF List Display As a Grid' . center(50, '-'))
printTable(tableData)

    