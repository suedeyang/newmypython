# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:11:12 2020

@author: suedeyang
"""


from gtts import gTTS
import os
from pygame import mixer

mixer.init()

if not os.path.isfile("tmp.mp3"):
    tts=gTTS(text='1',lang='en')
    tts.save('tmp.mp3')
    print('不重要的mp3已經儲存')

def bot_speak(text,lang):
    try:
        mixer.music.load('tmp.mp3') #mixer下來有一個子套件music 鎖定無關緊要的mp3才能不斷重複撥放mp3
        tts=gTTS(text=text,lang=lang)
        tts.save('speak.mp3')
        mixer.music.load('speak.mp3')
        mixer.music.play()
        while mixer.music.get_busy():
            continue
    except:
        print("播放音樂失敗")

bot_speak('測試123','zh-TW')
        
        