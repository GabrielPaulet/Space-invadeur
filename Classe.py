# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 08:17:56 2022

@author: g.paulet-duprat
"""
import tkinter as tk



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
            
        

        
        
        