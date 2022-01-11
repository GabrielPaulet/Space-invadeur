#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:55:26 2021

@author: g.paulet-duprat
"""
import tkinter as tk
import Classe as cl
import Fonctions as f
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Oui")
window.geometry("200x100")

Frame1 = tk.Frame(window, bg="black", relief="groove")
Frame1.pack(side="left",padx="10",pady="10")
backImg=Image.open("images/earth.jpeg")
backimg=backImg.resize((4000, 6000))
backPhoto=ImageTk.PhotoImage(backimg,master=cadreG,height=100) 
backitem=canvas.create_image(800,470,image=backPhoto)
window.mainloop()