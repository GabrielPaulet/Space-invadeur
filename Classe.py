# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 08:17:56 2022

@author: g.paulet-duprat
"""

class board():

    def __init__(self,lenght,height):
        self.entityGrid= self.createGrid(lenght,height)
        self.allyShootGrid= self.createGrid(lenght,height)
        self.enemyShootGrid= self.createGrid(lenght,height)

    def createGrid(self,lenght,height):
        Grid=[]
        for i in range (0,lenght):
            Grid.append([])
        for i in range(0,lenght):
            for j in range (0,height):
                Grid[i].append(0)
        return Grid


    def printGrid(self,number):
        if number ==0:
            Grid=self.entityGrid
        elif number ==1:
            Grid=self.allyShootGrid
        else:
            Grid=self.enemyShootGrid
        for i in range(0,len(Grid)):
            aff=""
            for j in range(0,len(Grid[i])):
                aff+=str(Grid[i][j])+" "
            print(aff)


A=board(20,30)
A.printGrid(1)
print('\n')
A.printGrid(2)
print('\n')
A.printGrid(13)