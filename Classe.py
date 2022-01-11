# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 08:17:56 2022

@author: g.paulet-duprat
"""
import tkinter as tk
import Classe as cl
import Fonctions as f
from PIL import Image, ImageTk

class jeu():
    def __init__(self):
        self.pressed={}
        self.creatInterface()
        
    def start(self):
        self._animate()
        self.root.mainloop()
        
    def creatInterface(self):
        # Initialisation de la fenêtre et des boutons
        self.root =tk.Tk()
        self.root.geometry("1920x1080")
        self.root.title("Space invader")
        self.cadreG= tk.Frame(self.root)
        self.cadreG.pack(side='left')
        self.cadreTop= tk.Frame(self.cadreG)
        self.cadreTop.pack(side='top')
        
        # Initialisation du score et de la vie du joueur
        self.score= tk.Label(self.cadreTop,text='Score : 1000')
        self.score.pack(side='left' ,padx=300,pady=30)
        self.vie=tk.Label(self.cadreTop, text='Vies : 3')
        self.vie.pack(side='right' ,padx=300,pady=30)
        
        # Initialisation du canvas et des images
        backImg=Image.open("images/earth.jpeg")
        backimg=backImg.resize((1600, 940))
        self.backPhoto=ImageTk.PhotoImage(backimg,master=self.cadreG)
        
        #Initialisation des tires
        t1Image=Image.open("images/piou.png")
        t1img=t1Image.resize((15, 40))
        self.t1Photo=ImageTk.PhotoImage(t1img,master=self.cadreG)
        
        #Initialisation des ennemies
        v2Image=Image.open("images/vaisseau2.png")
        v2img=v2Image.resize((100, 70))
        self.v2Photo=ImageTk.PhotoImage(v2img,master=self.cadreG)
        
        #initialisation du vaisseau
        self.v1=cl.vaisseau(800,860,100,70,"images/vaisseau1.png")
        v1Image=Image.open(self.v1.image)
        v1img=v1Image.resize((self.v1.lenght, self.v1.height))
        self.v1Photo=ImageTk.PhotoImage(v1img,master=self.cadreG)
        
        #Création du canvas 
        self.canvas=tk.Canvas(self.cadreG,bg='grey',height=940,width=1600)
        self.backitem=self.canvas.create_image(800,470,image=self.backPhoto)
        self.v1item=self.canvas.create_image(self.v1.x,self.v1.y,image=self.v1Photo)
        self.v2item=f.creatEnemies(50,50,self.v2Photo,self.canvas)
        self.canvas.pack()
        self.setBindings()
        
        # Initialisation des boutons de nouvelle partie et de fin
        self.newGame= tk.Button(self.root,text='Nouvelle Partie',command=self.root.destroy)
        self.newGame.pack(pady=300)
        self.quitbtn= tk.Button(self.root,text='Quitter',command=self.root.destroy)
        self.quitbtn.pack()
        
    def setBindings(self):
        for char in ["q","d","a"]:
            self.root.bind("<KeyPress-%s>" % char, self._pressed)
            self.root.bind("<KeyRelease-%s>" % char, self._released)
            self.pressed[char] = False
            
    def _animate(self):
        if self.pressed["q"]: self.v1.move(-15,0,self.v1item,self.canvas)
        if self.pressed["d"]: self.v1.move(15,0,self.v1item,self.canvas)
        if self.pressed["a"]: f.creatTire(self.v1,self.t1Photo,self.canvas,self.root)
        self.root.after(20, self._animate)
        
    def _pressed(self, event):
        self.pressed[event.char] = True

    def _released(self, event):
        self.pressed[event.char] = False
    

class vaisseau():
    
    def __init__(self,x,y,lenght,height,image):
        #x et y : coordonnées , lenght et height: dimmensions de l'image , image: liens de l'image.
        self.x=x
        self.y=y
        self.lenght=lenght
        self.height=height
        self.image=image
    
    def move(self,dx,dy,vitem,canvas):
        #dx et dy : variation des coordonnées, vitem: item du canvas a déplacer, canvas: zone de dessin.
        #change les coordonnées du vaisseau en leur ajoutant dx et dy.
        if self.x+dx>55 and self.x+dx<1545:    
            self.x+=dx
        self.y+=dy
        canvas.coords(vitem,self.x,self.y)
        

class enemy():
    def __init__(self,x,y,lenght,height,image,vie):
        self.x=x
        self.y=y
        self.lenght=lenght
        self.height=height
        self.image=image
        self.vie=vie
        
    def move(self,dx,dy):
        self.x+=dx
        self.y+=dy
        
class Allenemy():
    def __init__(self):
        self.enemyListe=[]
        self.deplacement='D'

    def add(self,enemy):
        self.enemyListe.append(enemy)
    
    def remove (self,enemy):
        i=self.enemyListe.index(enemy)
        self.enemyListe.pop(i)
    
    def move(self):
        dx=15
        if self.deplacement=='D':
            maxx=0
            for i in range(0,len(self.enemyListe)):
                if self.enemyListe[i].x>maxx:
                    maxx=self.enemyListe[i].x
            if maxx+dx<1600:
                for i in range(0,len(self.enemyListe)):
                    self.enemyListe[i].move(dx,0)
            else:
                self.deplacement ='B'
        elif self.deplacement=='G':
            dx=-dx
            minx=1600
            for i in range(0,len(self.enemyListe)):
                if self.enemyListe[i].x<=minx:
                    minx=self.enemyListe[i].x
            if minx+dx>=0:
                for i in range(0,len(self.enemyListe)):
                    self.enemyListe[i].move(dx,0)
            else:
                self.deplacement ='B'
        elif self.deplacement=='B':
            dy=50
            for i in range(0,len(self.enemyListe)):
                self.enemyListe[i].move(0,dy)
            
        

        
        
        