# Creating something that makes a spotify playlist
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import json
import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

# search_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
search_date = "2020-01-01"
year = search_date[:4]

def get_artist(item):
    song_tag = item.h3
    song_title = (song_tag.text).strip()
    parent_tag = song_tag.parent
    artist = (parent_tag.span.text).strip()
    return (artist,song_title)

def get_songs():
    with urlopen((f"https://www.billboard.com/charts/hot-100/{search_date}")) as response:
        soup = bs(response, 'html.parser')
        
        with open("Day 46/top_100.json","w") as file:
            to_dump = {
                i:{
                    "Artist":get_artist(item)[0],
                    "Song":get_artist(item)[1]
                } 
                for i,item in enumerate(
                    soup.find_all(
                        class_="o-chart-results-list-row-container"
                    )
                )
            }
            
            json.dump(to_dump,file,indent=4)
            
file = open('Day 46/top_100.json')
data = json.load(file)

link_start="https://api.spotify.com/v1/search/"

sp = Spotify(auth_manager=SpotifyClientCredentials(client_id="b77e2e8563ed43a5b8fa3a4a05e83630",client_secret="afec32bf25404bd38592a938bc5ec3f2"))

song_ids = []
for i in data:
    artist = data[i]['Artist']
    song = data[i]['Song']
    query = f"track:{song} artist:{artist}"
    a = sp.search(q=query,type="track",market="US",limit=1)
    try:
        song_ids.append(a["tracks"]["items"][0]["id"])
    except :
        song_ids.append("skipped")
    
with open("Day 46/top_100.txt", "a") as file:
    file.writelines('\n'.join(song_ids) + '\n')
