# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 11:29:39 2020

@author: suedeyang
"""


import pandas as pd

#df=pd.DataFrame([[1,2],[3,4],[5,6]],index=['a','b','c'])
#print(df.shape)
#print(df.columns)

s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
r=s.rolling(window=3) #建立window為3的窗戶  每3個一抓
print(r.mean())