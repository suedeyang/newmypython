
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="利用st.session_state來進行線性控制",page_icon=":heart:")

st.markdown('[教學網站](https://blog.devgenius.io/streamlit-python-tips-how-to-avoid-your-app-from-rerunning-on-every-widget-click-cae99c5189eb)')

st.markdown(
    '''
    * 字典 也可以建立dataframe
    * 如果已經用pd整理過的dataframe可以直接用st.write 顯示出來(magic?)
    * plotly.express 繪圖
    * 階段一 如果不用button 改用checkbox widget 可以保留check的狀態 
    * 用st.session_state 來做線性控制保住button的狀態
    '''
)

# --- Initialising SessionState ---
if "load_state" not in st.session_state:
     st.session_state.load_state = False


st.header("Fruits List")
# ---- Creating Dictionary ----
_dic = { 'Name': ['Mango', 'Apple', 'Banana'],
         'Quantity': [45, 38, 90]}
#st.dataframe(_dic)
_df = pd.DataFrame(_dic)
st.write(_df)

#差異在這 st.button is an inactive state as the script reruns due to the radio button trigger.
#一次性的東西一經過rerun性質就消失了 改用checkbox才能保留active 狀態

#load = st.button('Load Data')
if st.button('Load Data') or st.session_state.load_state:
    st.session_state.load_state = True
    #_df=pd.DataFrame(_dic)
    opt = st.radio('Plot type :',['Bar', 'Pie'])

    if opt == 'Bar':
        fig = px.bar(_df, x= 'Name',y = 'Quantity',title ='Bar Chart')
        st.plotly_chart(fig)
    else:     
        fig = px.pie(_df,names = 'Name',values = 'Quantity',title ='Pie Chart')
        st.plotly_chart(fig)


'''
load =st.checkbox('Load Data')

if load:
    _df = pd.DataFrame(_dic)
    st.write(_df)
   
   # ---- Plot types -------
    opt = st.radio('Plot type :',['Bar', 'Pie'])
    if opt == 'Bar':
        fig = px.bar(_df, x= 'Name',y = 'Quantity',title ='Bar Chart')
        st.plotly_chart(fig)
    else:     
        fig = px.pie(_df,names = 'Name',values = 'Quantity',title ='Pie Chart')
        st.plotly_chart(fig)

'''