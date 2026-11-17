import streamlit as st
import pandas as pd

st.title("My Youtube Wrapped")

#add dropbox
st.header("Music History")
st.caption("🔒 Your file is only used to build this page and is never saved or shared!")

#guideline
with st.expander("How to take your history file from Google Takeout"):
    st.markdown(""" 
1. Go to [takeout.google.com](https://takeout.google.com)
2. Click "Deselect all", then scroll all the way down and tick only **YouTube and YouTube Music** (Do not click **next step** yet!)
3. In "All YouTube data included", keep only **history** 
4. In "Multiple formats", scroll down to "diary" and change HTML to **JSON** -> Click OK
5. In "Includes all data on YouTube", click "Deselected all" then click "history" only -> Click OK
6. Time for "Next Step"!
7. In "Destination", choose "send the download link via email" and **.zip** file
8. Google emails a zip (can take minutes to days! please be patient and remember to come back here 😋)
9. Unzip it and upload watch-history.json here
                
""")
    

uploaded = st.file_uploader("Upload your music history", type="json")

if uploaded is None:
    st.write("Please upload a file first!")
    st.stop()


history = pd.read_json(uploaded)

#most common channel
history["channel"] = history["subtitles"].str.get(0).str.get("name")


#remove "Watched"
history["clean_title"] = history["title"].str.replace(r"Đã xem |Watched |Vous avez regardé |Pinanood ang | adlı videoyu izlediniz|を視聴しました|观看了 |觀看 |을\(를\) 시청했습니다", "", regex=True).str.strip()


#filtering music 
official = history[history["title"].str.contains("Official|Live|Concert|MV|M/V|Performance|Session|ft|EP|Music|Set|feat|Music Video|Audio|Lyrics|Visualizer|VEVO|Album|Original|Cover|Remix|Playlist", case = False)]


#time limit
official["time"] = pd.to_datetime(official["time"], format="ISO8601")
official["time_month"] = official["time"].dt.strftime("%Y-%m")

#time range option
time_range = st.selectbox("Pick a time range", ["All time", "Last month", "Last 3 months", "Last 6 months", "Last year"])

#time
latest = official["time"].max()
if time_range == "Last month":
    start = latest - pd.DateOffset(months=1)
    official = official[official["time"] >= start]
elif time_range == "Last 3 months":
    start = latest - pd.DateOffset(months=3)
    official = official[official["time"]>=start]
elif time_range == "Last 6 months":
    start = latest - pd.DateOffset(months=6)
    official = official[official["time"]>=start]
elif time_range == "Last year":
    start = latest - pd.DateOffset(months=12)
    official = official[official["time"]>=start]






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






