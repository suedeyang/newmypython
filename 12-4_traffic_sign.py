# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 22:44:31 2020

@author: suedeyang
"""


import cv2
img=cv2.imread("pic_turnR.jpg")
detector=cv2.CascadeClassifier("harr_turnR.xml") #建立分類器物件
signs=detector.detectMultiScale(img,scaleFactor=1.01,minNeighbors=15,minSize=(30,30))

if len(signs)>0: #表示有偵測到東西
    for (x,y,w,h) in signs:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
else:
    print('fail')
cv2.imshow("Frame",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
