import os
from dotenv import load_dotenv
import lyricsgenius

load_dotenv()
token = os.getenv("GENIUS_KEY")

genius = lyricsgenius.Genius(token)

print("Cautare artist \"Depeche mode\"")
dm = genius.search_artist("Depeche mode",max_songs=10)
print(f"Rezultat:\n{dm.songs}")