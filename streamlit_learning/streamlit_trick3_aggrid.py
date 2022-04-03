#https://github.com/PablocFonseca/streamlit-aggrid


from argparse import ArgumentDefaultsHelpFormatter
import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')

st.dataframe(df)
st.write("---------------")
grid_return=AgGrid(df,width='100%',editable=True)
#https://streamlit-aggrid.readthedocs.io/en/docs/Usage.html Making Cells Editable
new_df = grid_return['data']
st.write(new_df)