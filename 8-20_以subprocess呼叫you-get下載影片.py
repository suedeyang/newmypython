# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 10:29:36 2020

@author: suedeyang
"""


import subprocess as sp

def yget_info(url): #回傳兩個參數 title與最佳品質
    process=sp.Popen('you-get -i '+url,  #i的後面要加上空格 語法才會正確
                     shell=True,
                     stdout=sp.PIPE,
                     stderr=sp.PIPE)
    r=process.communicate()
    s=str(r[0],'utf8') #轉換成utf8格式 
    #print(s)
    print('-------------------------------------')
    if s.find('title:')<0: #找不到title 失敗
        return '',''
    title=s[s.find('title:')+6:s.find("streams:")].strip()  #切出title 最後用strip去除空白
    itag=s[s.find('itag:')+6:s.find('container')].strip()
    if len(itag)>8:
        itag=itag[4:-3]
    return title,itag



def yget_dl(url,itag=None):
    cmd='you-get ' #語法的關係要加上空白
    if itag:
        cmd=cmd+'--itag='+ itag + ' '#語法的關係要加上空白
    process=subprocess.Popen(cmd+url)
    process.wait()
    return process.returncode
    


url='https://www.youtube.com/watch?v=lucsQi5iY0c'
title,best=yget_info(url)
print(title,best)

r=yget_dl(url,best)
print('下載高品質:','OK' if r == 0 else 'Error')

r=yget_dl(url)
print('下載一般品質','OK' if r == 0 else 'Error')
yget_dl(url,itag)