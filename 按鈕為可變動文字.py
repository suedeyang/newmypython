# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:31:10 2020

@author: YANGS
"""

import tkinter as tk

def click_func():
    tkstr.set('被按了')

window=tk.Tk()
window.geometry('340x100')
window.title("12345")

tkstr=tk.StringVar() #字串變數 IntVar()整數變數 預設空 預設0  DoubleVar浮點變數 預設0.0
tkstr.set('請按我')

btn=tk.Button(window,textvariable=tkstr,font=('新細明體',20),command=click_func)
btn.pack()

window.mainloop()