# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 09:50:02 2020

@author: suedeyang
"""


import subprocess as sp
print('主程序開始')

p=sp.Popen('python 8-18.py',
           shell=True,
           stdout=sp.PIPE,stderr=sp.PIPE)
result=p.communicate() #回傳一個tuple結果(標準輸出結果,標準錯誤結果)

print('Returncode:',p.returncode) #輸出0代表執行正確  輸出1代表錯誤
print('標準結果輸出:',(result[0]) #輸出結果不支援中文 #str(result[0],'utf8')轉換成utf8格式
print('標準錯誤輸出:',(result[1])

print('主程序結束')
