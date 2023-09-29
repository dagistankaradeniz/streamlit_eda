import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")
     
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stock_price.csv')
st.line_chart(df["Close"])
