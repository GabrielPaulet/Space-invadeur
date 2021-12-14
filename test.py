#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:55:26 2021

@author: g.paulet-duprat
"""
import tkinter as tk

window = tk.Tk()
window.title("Oui")
window.geometry("200x100")

Frame1 = tk.Frame(window, bg="black", relief="groove")
Frame1.pack(side="left",padx="10",pady="10")
window.mainloop()