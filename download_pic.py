# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:15:35 2020

@author: YANGS
"""

import requests
from bs4 import BeautifulSoup
import os
import threading

#url="https://i.ytimg.com/vi/MPV2METPeJU/maxresdefault.jpg"
#path="doanload"
#def download_pic(url,path):
#    pic=requests.get(url)
#    path = path+"."+url[url.rfind('.'):] #副檔名
#    f=open(path,'wb')
#    f.write(pic.content)
#    f.close()
    
def download_pic(url,path):
    pic=requests.get(url)
    path += url[url.rfind("."):]
    f=open(path,'wb')
    f.write(pic.content)
    f.close()
    

def get_photolist(photo_name,download_num):
    page=1
    photo_list=[]
    
    while True:
        url='https://pixabay.com/zh/photos/'+ photo_name +'/?pagi='+str(page)
        #設定link
        html=requests.get(url)
        html.encoding='utf-8'
        bs=BeautifulSoup(html.text,'lxml')
        photo_item=bs.find_all('div',{'class':'item'})
        
        if len(photo_item)==0:
            return None
        for i in range(len(photo_item)):
            photo=photo_item[i].find('img')['src']
            
            if photo in photo_list:
                return photo_list
            if photo == '/static/img/blank.gif':
                photo=photo_item[i].find('img')['data-lazy']
                      
            photo_list.append(photo) 
            if len(photo_list) >= download_num:
                return photo_list
            #print(photo_list)
        page = page+1
        
while True:
    photo_name=input("請輸入你要下載的圖片名稱:")
    download_num=int(input("你要下載的相片數量"))
    photo_list=get_photolist(photo_name,download_num)
    
    if photo_list == None:
        print("找不到圖片，請換個關鍵字")
    else:
        if len(photo_list) <= download_num:
            print("僅找到"+str(len(photo_list))+"張相片")
        else:
            print("取得所有相片連結")
        break

for i in range(len(photo_list)) :
    download_pic(photo_list[i],str(i+1))

        