    import streamlit as st
    import pandas as pd
     
    st.write("""
    # My first app
    Hello *world!*
    """)
     
    df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/NBA_2020.csv')
    st.line_chart(df)
