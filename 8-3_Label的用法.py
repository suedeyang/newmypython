# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 19:45:29 2020

@author: YANGS
"""

import tkinter as tk

window=tk.Tk()
#window.geometry('640.480')
window.title('Youtube極速下載器')


lb=tk.Label(window,bg='red',fg='white',text='請輸入Youtube網址',font=('新細明體',20),padx=50,pady=80)
lb.pack()
window.mainloop()