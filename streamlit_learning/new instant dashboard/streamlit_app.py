import streamlit as st
import pandas as pd
import numpy as np
import plost
from PIL import Image

# Page setting
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Row A
a1, a2, a3 = st.columns(3)
#a1.image(Image.open('streamlit-logo-secondary-colormark-darktext.png'))
a2.metric("Wind", "9 mph", "-8%")
a3.metric("Humidity", "86%", "4%")

# Row B
b1, b2, b3, b4 = st.columns(4)
b1.metric("Temperature", "70 °F", "1.2 °F")
b2.metric("Wind", "9 mph", "-8%")
b3.metric("Humidity", "86%", "4%")
b4.metric("Humidity", "86%", "4%")

#抓取網站資料
url='https://covid-19.nchc.org.tw/city_confirmed.php?mycity=%E9%AB%98%E9%9B%84%E5%B8%82'