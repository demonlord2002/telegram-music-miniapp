import requests

def search_track(query):
    """
    Returns a dict:
    {
        "title": "",
        "artist": "",
        "duration": "",
        "thumbnail": "",
        "audio_url": ""
    }
    """

    url = f"https://itunes.apple.com/search?term={query}&limit=1"
    r = requests.get(url).json()

    if not r["resultCount"]:
        return None

    item = r["results"][0]

    return {
        "title": item.get("trackName", "Unknown"),
        "artist": item.get("artistName", "Unknown"),
        "duration": item.get("trackTimeMillis", 0) // 1000,
        "thumbnail": item.get("artworkUrl100"),
        "audio_url": item.get("previewUrl")  # 30 sec preview only (safe for Heroku)
    }
