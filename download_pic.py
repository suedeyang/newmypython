# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:15:35 2020

@author: YANGS
"""

import requests
from bs4 import BeautifulSoup
import os
import threading

'''
多執行緒的部分未完成 直接跳過
def get_photothread(folder_name,photo_name,photo_list):
    download_num=len(photo_list)
    Q=int(download_num/100)
    R=download_num % 100
    
    for i in range(Q):
        threads=[]
        for j in range(100):
            threads.append(threading.THread(target=download_pic,args=(photo_list[i*100+j],folder_name+os.sep+photo_name+os.sep+str(i*100+j+1)))
            threads[j].start()               
        for j in threads:
            j.join()
        print(int((i+1)*100/download_num*100),"%"
                           
'''                           


def create_folder(photo_name):
    folder_name=str(input("請輸入資料夾名稱:"))
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print("資料夾不存在 建立資料夾"+folder_name)
    else:
        print("找到資料夾"+folder_name)
    if not os.path.exists(folder_name+os.sep+photo_name):
        os.mkdir(folder_name+os.sep+photo_name) #os.sep 作業系統的路徑分隔資料 
        print('建立資料夾'+photo_name)
    else:
        print(photo_name+"已經存在")
    return folder_name
    
def download_pic(url,path):
    pic=requests.get(url)
    path += url[url.rfind("."):] #副檔名
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

folder_name=create_folder(photo_name)


for i in range(len(photo_list)) :
    download_pic(photo_list[i],folder_name+os.sep+photo_name+os.sep+str(i+1))

print("下載完畢!!")
    

        