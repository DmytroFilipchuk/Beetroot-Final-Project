import re

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

cid = 'c105a42529ce419aab0cb5188ecedd06'
secret = '98243799473f44be8e4680c46f1922e2'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def get_playlist_uri(playlist_link):

    if match := re.match(r"https://open.spotify.com/playlist/(.*)\?", playlist_link):
        playlist_uri = match.groups()[0]
    else:
        raise ValueError("Expected format: https://open.spotify.com/playlist/...")

    return playlist_uri

def call_playlist(playlist_id):
    # step1

    playlist_features_list = ["artist", "album", "track_name", "track_id", "danceability", "energy", "key", "loudness",
                              "mode", "speechiness", "instrumentalness", "liveness", "valence", "tempo", "duration_ms",
                              "time_signature"]

    playlist_df = pd.DataFrame(columns=playlist_features_list)

    # step2

    playlist = sp.user_playlist_tracks('spotify', get_playlist_uri(playlist_id)).get("items", [])
    for track in playlist:
        # Create empty dict
        playlist_features = {}
        # Get metadata
        playlist_features["artist"] = track["track"]["album"]["artists"][0]["name"]
        playlist_features["album"] = track["track"]["album"]["name"]
        playlist_features["track_name"] = track["track"]["name"]
        playlist_features["track_id"] = track["track"]["id"]

        # Get audio features
        audio_features = sp.audio_features(playlist_features["track_id"])[0]
        for feature in playlist_features_list[4:]:
            playlist_features[feature] = audio_features[feature]

        # Concat the dfs
        track_df = pd.DataFrame(playlist_features, index=[0])
        playlist_df = pd.concat([playlist_df, track_df], ignore_index=True)

    # Step 3

    return playlist_df


def get_songs(playlist_id, tempo):

    result = call_playlist(playlist_id)
    result = result.to_dict(orient='records')

    top_songs = {}

    for song in result:

        if int(tempo)-10 < int(song['tempo']) < int(tempo)+10:
            top_songs[song['artist']] = song['track_name']

    return top_songs






