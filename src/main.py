import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from dotenv import load_dotenv
import os

def createjson(list, name):
    _list = json.dumps(list, indent=4)
    path = "./" + name + ".txt"
    f = open(path, "w")
    f.write(_list)
    f.close()

# AUTH HANDLING
scopes = ["playlist-read-private", "playlist-modify-private"]

load_dotenv()
_ClientID= os.getenv("SPOTIPY_CLIENT_ID")
_ClientSecret=os.getenv("SPOTIPY_CLIENT_SECRET")
_RedirectURI=os.getenv("RedirectURI")

auth_READ = SpotifyOAuth(scope=scopes[0], client_id=_ClientID, client_secret=_ClientSecret, redirect_uri=_RedirectURI)
auth_MODIFY = SpotifyOAuth(scope=scopes[1], client_id=_ClientID, client_secret=_ClientSecret, redirect_uri=_RedirectURI)

SP_READ = spotipy.Spotify(auth_manager=auth_READ)
SP_MODIFY = spotipy.Spotify(auth_manager=auth_MODIFY)


# READING PLAYLISTS
playlist_results = SP_READ.current_user_playlists()

playlists = []
all_tracks = []
includeprivate = False

for playlist in playlist_results['items']:
    if includeprivate:
        playlists.append(playlist['id'])
    elif(playlist["public"]):
        playlists.append(playlist['id'])

for playlist in playlists:
    track_results = SP_READ.playlist_tracks(playlist_id=playlist)
    for track in track_results['items']:
        all_tracks.append(track['track']['name'])

all_tracks = list(dict.fromkeys(all_tracks))

print(all_tracks)