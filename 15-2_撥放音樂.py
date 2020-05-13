# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:47:44 2020

@author: suedeyang
"""

from gtts import gTTS
from pygame import mixer 


tts=gTTS(text="楊恩尼你複習功課結束了嗎?",lang='zh-TW')
tts.save('audio.mp3')

mixer.init()
mixer.music.load('audio.mp3')
mixer.music.play()
