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