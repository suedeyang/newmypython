# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:31:00 2020

@author: suedeyang
"""


import cv2
cap=cv2.VideoCapture(0)
pre_img=None

while cap.isOpened():
    success,img=cap.read()
    if success:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img_now=cv2.GaussianBlur(gray,(13,13),5)
        if pre_img is not None:
            diff=cv2.absdiff(img_now,pre_img)
            ret,thresh=cv2.threshold(diff,25,255,cv2.THRESH_BINARY) #設定閥值25 以下的全部改為0  以上的全部改為255 ret為傳回之門檻值
            contours,_=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #描述輪廓 _ 用來承接沒用的回傳值 這邊跟書上不同 書上回傳值有3個 其實只有兩個
            if contours:
                cv2.drawContours(img,contours,-1,(255,255,255),2)
                print('偵測到移動')
            else:
                print('靜止畫面')
            
        cv2.imshow("frame",img)
        pre_img=img_now.copy()
    k=cv2.waitKey(50)
    if k == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        break
            
            
    