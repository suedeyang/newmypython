# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:01:11 2020

@author: suedeyang
"""


import pandas as pd
s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])

print(s)
type(s)

print(s[4])
print(s['a'])

print('----------------')


df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],index=['a','b','c'])

print(df)
print('形狀',df.shape)
print('columns',df.columns)
print('index',df.index)
print('head',df.head(2))

print('----------------')
print(df[0])
print('----------------')

df.info()

print('----------------')

print(df.describe())