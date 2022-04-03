import time
import requests

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    print(r.json())
    return r.json()

spooky="https://assets9.lottiefiles.com/packages/lf20_t9gkkhz4.json"
lottie_url_hello = "https://assets5.lottiefiles.com/packages/lf20_V9t630.json"
lottie_url_download = "https://assets4.lottiefiles.com/private_files/lf30_t26law.json"
lottie_hello = load_lottieurl(spooky)
lottie_download = load_lottieurl(lottie_url_download)


st_lottie(lottie_hello, key="123")

if st.button("Download"):
    with st_lottie_spinner(lottie_download, key="download"):
        time.sleep(5)
    st.balloons()