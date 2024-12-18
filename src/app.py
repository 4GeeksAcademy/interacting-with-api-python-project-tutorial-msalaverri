import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()

#Insert the info to work with it
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

breaking_benjamin_uri = 'spotify:artist:5BtHciL0e0zOP7prIHn3pP'
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


results = spotify.artist_top_tracks('5BtHciL0e0zOP7prIHn3pP')

#Create a function to convert milliseconds to minutes
def mil_convert(milliseconds):
   seconds, milliseconds = divmod(milliseconds, 1000)
   minutes, seconds = divmod(seconds, 60)
   return minutes, seconds

# Pull the information using 'track' with the most played songs of the artist, keep the name of the song, the popularity and the duration (in minutes).
for track in results['tracks']:
    milliseconds = track['duration_ms']
    minutes, seconds = mil_convert(milliseconds)
    print('track         : ' + track['name'])
    print('popularity    : ' + str(track['popularity']))
    print(f'duration      : {minutes}:{seconds:02d} minutes')
    print()

#Convert it to a DataFrame
track_list = []

for track in results['tracks']:
    track_info = {'name': track['name'], 'popularity': track['popularity'], 'duration_ms': track['duration_ms'], 'album_name': track['album']['name'], 'release_date': track['album']['release_date'], 'artist_name': track['artists'][0]['name']}
    track_list.append(track_info)

df = pd.DataFrame(track_list)

#Sort by popularity
df_sorted = df.sort_values(by='popularity', ascending=False)

#Show top 3 songs
top_3_songs = df_sorted.head(3)
print(top_3_songs)