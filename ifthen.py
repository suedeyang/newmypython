# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 19:28:27 2019

@author: YANGS
"""

temp=input("請輸入要換算的溫度")
if temp.count(".")>1:
    print("只能有一個小數點")
elif temp[1:].replace(".","").isdigit():
    if temp[0] == "-" or temp[0].isdigit():
        temp=float(temp)
        print(f'攝氏{temp}度等於華氏{(temp*9/5)+32:+5.1f}度')
    else:
        print("只能以負號或數字開頭")
else:
    print("輸入的溫度無法轉換")
        