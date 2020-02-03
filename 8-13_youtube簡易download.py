# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:17:55 2020

@author: suedeyang
"""

from pytube import YouTube
url='https://www.youtube.com/watch?v=JwBXgJeqeOs'
yt=YouTube(url)
print(f'開始下載影片{yt.title}')
yt.streams.first().download('D:/video')
print("下載完成")

