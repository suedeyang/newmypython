# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 19:46:51 2019

@author: YANGS
"""

j=float(input("請輸入一個數字:"))
i=0
while i*i<j:
    i+=0.00001
print(i)
