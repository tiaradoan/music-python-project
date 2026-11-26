import random
from datetime import datetime, timedelta
import json

songs = [
    ("Watched Coldplay - Yellow (Official Video)", "Coldplay"),
    ("Watched Eva Cooper - Moral of the Story (Official Audio)", "Eva Cooper - Topic"),
    ("Watched Taylor Swift - Champagne problems (Official Lyric Video)", "Taylor Swift"),
    ("Watched Harry Styles - As It Was (Official Video)", "Harry Styles"),
    ("Watched Ed Sheeran - Bad Habits (Official Video)", "Ed Sheeran"),
    ("Watched Ed Sheeran - Shivers (Official Video)", "Ed Sheeran"),
    ("Watched Justin Bieber - Ghost (Official Video)", "Justin Bieber"),
    ("Watched Adele - Easy On Me (Official Video)", "Adele"),
    ("Watched The Kid LAROI - Stay (with Justin Bieber) [Official Music Video]", "The Kid LAROI"),
    ("Watched Dua Lipa - Levitating (Official Music Video) ft. DaBaby", "Dua Lipa"),
]

#repeat
start = datetime(2024, 12, 1)
plays = []
for i in range(600):
    title, channel = random.choice(songs)
    days = random.randint(0, 729)
    minutes = random.randint(0, 1439)
    time = start + timedelta(days=days, minutes = minutes)
    plays.append({"title": title, "subtitles": [{"name": channel}], "time": time.isoformat() + "Z", })
with open("data/demo_history.json", "w") as f:
        json.dump(plays, f, indent=2)

