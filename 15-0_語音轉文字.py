# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:05:19 2020

@author: suedeyang
"""

import speech_recognition as sr

def bot_listen():
    recog=sr.Recognizer() #建立語音辨識聽打員、或稱之為辨識物件
    with sr.Microphone() as source:
        audioData=recog.listen(source)
    try:
        text=recog.recognize_google(audioData, language="zh-TW")
        return text
    except:
        return '聽不懂'

question=bot_listen()
print(question)
        
