from pyrogram.enums import ChatMemberStatus


def is_admin(member):
    return member.status in [
        ChatMemberStatus.OWNER,
        ChatMemberStatus.ADMINISTRATOR
    ]


def format_track(track):
    return (
        f"♬ **Started Streaming**\n\n"
        f"⋆ **Title:** {track['title']}\n"
        f"⋆ **Duration:** {track['duration']}\n"
        f"⋆ **Artists:** {track['artists']}\n"
    )
