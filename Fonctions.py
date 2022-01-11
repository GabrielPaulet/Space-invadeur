#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:20:49 2021

@author: g.paulet-duprat
"""
import tkinter as tk
import Classe as cl
from PIL import Image, ImageTk

def creatTire(v1,t1Photo,canvas,window):
    t1=cl.vaisseau(0,0,15,40,"images/piou.png")
    t1.x=v1.x
    t1.y=v1.y -60
    t1item=canvas.create_image(t1.x,t1.y,image=t1Photo)
    automove(t1,t1item,canvas,window)
    
def creatEnemies(x,y,v2Photo,canvas):
    v2=cl.vaisseau(x,y,100,70,"images/piou.png")
    v2item=canvas.create_image(x,y,image=v2Photo)
    return v2item
    
def automove(t1,t1item,canvas,window):
    if t1.y>50:
        t1.move(0,-10,t1item,canvas)
        window.after(10,automove,t1,t1item,canvas,window)
    else: canvas.delete(t1item)
        




#def destructionVaisseau(ligne,colonne):
    
    

    
    


        