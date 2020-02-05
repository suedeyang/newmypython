# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:17:55 2020

@author: suedeyang
"""

from pytube import YouTube
url='https://www.youtube.com/watch?v=JwBXgJeqeOs'
yt=YouTube(url)
print(yt.streams.all()) #查看所有格式
yt.streams.get_by_itag('136').download('d:/video') #下載特定解析度