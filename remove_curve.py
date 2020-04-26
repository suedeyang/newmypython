# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 10:04:58 2020

@author: suedeyang
"""


import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import cv2
import pytesseract

def rm_regression(img,border):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    denoise=cv2.fastNlMeansDenoising(gray,h=50)
    ret,thres=cv2.threshold(denoise,127,255,cv2.THRESH_BINARY_INV)
    ori=thres.copy()
    width=thres.shape[1]
    height=thres.shape[0]
    thres[height*3//5:height,0:width//2]=0 #遮掉左下區域 //代表商
    thres[height*1//4:height,width//2:width]=0 #遮掉右下區域
    #機器學習#
    border_data=np.where(thres == 255) #取得所以白點的x,y座標
    Y_label=border_data[0] #所有白點的y座標
    samples=Y_label.shape[0] #總共有sample的座標
    
    X=border_data[1].reshape(samples,1) #轉為2維資料
    regs=LinearRegression()
    feature=PolynomialFeatures(degree=2) #代表二次多項式
    X_input=feature.fit_transform(X)
    
    regs.fit(X_input,Y_label)
    print("二項函數係數:",regs.coef_)
    print("二項函數截距",regs.intercept_)
    
    #產生回歸預測值#
    newX=np.array([i for i in range(width)]) #製作新的X座標特徵
    newX=newX.reshape(newX.shape[0],1)#轉換成2維 做成一份一份
    newX_input=feature.fit_transform(newX) #再次轉成二次項特徵
    newY=regs.predict(newX_input) #輸入新的特徵給回歸函數 產生預測資料
    
    #繪製資料點#
    plt.ylim(bottom=0,top=height) #限制Y軸範圍
    plt.scatter(X,height - Y_label,color='blue',s=1)#劃出原始資料點 
    plt.scatter(newX,height-newY,color='red',s=1) #畫出回歸預測資料點
    plt.show()
    
    #製造曲線影像
    img_cuv = np.zeros_like(ori) #產生與原始黑白影像同尺寸的全黑影像 書上錯誤點
    newY=newY.round(0) #回歸線的Y座標 去除小數位
    for point in np.column_stack([newY,newX]):
        py=int(point[0]) #Y座標位置
        px=int(point[1]) #X座標位置
        w=4  #曲線寬度 可調整改變的地方
        img_cuv[py-w:py+w,px] = 255
    
    #除去曲線 相減
    diff=cv2.absdiff(ori,img_cuv)
    
    #再次降造
    denoise=cv2.fastNlMeansDenoising(diff,h=80)
    return denoise

img=cv2.imread("capcha.png")
result_img=rm_regression(img,border=9)#調整這裡
cv2.imshow('Frame2',result_img)
cv2.imshow('Frame1',img)
ocr_text=pytesseract.image_to_string(result_img)  
print('影像辨識的結果：',ocr_text)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
    
    
    