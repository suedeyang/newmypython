# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:37:08 2020

@author: suedeyang
"""


from gtts import gTTS
tts=gTTS(text='我是電腦',lang="zh-TW")
tts.save('audio.mp3')
