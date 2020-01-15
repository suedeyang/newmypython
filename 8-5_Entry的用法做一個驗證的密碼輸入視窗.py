# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:54:50 2020

@author: YANGS
"""

import tkinter as tk


def check_pw():
    if pwvar.get()=='flag':  #注意get的用法
        msvar.set('密碼正確') #注意set的用法
    else:
        msvar.set('密碼錯誤')
    


window=tk.Tk()
lb=tk.Label(window,text='請輸入密碼')
lb.pack()

#Entry輸入欄位
pwvar=tk.StringVar()
entry=tk.Entry(window,width='15',textvariable=pwvar,show='*',justify='center')
entry.pack()

btn=tk.Button(window,text='驗證',command=check_pw)
btn.pack()

#label訊息視窗

msvar=tk.StringVar()
lb_msg=tk.Label(window,textvariable=msvar)
lb_msg.pack()




window.mainloop()