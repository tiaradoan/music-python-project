import pandas as pd

# read the CSV file into a table (a "DataFrame")
df = pd.read_csv("data/dataset.csv")

print("Rows and columns:", df.shape)
print()
print("Column names:")
print(list(df.columns))
print()
print("First 5 rows:")
print(df.head()) 

#remove column
df = df.drop(columns= ["Unnamed: 0"])
print(df["track_genre"].value_counts())
print(df.isna().sum())

#remove row
df = df.dropna()
print (df.shape)
print (df.duplicated().sum())
print (df.duplicated(subset=["track_id"]).sum())
df = df.drop_duplicates()
print (df.shape)
print (df.duplicated(subset=["track_id"]).sum())

#grouping
avg_popularity = df.groupby("track_genre")["popularity"].mean()
avg_popularity = avg_popularity.sort_values(ascending=False)
avg_popularity = avg_popularity.round(2)
print(avg_popularity.head(10))
print(avg_popularity.tail(5))

#fastest genre by tempo
avg_tempo = df.groupby("track_genre")["tempo"].mean()
avg_tempo = avg_tempo.sort_values(ascending=False)
avg_tempo = avg_tempo.round(1)
print(avg_tempo.head(10))

#count song
songs = df.drop_duplicates(subset=["track_id"])
print(songs.shape)
print(songs["artists"].value_counts().head(10))

#compare audio features between genres
avg_types = df.groupby("track_genre")[["danceability", "energy", "valence"]].mean()
avg_types = avg_types.sort_values(by="valence", ascending=False)
avg_types = avg_types.round(2)
print(avg_types.loc[["sad", "happy", "chill"]])
print(avg_types.head(5))




