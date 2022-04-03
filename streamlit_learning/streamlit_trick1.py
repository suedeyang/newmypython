

import streamlit as st
import pandas as pd
st.set_page_config(page_title="葉面標頭",page_icon=":gun:")

st.markdown("[教學影片](https://www.youtube.com/watch?v=0gT_Ro8ijII&t=732s)")

st.markdown(
    '''
    * 隱藏主選單與footer
    * 設定頁面標題與ICON
    * 橫向排列RADIO按鈕
    * 以dataframe呈現資料 並以副程式判斷數值後給予不同的顏色
    '''
)

hide_menu_style="""
    <style>
    #MainMenu {visibility:hidden;} #這個跟想的不一樣
    footer {visibility:hidden; }
    </style>
    """

st.markdown(hide_menu_style,unsafe_allow_html=True)

st.header("Cool Streamlit Tricks")
st.radio("Radio Button",['R1','R2','R3','R4'],key='radio_state')
st.subheader('橫向排列')
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


def color_df(val):
    if val > 21:
        color = 'yellow'
    else :
        color = 'red'
    return f'background-color: {color}'

st.subheader("簡單的data以dataframe呈現")
data = [['Tom', 23], ['Nick', 18], ['Bob', 20], ['Martin', 25]]
st.dataframe(data)

st.subheader("data加上欄位標題 Name and Age 再以dataframe呈現")
df = pd.DataFrame(data, columns = ['Name', 'Age'])
st.dataframe(df)

st.subheader("上方的dataframe 加上 style輔以副程式做顏色研判後乘現")
st.dataframe(df.style.applymap(color_df,subset=['Age']))