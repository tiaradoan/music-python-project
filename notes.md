1. What is venv for? = show up
-> venv is a toolbox for a project
-> when ran "pip install pandas streamlit" => went into toolbox only, not whole computer

2. Why does .gitignore list venv?
-> git saves everything in folder unless tell it not to
-> venv is huge + anyone can rebuild by running "pip install" => tell Git to skip

3. git commit vs git push?
-> commit = saving your game on your own computer (snapshot that can go back to)
-> push = uploading that save the cloud (GitHub) => backed up and others can see
=> commit any times but only need to push once

4. Git
1) git add <files> : choose which files go into next snapshot
Ex) git add requirements.txt notes.md (name separated by spaces)
2) git add . : add all changed files (. means eevrything in this folder)
3) git commit -m "message": takes snapshot (-m means message, "text in quotes" describes what you changed such as "Add requirements and notes")
4) git push: uploads all commits to GitHub

## 5. pandas

### Load and look

| Code | What it does |
|---|---|
| `import pandas as pd` | Loads pandas with the nickname `pd` |
| `df = pd.read_csv("data/dataset.csv")` | Reads the CSV file into a table called `df` |
| `df.shape` | (rows, columns) |
| `df.columns` | All column names |
| `df.head()` / `df.head(10)` | First 5 / first 10 rows |
| `df.tail(5)` | Last 5 rows |
| `df["track_genre"]` | Picks one column |
| `df["track_genre"].unique()` | Each different value in a column, listed once |
| `df["track_genre"].value_counts()` | Each value plus how many times it appears |

### Clean

| Code | What it does |
|---|---|
| `df = df.drop(columns=["Unnamed: 0"])` | Removes a column |
| `df.isna().sum()` | Counts missing values in each column |
| `df = df.dropna()` | Removes rows with missing values |
| `df.duplicated().sum()` | Counts rows that are exact copies |
| `df.duplicated(subset=["track_id"]).sum()` | Counts rows whose `track_id` repeats |
| `df = df.drop_duplicates()` | Removes exact copy rows |
| `songs = df.drop_duplicates(subset=["track_id"])` | Keeps one row per song, saved as a new table `songs` |

Remember: `df = ...` saves the change. Without it, nothing changes.

### Analyse

| Code | What it does |
|---|---|
| `df.groupby("A")["B"].mean()` | Average of B for each A |
| `df.groupby("A")[["B", "C", "D"]].mean()` | Averages of several columns for each A |
| `.sort_values(ascending=False)` | Sorts big → small (`True` = small → big) |
| `.sort_values(by="valence", ascending=False)` | Sorts a table by one chosen column |
| `.round(2)` | Keeps 2 decimals |
| `.head(5)` after sorting | The top 5 |
| `.loc[["sad", "happy", "chill"]]` | Picks rows by their names |
| `songs["artists"].value_counts().head(10)` | The 10 most common artists |

How to read groupby: "average **B** per **A**". A = the groups, B = the numbers.

### () vs []

| Symbol | Meaning | Example |
|---|---|---|
| `()` | **Do** something (run a tool, settings go inside) | `.mean()`, `.round(2)`, `.head(5)` |
| `[]` | **Pick** something (a column or row) | `df["energy"]` |
| `[ , ]` | A **list** of several things | `["sad", "happy", "chill"]` |
| `[[ , ]]` | **Pick** using a **list** (several at once) | `df[["energy", "valence"]]` |

You can only use names that already exist in the data. Check them with `df.columns` (column names) or `.unique()` (values in a column).