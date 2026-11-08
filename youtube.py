import pandas as pd

history = pd.read_json("private/history.json")

#shape
print("Rows and columns: ", history.shape)

#column names
print("Column names is: ")
print(list(history.columns))

#first 5 row
print(history.head(5))

#Count number of songs on Youtube
print(history["header"].value_counts())

#most common channel
history["channel"] = history["subtitles"].str.get(0).str.get("name")
#print(history["channel"].value_counts().head(20))

#remove "Watched"
history["clean_title"] = history["title"].str.replace("Đã xem ", "")
#print(history["clean_title"].head(20))


#filtering music 
official = history[history["title"].str.contains("Official|Live|Concert|MV|M/V|Performance|Session|ft|EP|Music|Set|feat|Music Video|Audio|Lyrics|Visualizer|VEVO|Album|Original|Cover|Remix|Playlist", case = False)]
print(official["channel"].value_counts().head(20))
print(official["clean_title"].value_counts().head(20))
#print((official["channel"] == "Huace Croton TV Vietnam").sum()) #check leak in

#not music
not_official = history[~history["title"].str.contains("Official|Music Video|Audio|Lyrics|Visualizer|VEVO|Album|Original|Cover|Remix|Playlist", case=False)]
vu_missed = not_official[not_official["channel"] == "Vũ Official"]
#print(vu_missed["title"].value_counts().head(30))




