#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:20:49 2021

@author: g.paulet-duprat
"""
import tkinter as tk
import Classe as cl
from PIL import Image, ImageTk

def init_info():
    launch = tk.Tk()
    launch.geometry("600x800")
    launch.title("Space invader Instruction")
    launch.configure(bg='black')
    instruction='Bonjour, nous avons recréer le fameux space invaders\n mais à notre sauce vous pourrez :'
    info= tk.Label(launch,text=instruction)
    info.configure(bg='black',fg='white',font=("Courier", 10))
    info.pack(padx=30,pady=30)
    begin= tk.Button(launch,text='Commencer',command=launch.destroy)
    begin.configure(bg='black',fg='white',font=("Courier", 10))
    begin.pack()
    launch.mainloop()
    jeu=cl.jeu()


def creatTire(v1,t1Photo,canvas,window,vitesse):
    if vitesse<0:
        posy=-60
    else:
        posy=60
    if v1.camp=="G":
        t1=cl.vaisseau(0,0,15,40,"images/piou.png",1,"T")
    else:
        t1=cl.vaisseau(0,0,15,40,"images/piou2.png",1,"T")
    t1.x=v1.x
    t1.y=v1.y +posy
    t1item=canvas.create_image(t1.x,t1.y,image=t1Photo)
    t1.addItem(t1item)
    automove(t1,t1item,canvas,window,vitesse)
    
def creatEnemies(x,y,v2Photo,canvas):
    v2=cl.vaisseau(x,y,100,70,"vaisseau2.png",1,"M")
    v2item=canvas.create_image(x,y,image=v2Photo)
    v2.addItem(v2item)
    return v2
    
def automove(t1,t1item,canvas,window,vitesse):
    if t1.y>50 and t1.y<950:
        t1.move(0,vitesse,canvas)
        window.after(10,automove,t1,t1item,canvas,window,vitesse)
    else: canvas.delete(t1item)
    
def OuvrirFichier(nom,car='/'):
    monFichier=open(nom, encoding='utf-8')
    Fichier=monFichier.readlines()
    monFichier.close()
    for i in range(len(Fichier)):
        a=Fichier[i].split(car)
        Fichier[i]=a[0:-1]
    return Fichier
        




#def destructionVaisseau(ligne,colonne):
    
    

    
    


        