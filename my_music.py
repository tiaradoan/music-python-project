import streamlit as st
import pandas as pd

st.title("My Youtube Wrapped")

#add dropbox
st.header("Your Dropbox")
uploaded = st.file_uploader("Upload your music history", type="json")
if uploaded is None:
    st.write("Please upload a file first!")
    st.stop()


history = pd.read_json(uploaded)

#most common channel
history["channel"] = history["subtitles"].str.get(0).str.get("name")


#remove "Watched"
history["clean_title"] = history["title"].str.replace("Đã xem ", "")


#filtering music 
official = history[history["title"].str.contains("Official|Live|Concert|MV|M/V|Performance|Session|ft|EP|Music|Set|feat|Music Video|Audio|Lyrics|Visualizer|VEVO|Album|Original|Cover|Remix|Playlist", case = False)]


#time limit
official["time"] = pd.to_datetime(official["time"], format="ISO8601")
official["time_month"] = official["time"].dt.strftime("%Y-%m")


#highest month
counts = official["time_month"].value_counts()

#improve ux
col1, col2 = st.columns(2)
col1.metric("Top month", str(counts.idxmax()))
col2.metric("Amount of times", str(counts.max()))

#monthly chart
st.subheader("Plays per month")
st.bar_chart(counts.sort_index())


#top songs and top channels
left,right = st.columns(2)

top_songs = official["clean_title"].value_counts().head(10)
left.subheader("Top songs")
left.dataframe(top_songs)

top_channels = official["channel"].value_counts().head(10)
right.subheader("Top channels")
right.dataframe(top_channels)



