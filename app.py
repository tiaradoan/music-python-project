import streamlit as st
import pandas as pd

df = pd.read_csv("data/dataset.csv")

#remove column
df = df.drop(columns = ["Unnamed: 0"])

#remove row
df = df.dropna()

#remove duplicate
df = df.drop_duplicates()

st.title("Music Data")
st.write("Number of rows: ", df.shape[0])
st.dataframe(df)


