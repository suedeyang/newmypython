# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 20:22:03 2019

@author: YANGS
"""

drinks=('紅茶','綠茶','咖啡')
prices=('10','20','30')
matchs=('a','b','c','d')

for drink,price,match in zip(drinks,prices,matchs):
    print(drink,price,match)