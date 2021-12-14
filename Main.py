#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:21:08 2021

@author: g.paulet-duprat
"""

import Fonctions as f


grille=f.creatGrille(30, 30)
f.modifGrille(1, 2, 1, grille,0)
x=f.lireGrille(1, 2, grille,0)
for ligne in reversed(grille):
    print(ligne)
    
print (x)
    
