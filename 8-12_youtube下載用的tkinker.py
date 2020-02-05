# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 22:26:41 2020

@author: suedeyang
"""


import tkinter as tk
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

def click_func():
    return
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