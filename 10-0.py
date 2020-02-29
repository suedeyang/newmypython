# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:19:16 2020

@author: suedeyang
"""


import cv2

try:
    img=cv2.imread('car.jpg') 
    img_small=cv2.resize(img,(300,100))
    cv2.imshow('Frame1',img)#沒開window直接讀取 當視窗不存在時 會自動建立一個視窗 frame1 是視窗的名稱
    cv2.imshow('Frame2',img_small)
    cv2.waitKey(3000)  #單位為ms 或按下any key
    cv2.destroyAllWindows()
    try:
        cv2.imwrite('small.jpg',img_small)
        print('Saved')
    except:
        print('Error')
        
except:
    print('讀取錯誤')
    
    
                  