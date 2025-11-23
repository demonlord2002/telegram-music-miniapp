import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

auth = SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
)

spotify = spotipy.Spotify(auth_manager=auth)


def ms_to_time(ms):
    seconds = int(ms / 1000)
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02d}:{seconds:02d}"


def search_spotify_track(query):
    results = spotify.search(q=query, type="track", limit=1)

    if not results["tracks"]["items"]:
        return None

    track = results["tracks"]["items"][0]

    return {
        "id": track["id"],
        "title": track["name"],
        "artists": ", ".join([a["name"] for a in track["artists"]]),
        "duration": ms_to_time(track["duration_ms"]),
        "thumbnail": track["album"]["images"][0]["url"],
        "preview_url": track["preview_url"],
    }
