# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 14:23:06 2019

@author: YANGS
"""

s=[(3,4),(2,4),(5,3)]

def calc(w,h):
    return w*h

def calcAll(conta,func):
    for r in conta:
        print(func(r[0],r[1]),end='  ')

calcAll(s,calc)