# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 20:46:02 2019

@author: YANGS
"""
def prnSum(name,*args): #注意要加上*
    print(name,args,'=',sum(args))

prnSum('總和',1,2,3,4,5)


def prnPrice(name,**kwargs):
    print(name,kwargs)
    
prnPrice("飲料",紅茶=80,綠茶=50,可樂=20)
