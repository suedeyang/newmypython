# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 22:21:15 2020

@author: suedeyang
"""
import tkinter as tk
from pytube import YouTube
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import threading

def click_func():
    url=yt_url.get()
    try:
        YouTube(url)
    except:
        messagebox.showerror('錯誤','pytube不支援影片或者網址錯誤')
        return
    
    urls= get_urls(url)
    
    if urls and messagebox.askyesno('確認方塊',f'總共找到{len(urls)}個影片，是否下載所有影片? 按否下載單一影片'):
        print('開始下載影片')
        for u in urls:
            yt=YouTube(u)
            #print(f'開始下載{yt.title}')
            listbox.insert(tk.END,f'開始下載  {yt.title}')
            yt.streams.first().download('d:/video')
            listbox.insert(tk.END,f'下載完成  {yt.title}')
            #print(f'{yt.title}下載完成')
    else:
        yt=YouTube(url)
        if messagebox.askyesno('確認方塊',''f'是否下載{yt.title}?'):
            yt.streams.first().download('d:/video')
            listbox.insert(tk.END,f'下載完成  {yt.title}')
        else:
            print('取消下載')
            listbox.insert(tk.END,'取消下載')
    
def get_urls(url):
    urls=[]
    if "&list=" not in url: 
        return urls
    
    response=requests.get(url)
    if response.status_code != 200:
        print('請求失敗')
        return
    bs=BeautifulSoup(response.text,'lxml')
    a_list=bs.find_all('a')
    base='https://www.youtube.com/'
    for a in a_list:
        href=a.get('href')
        url=base+href
        if '&index=' in url and url not in urls:
            urls.append(url)
    return urls
    




window=tk.Tk()
window.geometry('640x480')
window.title('Youtube下載器')

input_fm=tk.Frame(window,bg='red',width=640,height=120)
input_fm.pack()

lb=tk.Label(input_fm,text='請輸入Youtube網址',bg='red',fg='white')
lb.place(rely=0.25,relx=0.5,anchor='center')

yt_url=tk.StringVar()
entry=tk.Entry(input_fm,textvariable=yt_url,width=50)
entry.place(rely=0.5,relx=0.5,anchor='center')


btn=tk.Button(input_fm,text='下載影片',command=click_func)
btn.place(rely=0.5,relx='0.85',anchor='center')


dload_fm=tk.Frame(window,width=640,height=480-120)
dload_fm.pack()

lb=tk.Label(dload_fm,text='下載狀態')
lb.place(rely=0.1,relx=0.5,anchor='center')

listbox=tk.Listbox(dload_fm,width=65,height=15)
listbox.place(rely=0.5,relx=0.5,anchor='center')

sbar=tk.Scrollbar(dload_fm)
sbar.place(rely=0.5,relx=0.87,anchor='center',relheight=0.7) #重點在relheight

listbox.config(yscrollcommand=sbar.set)
sbar.config(command=listbox.yview)    

window.mainloop()

