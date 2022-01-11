#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:25:48 2021

@author: victor.maschio
"""
import tkinter as tk
import Classe as cl
import Fonctions as f
from PIL import Image, ImageTk

# Initialisation de la fenêtre et des boutons
window =tk.Tk()
window.geometry("1920x1080")
window.title("Space invader")
cadreG= tk.Frame(window)
cadreG.pack(side='left')
cadreTop= tk.Frame(cadreG)
cadreTop.pack(side='top')

# Initialisation du score et de la vie du joueur
score= tk.Label(cadreTop,text='Score : 1000')
score.pack(side='left' ,padx=300,pady=30)
vie=tk.Label(cadreTop, text='Vies : 3')
vie.pack(side='right' ,padx=300,pady=30)

# Initialisation du canvas et des images
backImg=Image.open("images/earth.jpeg")
backimg=backImg.resize((1600, 940))
backPhoto=ImageTk.PhotoImage(backimg,master=cadreG) 


#Initialisation des tires
t1Image=Image.open("images/piou.png")
t1img=t1Image.resize((15, 40))
t1Photo=ImageTk.PhotoImage(t1img,master=cadreG)

#Initialisation des ennemies
v2Image=Image.open("images/vaisseau2.png")
v2img=v2Image.resize((100, 70))
v2Photo=ImageTk.PhotoImage(v2img,master=cadreG)

#initialisation du vaisseau
v1=cl.vaisseau(800,860,100,70,"images/vaisseau1.png")
v1Image=Image.open(v1.image)
v1img=v1Image.resize((v1.lenght, v1.height))
v1Photo=ImageTk.PhotoImage(v1img,master=cadreG)

#Création du canvas 
canvas=tk.Canvas(cadreG,bg='grey',height=940,width=1600)
backitem=canvas.create_image(800,470,image=backPhoto)
v1item=canvas.create_image(v1.x,v1.y,image=v1Photo)
v2item=f.creatEnemies(50,50,v2Photo,canvas)
canvas.pack()

# Assignation des touches
window.bind('a',lambda event : f.creatTire(v1,t1Photo,canvas,window))
window.bind('q',lambda event : v1.move(-15, 0,v1item,canvas))
window.bind('d',lambda event : v1.move(15, 0,v1item,canvas))   
   

# Initialisation des boutons de nouvelle partie et de fin
newGame= tk.Button(window,text='Nouvelle Partie',command=window.destroy)
newGame.pack(pady=300)
quitbtn= tk.Button(window,text='Quitter',command=window.destroy)
quitbtn.pack()



window.mainloop()