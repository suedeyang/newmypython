import requests
from bs4 import BeautifulSoup
from pytube import YouTube

def get_urls(url):
    urls=[]
    if '&list' not in url:
        return url #單一影片 直接download
    response=requests.get(url)
    if response.status_code != 200:
        print('請求失敗')
        return
    bs=BeautifulSoup(response.text,'lxml')
    a_list=bs.find_all('a')
    base="https://www.youtube.com"
    for a in a_list:
        href=a.get('href')
        url=base+href
        if "&index=" in url and url not in urls:
            urls.append(url)
    return urls

playlist_url='https://www.youtube.com/watch?v=pbEOv5FaZqo&list=PL_pux_5iXSsQIkCLpito-sg2Fbz4QBgIp'

urls=get_urls(playlist_url)
for url in urls:
    yt=YouTube(url)
    print(f"{yt.title}下載開始")
    yt.streams.first().download('d:/video')
    print(f'{yt.title}下載結束')