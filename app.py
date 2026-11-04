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

#dropdown
genres = df["track_genre"].unique()
option = st.selectbox("Pick a genre: ", genres)
st.write("You picked: ", option)

#new table
genre_songs = df[df["track_genre"] == option]
genre_songs = genre_songs.sort_values(by="popularity", ascending = False)
st.dataframe(genre_songs.head(10))

#popularity overall
avg_popularity = df.groupby("track_genre")["popularity"].mean()
avg_popularity = avg_popularity.sort_values(ascending = False)
st.subheader("Top 10 most popular genres")
st.bar_chart(avg_popularity.head(10), sort = False)

#energy bar
energy_bar = st.slider("Energy Level", 0.0, 1.0, 0.8)
energy_level = df[df["energy"] >= energy_bar]
energy_level = energy_level.drop_duplicates(subset= ["track_id"])
st.write("This energy level or higher: ", energy_level.shape[0])
energy_level = energy_level.sort_values(by = "popularity", ascending = False)
st.write(energy_level.head(10))







