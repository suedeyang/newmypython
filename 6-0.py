# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 07:02:21 2020

@author: YANGS
"""

def get_setting():
    res=[]
    try:
        with open('stock.txt') as f:
            slist=f.readlines()
            print("讀入資料:",slist)
            for lst in slist:
                s=lst.split(',')
                res.append([s[0],float(s[1]),float(s[2])])
    except:
        print("讀檔錯誤")
    return res

stock=get_setting()
print(stock)                