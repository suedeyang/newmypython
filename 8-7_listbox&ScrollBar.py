# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 20:58:42 2020

@author: YANGS
"""

import tkinter as tk
window=tk.Tk()

listbox=tk.Listbox(window)
print(f'資料比數:{listbox.size()}')
for row in range(30):
    listbox.insert(row,f'第{row}筆資料')
print(f'資料筆數{listbox.size()}')

listbox.pack(side=tk.LEFT)

#ScrollBar捲動軸
sbar=tk.Scrollbar(window)
sbar.pack(side=tk.RIGHT,fill=tk.Y)

#列示框與捲動軸的連結
sbar.config(command=listbox.yview)
listbox.config(yscrollcommand=sbar.set)

window.mainloop()