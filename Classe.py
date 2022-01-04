# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 08:17:56 2022

@author: g.paulet-duprat
"""
import tkinter as tk



class vaisseau():
    
    def __init__(self,x,y,lenght,height,image):
        self.x=x
        self.y=y
        self.lenght=lenght
        self.height=height
        self.image=image
    
    def move(self,dx,dy,vitem,canvas):
        self.x+=dx
        self.y+=dy
        print(self.x)
        canvas.coords(vitem,self.x,self.y)
        
        

        
        
        