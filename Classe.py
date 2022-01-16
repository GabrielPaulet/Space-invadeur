# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 08:17:56 2022

@author: g.paulet-duprat
"""
import tkinter as tk
import Classe as cl
import Fonctions as f
import random as r
from PIL import Image, ImageTk

class jeu():
    def __init__(self):
        self.pressed={}
        self.creatInterface()
        
    def start(self):
        self._animatemove()
        self._animatetire()
        self.root.mainloop()
        
    def creatInterface(self):
        # Initialisation de la fenêtre et des boutons
        self.root =tk.Tk()
        self.root.geometry("1920x1080")
        self.root.title("Space invader")
        self.root.overrideredirect(True)
        self.root.configure(bg='black')
        self.cadreG= tk.Frame(self.root)
        self.cadreG.configure(bg='black')
        self.cadreG.pack(side='left')
        self.cadreTop= tk.Frame(self.cadreG)
        self.cadreTop.configure(bg='black')
        self.cadreTop.pack(side='top')
        
        # Initialisation du score et de la vie du joueur
        self.score= tk.Label(self.cadreTop,text='Score : 1000')
        self.score.configure(bg='black',fg='white',font=("Courier", 20))
        self.score.pack(side='left' ,padx=300,pady=30)
        self.vie=tk.Label(self.cadreTop, text='Vies : 3')
        self.vie.configure(bg='black',fg='white',font=("Courier", 20))
        self.vie.pack(side='right' ,padx=300,pady=30)
        
        # Initialisation du canvas et des images
        backImg=Image.open("images/earth.jpeg")
        backimg=backImg.resize((1800, 1100))
        self.backPhoto=ImageTk.PhotoImage(backimg,master=self.cadreG)
        
        #Initialisation des tires piou
        t1Image=Image.open("images/piou.png")
        t1img=t1Image.resize((15, 40))
        self.t1Photo=ImageTk.PhotoImage(t1img,master=self.cadreG)
        
        #Initialisation des tires piou2
        t2Image=Image.open("images/piou2.png")
        t2img=t2Image.resize((15, 40))
        self.t2Photo=ImageTk.PhotoImage(t2img,master=self.cadreG)
        
        #Initialisation des ennemies
        v2Image=Image.open("images/vaisseau2.png")
        v2img=v2Image.resize((100, 70))
        self.v2Photo=ImageTk.PhotoImage(v2img,master=self.cadreG)
        
        #initialisation du vaisseau
        self.v1=cl.vaisseau(850,940,100,70,"images/vaisseau1.png",3,'G')
        v1Image=Image.open(self.v1.image)
        v1img=v1Image.resize((self.v1.lenght, self.v1.height))
        self.v1Photo=ImageTk.PhotoImage(v1img,master=self.cadreG)
        
        #Création du canvas 
        self.canvas=tk.Canvas(self.cadreG,bg='grey',height=1000,width=1700)
        self.backitem=self.canvas.create_image(800,470,image=self.backPhoto)
        v1item=self.canvas.create_image(self.v1.x,self.v1.y,image=self.v1Photo)
        self.v1.addItem(v1item)
        self.allEnemmies=Allenemy()
        for i in range(0,6):
            v2=f.creatEnemies(50+200*i,50,self.v2Photo,self.canvas)
            v3=f.creatEnemies(50+150*i,200,self.v2Photo,self.canvas)
            self.allEnemmies.add(v2)
            self.allEnemmies.add(v3)
        self.canvas.pack()
        self.allEnemmies.move(self.canvas,self.root)
        self.setBindings()
        
        # Initialisation des boutons de nouvelle partie et de fin
        self.newGame= tk.Button(self.root,text='Nouvelle Partie',command=self.root.destroy)
        self.newGame.configure(bg='black',fg='white',font=("Courier", 10))
        self.newGame.pack(pady=300)
        self.quitbtn= tk.Button(self.root,text='Quitter',command=self.root.destroy)
        self.quitbtn.configure(bg='black',fg='white',font=("Courier", 10))
        self.quitbtn.pack()
        
    def setBindings(self):
        for char in ["q","d","a"]:
            self.root.bind("<KeyPress-%s>" % char, self._pressed)
            self.root.bind("<KeyRelease-%s>" % char, self._released)
            self.pressed[char] = False
            
    def _animatemove(self):
        if self.pressed["q"]: self.v1.move(-15,0,self.canvas)
        if self.pressed["d"]: self.v1.move(15,0,self.canvas)
        
        self.root.after(20, self._animatemove)
        
    def _animatetire(self):
        if self.pressed["a"]: f.creatTire(self.v1,self.t1Photo,self.canvas,self.root,-10)
        ran=r.randint(0,200)
        if ran<=5 and r!=0:
            nbEnnemie=len(self.allEnemmies.enemyListe)
            for ennemie in self.allEnemmies.enemyListe:
                chance=r.randint(0,nbEnnemie)
                if chance<=ran:
                    f.creatTire(ennemie,self.t2Photo,self.canvas,self.root,10)
                    ran=ran-1
                nbEnnemie=nbEnnemie-1
        self.root.after(100, self._animatetire)
        
        
    def _pressed(self, event):
        self.pressed[event.char] = True

    def _released(self, event):
        self.pressed[event.char] = False
    

class vaisseau():
    
    def __init__(self,x,y,lenght,height,image,vie,camp):
        #x et y : coordonnées , lenght et height: dimmensions de l'image , image: liens de l'image.
        self.x=x
        self.y=y
        self.lenght=lenght
        self.height=height
        self.image=image
        self.vie=vie
        self.camp=camp
    
    def move(self,dx,dy,canvas):
        #dx et dy : variation des coordonnées, vitem: item du canvas a déplacer, canvas: zone de dessin.
        #change les coordonnées du vaisseau en leur ajoutant dx et dy.
        if self.x+dx>55 and self.x+dx<1645:    
            self.x+=dx
        self.y+=dy
        canvas.coords(self.item,self.x,self.y)
        
    def addItem(self,item):
        self.item=item
        
        
class Allenemy():
    def __init__(self):
        self.enemyListe=[]
        self.deplacement=['B','D']

    def add(self,enemy):
        self.enemyListe.append(enemy)
    
    def remove (self,enemy):
        i=self.enemyListe.index(enemy)
        self.enemyListe.pop(i)
    
    def move(self,canvas,root):
        dx=15
        if self.deplacement[1]=='D':
            maxx=0
            for i in range(0,len(self.enemyListe)):
                if self.enemyListe[i].x>maxx:
                    maxx=self.enemyListe[i].x
            if maxx+dx<1600:
                for i in range(0,len(self.enemyListe)):
                    self.enemyListe[i].move(dx,0,canvas)
            else:
                self.deplacement[0] =self.deplacement[1]
                self.deplacement[1] ='B'
        elif self.deplacement[1] =='G':
            dx=-dx
            minx=1600
            for i in range(0,len(self.enemyListe)):
                if self.enemyListe[i].x<=minx:
                    minx=self.enemyListe[i].x
            if minx+dx>=80:
                for i in range(0,len(self.enemyListe)):
                    self.enemyListe[i].move(dx,0,canvas)
            else:
                self.deplacement[0] =self.deplacement[1]
                self.deplacement[1] ='B'
        elif self.deplacement[1] =='B':
            maxy=0
            for i in range(0,len(self.enemyListe)):
                if self.enemyListe[i].y>maxy:
                    maxy=self.enemyListe[i].y
            posyenemymax = maxy + 50

            self.descente(posyenemymax,canvas,root)

            if self.deplacement[0] == 'D':
                self.deplacement[1] = 'G'
            elif self.deplacement[0] == 'G':
                self.deplacement[1] = 'D'
            self.deplacement[0] = 'B'
        root.after(30, self.move,canvas,root)

    def descente(self,posyenemymax,canvas,root):
        maxy=0
        for i in range(0,len(self.enemyListe)):
            if self.enemyListe[i].y>maxy:
                maxy=self.enemyListe[i].y
        if maxy <=880:
            if maxy <= posyenemymax:
                for i in range(0,len(self.enemyListe)):
                    self.enemyListe[i].move(0,15,canvas)
                root.after(20,self.descente,posyenemymax,canvas,root)
            
        

        
        
        