# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:40:36 2020

@author: YANGS
"""

import tkinter as tk
from tkinter import messagebox

def hello():
    messagebox.askyesno("提問對話框",'你好嗎?')
    
window=tk.Tk()
btn=tk.Button(window,text='按鈕',command=hello)
btn.pack()

window.mainloop()