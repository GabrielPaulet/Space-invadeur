#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:25:48 2021

@author: victor.maschio
"""
import tkinter as tk



def createWindow():
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
    
    canvas=tk.Canvas(cadreG,bg='grey',height=940,width=1600)
    canvas.pack()
    
    newGame= tk.Button(window,text='Nouvelle Partie',command=window.destroy)
    newGame.pack(pady=300)
    quitbtn= tk.Button(window,text='Quitter',command=window.destroy)
    quitbtn.pack()
    return window



fenetre=createWindow()


fenetre.mainloop()