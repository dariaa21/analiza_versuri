import os
from dotenv import load_dotenv
import lyricsgenius
from functii import versuri, curatare_versuri

load_dotenv()
token = os.getenv("GENIUS_KEY")

genius = lyricsgenius.Genius(token)

print("Cautare artist \"Depeche mode\"")
dm = versuri("Depeche mode","Never let me down",genius)
print(f"Rezultat:\n{curatare_versuri(dm)}")