import streamlit as st
import pandas as pd

# ===== MAP =====
# TABLES (variables that hold a whole table)
#   history    = every video you watched, straight from the uploaded file
#   official   = only the music rows (keyword filter + block list + time range)
#   song_plays = only the plays of the one song picked in "Song history"
#
# COLUMNS (inside history / official)
#   title       = raw video title, e.g. "Đã xem .... (Official MV)" (used for FILTERING)
#   clean_title = tidy title for SHOWING, e.g. "Soobin - Vụt Tan"
#   channel     = the YouTube channel that posted the video
#   time        = exact date + time of the play
#   time_month  = just the month, e.g. "2023-03"
#   top_year    = just the year, e.g. "2025"
#
# OTHER VARIABLES
#   uploaded     = the file the visitor uploaded
#   time_range   = what's picked in the time dropdown, e.g. "Last month"
#   latest       = date of the newest play (we count back from this)
#   counts       = plays per month (for "Plays per month" + top month cards)
#   counts_year  = plays per year (for the "Top year" card)
#   top_songs    = top 20 songs with their play counts
#   top_channels = top 20 channels with their play counts
#   song_history = the song picked in the "Pick a song" dropdown
#   song_counts  = plays per month of that one song (for its chart)

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
**No email? Go to [takeout.google.com/manage](https://takeout.google.com/manage)**
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
official = official[~official["title"].str.contains("Episode|Vlog|Reaction|Tập|Review|Trailer|Livestream", case=False)]

#filter official name
official["clean_title"]= official["clean_title"].str.replace(r"\(.*?\)|\[.*?\]", "", regex=True).str.strip()
official["clean_title"] = official["clean_title"].str.replace(r"[|/] *Official.*", "", regex=True, case=False).str.strip()


#time limit
official["time"] = pd.to_datetime(official["time"], format="ISO8601")
official["time_month"] = official["time"].dt.strftime("%Y-%m")
official["top_year"] = official["time"].dt.strftime("%Y")

#time range option
time_range = st.selectbox("Pick a time range", ["All time", "Last month", "Last 3 months", "Last 6 months", "Last year"])

#time
all_music = official 
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
counts_year = official["top_year"].value_counts()

#improve ux
col1, col2, col3 = st.columns(3)
col1.metric("Top month", str(counts.idxmax()))
col2.metric("Top month plays", str(counts.max()))
col3.metric("Top year", str(counts_year.idxmax()))

#monthly chart
st.subheader("Plays per month")
st.bar_chart(counts.sort_index())


#top songs and top channels
left,right = st.columns(2)

top_songs = official["clean_title"].value_counts().head(20).rename_axis("Song").rename("Plays")
left.subheader("Top songs")
left.dataframe(top_songs)

top_channels = official["channel"].value_counts().head(20).rename_axis("Channel").rename("Plays")
right.subheader("Top channels")
right.dataframe(top_channels)

#song history
st.subheader("Song history")
song_history = st.selectbox("Pick a song", top_songs.index)
song_plays = official[official["clean_title"] == song_history]
song_counts = song_plays["time_month"].value_counts()
st.line_chart(song_counts.sort_index())






