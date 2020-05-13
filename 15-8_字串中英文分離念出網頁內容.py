# -*- coding: utf-8 -*-
"""
Created on Sun May  3 01:17:24 2020

@author: suedeyang
"""


import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import os
from pygame import mixer
import re
mixer.init()


def bot_get_wiki(keyword):
    response=requests.get("https://zh.wikipedia.org/zh-tw/"+keyword)
    bs=BeautifulSoup(response.text,'lxml')
    p_list=bs.find_all('p')
    for p in p_list:
        if keyword in p.text[0:10]:
            return p.text


def bot_speak_re(sentense):
    s1=re.sub(r'\[[^\]]+\]','',sentense) #re把註解的部分用 re.sub的方式去除掉
    print(s1)
    en_list=re.findall(r'[a-zA-Z \-]+',s1) #取得英文字的串列
    s2=re.sub(r'[a-zA-Z \-]+','@English@',s1)
    all_list=s2.split('@')
    index=0
    for text in all_list:
        if text != 'English':
            bot_speak(text,'zh-TW')
        else:
            bot_speak(en_list[index],'en')
            index += 1



def bot_speak(text,lang):
    if not os.path.isfile("tmp.mp3"):
        tts=gTTS(text='1',lang='en')
        tts.save('tmp.mp3')
        print('不重要的mp3已經儲存')
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

sentense=bot_get_wiki('愛因斯坦')
bot_speak_re(sentense)