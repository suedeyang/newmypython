# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 14:23:06 2019

@author: YANGS
"""

def calc(w,h):
    return((w+h)*2,w*h,'正方形' if w==h else "長方形")

a=calc(2,3)
print(a)