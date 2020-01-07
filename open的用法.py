# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 06:28:06 2020

@author: YANGS
"""

f=open('a.txt','w',encoding='utf-8')
f.write('''
白日依山盡
        ''')
f.close()
f=open('a.txt','r',encoding='utf-8')
s=f.readlines()
print(s)