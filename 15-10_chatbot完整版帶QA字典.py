# -*- coding: utf-8 -*-
"""
Created on Sun May  3 05:10:30 2020

@author: suedeyang
"""


import requests,os,re
from bs4 import BeautifulSoup
from hanziconv import HanziConv
import speech_recognition as sr
from gtts import gTTS
from pygame import mixer 
  
    


def bot_listen():
    recog=sr.Recognizer() #建立語音辨識聽打員、或稱之為辨識物件
    with sr.Microphone() as source:
        audioData=recog.listen(source)
    try:
        text=recog.recognize_google(audioData, language="zh-TW")
        return text
    except:
        return '聽不懂'
    

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
        
def bot_get_google(question):
    url=f'https://www.google.com/search?q={question}+維基百科'
    # 以下是要在 get 的表頭加上瀏覽器的資訊, 以偽裝成瀏覽器
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                             ' AppleWebKit/537.36 (KHTML, like Gecko)'
                             ' Chrome/70.0.3538.102 Safari/537.36'}
    response=requests.get(url,headers=headers)
    if response.status_code == 200:
        bs=BeautifulSoup(response.text,"lxml")
        wiki_url=bs.find("cite")
        kwd=wiki_url.text.split("›")[-1].replace(' ','') #注意那個符號並不是大於
        keyword_trad=HanziConv.toTraditional(kwd)
        return keyword_trad
    else:
        print('請求失敗')
        

question=''
answer=''
QA={'你是誰':'我是尼尼','聽不懂':'請再說一次'}

question = bot_listen()
print(question)

if question in QA:
    answer=QA[question]
    bot_speak(answer,'zh-TW')
    print(answer)
else:
    keyword=bot_get_google(question)
    content=bot_get_wiki(keyword)
    if content != None:
        bot_speak_re(content)
    else:
        print('找不到')