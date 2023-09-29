import pandas as pd
import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

st.write("""
# **EDA** using *Pandas Profiling* and *Streamlit*
This is just a sample Hello world kind of app to practice on AutoML and publishing easily (near real time)
""")
     
# df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stock_price.csv')
# st.line_chart(df, x="Date", y="Close")

df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()

st_profile_report(pr)
