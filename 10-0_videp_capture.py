# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:06:43 2020

@author: suedeyang
"""


import cv2
capture=cv2.VideoCapture(0)
success,img=capture.read()
print(success)
cv2.imshow('Frame',img)

keys=cv2.waitKey(10000)
print(keys)
cv2.destroyAllWindows()

capture.release() 