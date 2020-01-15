# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:04:39 2020

@author: YANGS
"""

import tkinter as tk
window=tk.Tk()
window.geometry('640x480')
window.title('Youtube極速下載器')

#GUI元件視窗區塊Frame
input_fm=tk.Frame(window,bg='red',width=640,height=120)
input_fm.pack() #pack是一種排版方式

#LABEL標籤
lb=tk.Label(input_fm,bg='red',fg='white',text='請輸入網址',font=('新細明體',30),pady=80,padx=50)
lb.pack()

#btn=tk.Button(window,text="YES")
#btn.pack()




window.mainloop()