import requests
import time

def sec_to_min(sec):
    m = sec // 60
    s = sec % 60
    return f"{m:02d}:{s:02d}"

def format_track(track, user):
    """
    Nicely formatted message for Telegram
    """
    return (
        "♬ **Started Streaming**\n\n"
        f"⋆ **Title:** {track['title']}\n"
        f"⋆ **Artist:** {track['artist']}\n"
        f"⋆ **Duration:** {sec_to_min(track['duration'])}\n"
        f"⋆ **Requested by:** {user.first_name}"
    )

def download_audio(url):
    """
    Downloads preview audio to /tmp
    Heroku-safe (ephemeral filesystem)
    """
    try:
        file_path = f"/tmp/audio_{int(time.time())}.mp3"
        r = requests.get(url)

        with open(file_path, "wb") as f:
            f.write(r.content)

        return file_path

    except Exception:
        return None
