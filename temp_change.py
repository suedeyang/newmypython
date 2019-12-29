# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 20:03:11 2019

@author: YANGS
"""
s=input("請輸入溫度:")
if s.count(".")>1:
    print('只能有一個小數點')
elif s[1:].replace('.','').isdigit():
    if s[0] == '-' or s[0].isdigit():
        temp=float(s)
        print(f'攝氏{temp}度 等於華氏{(temp*9/5)+32:+5.1f}度')
        print(f'華氏{temp}度 等於攝氏{(temp-32)*5/9:+5.1f}度')
    else:
        print('只能以數字或負號開頭')
else:
    print('無法轉換')
        
    