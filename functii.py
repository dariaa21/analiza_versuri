import re

def versuri(nume_artist, nume_cantec, genius):
    try:
        cantec = genius.search_song(nume_cantec,nume_artist)
        if cantec:
            return cantec.lyrics
        else:
            return None
    except Exception as e:
        print(f"Eroare la cautarea piesei: {e}")
        return None

def curatare_versuri(versuri):
    if versuri is None:
        return ""
    text = re.sub(r'\[.*?\]','',versuri)
    text = re.sub(r'\n{3,}','\n\n',text)
    return text.strip()
