import streamlit as st
import streamlit.components.v1 as components
import random
from PIL import Image
#image=Image.open('world_flags.gif')

chosen=['chinese','japan','english','franch']
def lottery():
    n=random.randint(0,3)
    return n
N=lottery()
st.write("你選到的的是",chosen[N])
