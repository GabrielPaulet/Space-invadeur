#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:25:48 2021

@author: victor.maschio
"""
import tkinter as tk
import Classe as cl
from PIL import Image, ImageTk




    
window =tk.Tk()

window.geometry("1920x1080")
window.title("Space invader")

cadreG= tk.Frame(window)
cadreG.pack(side='left')

cadreTop= tk.Frame(cadreG)
cadreTop.pack(side='top')

score= tk.Label(cadreTop,text='Score : 1000')
score.pack(side='left' ,padx=300,pady=30)
vie=tk.Label(cadreTop, text='Vies : 3')
vie.pack(side='right' ,padx=300,pady=30)

v1=cl.vaisseau(800,860,100,70,"images/vaisseau1.png")
v1Image=Image.open(v1.image)
v1img=v1Image.resize((v1.lenght, v1.height))
v1Photo=ImageTk.PhotoImage(v1img,master=cadreG,height=100) 
canvas=tk.Canvas(cadreG,bg='grey',height=940,width=1600)
print(v1Image)

v1item=canvas.create_image(v1.x,v1.y,image=v1Photo)


            

canvas.pack()
canvas.bind("q",v1.move(-10, 0,v1item,canvas))
canvas.bind("d",v1.move(10, 0,v1item,canvas))



newGame= tk.Button(window,text='Nouvelle Partie',command=window.destroy)
newGame.pack(pady=300)
quitbtn= tk.Button(window,text='Quitter',command=window.destroy)
quitbtn.pack()



window.mainloop()