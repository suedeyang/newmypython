# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 11:09:45 2020

@author: suedeyang
"""


import pytesseract
from selenium import webdriver
import cv2

url="https://portal.kh.edu.tw/"
#driver=webdriver.Chrome()
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options = option) #加入選項來指定不要有自動控制的訊息
driver.get(url)
#driver.find_element_by_id("loginname").click()
driver.find_element_by_name("loginpswd").click()
#driver.find_element_by_id("loginname").send_keys("")


"""

img=cv2.imread('verify_img.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
denoise=cv2.fastNlMeansDenoising(gray,h=30)
gaus=cv2.GaussianBlur(gray,(5,5),0)
ret,thresh=cv2.threshold(denoise,127,255,cv2.THRESH_BINARY_INV)#灰階低於127的通通轉為255，高於的轉為0(跟p.13-23恰巧相反，黑白互換)



cv2.imshow("Frame1",img)
cv2.imshow("Frame2",denoise)
cv2.imshow("Frame3",gaus)
cv2.imshow("Frame4",thresh)
ocr_txt=pytesseract.image_to_string(gaus)
print("影像辨識的結果是:",ocr_txt)
cv2.waitKey(0)
cv2.destroyAllWindows()  
"""