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

5. pandas 
1-load and look
| Code | What it does |
|---|---|
| df.shape  | (rows, columns) |
| df.head() | First 5 rows    |