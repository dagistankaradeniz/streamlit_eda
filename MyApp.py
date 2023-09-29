import pandas as pd
import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport


df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/iris.csv")
profile = ProfileReport(df,
                        title="Iris flower data set",
        dataset={
        "description": "This EDA report was generated by Pandas Profiling",
        "copyright_holder": "Dagistan",
        "copyright_year": "2023",
        "url": "https://dagistankaradeniz.github.io/",
    },
    variables={
        "descriptions": {
            "Sepal.Length": "Sepal.Length independent variable",
            "Sepal.Width": "Sepal.Width independent variable",
            "Petal.Length": "Petal.Length independent variable",
            "Petal.Width": "Petal.Width independent variable",
            "Species": "Species. The label / dependent variable"
        }
    }
)

st.title("Pandas Profiling in Streamlit!")
st.write(df)
st_profile_report(profile)
