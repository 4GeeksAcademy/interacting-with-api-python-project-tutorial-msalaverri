import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()

#Insert the information to work with it
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

