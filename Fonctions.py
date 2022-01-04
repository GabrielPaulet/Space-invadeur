#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:20:49 2021

@author: g.paulet-duprat
"""
import tkinter as tk

def creatGrille(hauteur,largeur): #largeur et hauteur sont des entiers
    grille=[]
    for indice in range(0,hauteur):
        ligne = [[0,0,0]]*largeur
        grille.append(ligne)
    return grille # Retourne une liste de ligne

def modifGrille(ligne,colonne,valeur,grille,etage): #ligne=int, colonne=int, valeur=int, grille=int
    if len(grille)>= ligne and len(grille[ligne])>=colonne:
        grille[ligne][colonne][etage]=valeur
    else:
        print("modification hors grille")

def lireGrille(ligne,colonne,grille,etage):
    valeur=-1
    if len(grille)>= ligne and len(grille[ligne])>=colonne:
        valeur=grille[ligne][colonne][etage]
    else:
        print("lecture hors grille")
    return valeur

def printGrid(Grid):

    for i in range(0,len(Grid)):

        aff=""

        for j in range(0,len(Grid[i])):

            aff+=str(Grid[i][j])+" "

        print(aff)

def deplacement(dx,dy):
    x=tk.IntVar()
    y=tk.IntVar()






#def destructionVaisseau(ligne,colonne):
    
    

    
    


        