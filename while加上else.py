# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 21:08:50 2019

@author: YANGS
"""
s=''
while s != "喵喵":
    if s != "":
        print("不對喔!!!")
    s=input("請輸入密碼:")
    if s =="out":
        break
else:
    print("pass")
        