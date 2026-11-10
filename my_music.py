import streamlit as st
import pandas as pd

st.title("My Youtube Wrapped")

history = pd.read_json("private/history.json")

#most common channel
history["channel"] = history["subtitles"].str.get(0).str.get("name")


#remove "Watched"
history["clean_title"] = history["title"].str.replace("Đã xem ", "")


#filtering music 
official = history[history["title"].str.contains("Official|Live|Concert|MV|M/V|Performance|Session|ft|EP|Music|Set|feat|Music Video|Audio|Lyrics|Visualizer|VEVO|Album|Original|Cover|Remix|Playlist", case = False)]


#time limit
official["time"] = pd.to_datetime(official["time"], format="ISO8601")
official["time_month"] = official["time"].dt.to_period("M")


#highest month
counts = official["time_month"].value_counts()

#improve ux
col1, col2 = st.columns(2)
col1.metric("Top month", str(counts.idxmax()))
col2.metric("Amount of times", str(counts.max()))