# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 19:51:20 2019

@author: YANGS
"""

i=float(input("請輸入一個正數:"))
j=0.0
while j*j < i:
    j=j+0.00001
print(f'{i}的 平方根是{j}')