# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 13:52:17 2019

@author: YANGS
"""

while True:
    s=input("請輸入100的除數")
    try:
        i=100/float(s)
    except ValueError:
        print("發生ValueError")
    else:
        print('100除',s,"=",i)
        break
    finally:
        print("你輸入的值是",s)
    print("進入下一個迴圈")
print("程式結束")
        
        