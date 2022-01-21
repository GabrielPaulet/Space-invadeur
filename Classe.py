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
        self.tiresG=[]
        self.tiresM=[]
        self.creatInterface()
        
    def start(self):
        self._animatemove()
        self._animatetire()
        self.boom()
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
        self.allEnemmies=Allenemy(self.v2Photo)
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
        if self.pressed["a"]: 
            self.tiresG.append(self.creatTire(self.v1))
        
        for ennemie in self.allEnemmies.enemyListe:
            chance=r.randint(0,100)
            if chance<=10 and ennemie.y<950 and ennemie.y>140:
                self.tiresM.append(self.creatTire(ennemie))
        self.root.after(200, self._animatetire)
        
    def _pressed(self, event):
        self.pressed[event.char] = True

    def _released(self, event):
        self.pressed[event.char] = False
        
    def collision(self,entite1, entite2):
        if self.canvas.bbox(entite1) != None and self.canvas.bbox(entite2) != None:

            #On récupère les coordonées de l'objet 1
            x_1 = self.canvas.bbox(entite1)[0] 
            x_2 = self.canvas.bbox(entite1)[2] 
            y_1 = self.canvas.bbox(entite1)[1] 
            y_2 = self.canvas.bbox(entite1)[3] 
    
            # les coordonnées de la deuxième entité
            coords = self.canvas.bbox(entite2)
    
            #On vérifie s'i y a une collison par la gauche de l'entité 2 sur l'entité 1
            if (x_2 > coords[0]> x_1) and (y_1 < coords[1]< y_2):
                return True
    
            #On vérifie s'i y a une collison par la droite de l'entité 2 sur l'entité 1
            elif (x_2 > coords[2]> x_1) and (y_1 < coords[3]< y_2):
                return True
        
    def creatTire(self,v):
        if v.camp=="G":
            vitesse=-20
            t1=cl.vaisseau(0,0,15,40,"images/piou.png",1,"G")
            imagePiou=self.t1Photo
        else:
            vitesse=20
            t1=cl.vaisseau(0,0,15,40,"images/piou2.png",1,"M")
            imagePiou=self.t2Photo
        if vitesse<0:
            posy=-60
        else:
            posy=60
        t1.x=v.x
        t1.y=v.y +posy
        t1item=self.canvas.create_image(t1.x,t1.y,image=imagePiou)
        t1.addItem(t1item)
        self.automove(vitesse,t1)
        return t1
        
    def automove(self,vitesse,t1):
        if t1.y>50 and t1.y<950:
            t1.move(0,vitesse,self.canvas)
            self.root.after(10,self.automove,vitesse,t1)
        elif t1 in self.tiresG or t1 in self.tiresM:
            self.suprTire(t1)
        
    def suprTire(self,t1):
        if t1.camp=="G":
            self.tiresG.remove(t1)
            self.canvas.delete(t1.item)
        else:
            self.tiresM.remove(t1)
            self.canvas.delete(t1.item)
    
    def boom(self):
        for tire in self.tiresG:
            for enemy in self.allEnemmies.enemyListe:
                colli=self.collision(enemy.item, tire.item)
                if colli:
                    self.suprTire(tire)
                    self.allEnemmies.removeEnemy(enemy)
                    self.canvas.delete(enemy.item)
                    
        for tire in self.tiresM:
            colli2=self.collision(self.v1.item,tire.item)
            if colli2:
                self.suprTire(tire)
        self.root.after(20, self.boom)
                    
    

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
    def __init__(self,V2Photo):
        self.level=f.OuvrirFichier("enemy.txt")
        self.enemyListe=[]
        self.deplacement=['B','D']
        self.v2Photo=V2Photo

    def add(self,enemy):
        self.enemyListe.append(enemy)
    
    def removeEnemy (self,enemy):
        self.enemyListe.remove(enemy)
    
    def move(self,canvas,root):
        dx=15
        if self.enemyListe ==[]:
            self.spawnEnemy(canvas)
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
            self.spawnEnemy(canvas)
            maxy=0
            for i in range(0,len(self.enemyListe)):
                if self.enemyListe[i].y>maxy:
                    maxy=self.enemyListe[i].y
            posyenemymax = maxy + 80
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
        if posyenemymax>maxy+100:
            posyenemymax=maxy+100
        if maxy <=880:
            if maxy <= posyenemymax:
                for i in range(0,len(self.enemyListe)):
                    self.enemyListe[i].move(0,15,canvas)
                root.after(20,self.descente,posyenemymax,canvas,root)
    
    def spawnEnemy(self,canvas):
        if self.level==[]:
            self.level=f.OuvrirFichier("enemy.txt")
        if self.deplacement[0] == 'D':
            value = 600
        elif self.deplacement[0] == 'G':
            value = 85
        elif self.deplacement[0] == 'B':
                value = 100
        for i in range (0,len(self.level[0])):
            if self.level[0][i] == '1' :
                v2=f.creatEnemies(value +150*i,-30,self.v2Photo,canvas)
                self.add(v2)
        self.level.pop(0)
            
        

        
        
        