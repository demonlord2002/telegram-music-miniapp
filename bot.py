import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from utils.db import Database
from utils.spotify_api import search_spotify_track

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_WEB_URL = os.getenv("BASE_WEB_URL")

db = Database()

bot = Client(
    "spotify-miniapp-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# -------------------------------
# /start
# -------------------------------
@bot.on_message(filters.command("start"))
async def start(_, message):
    await message.reply(
        "👋 Welcome to *Spotify Mini App Music Bot!*",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🎧 Open Music Room", url=f"{BASE_WEB_URL}/")]]
        )
    )

# -------------------------------
# /play
# -------------------------------
@bot.on_message(filters.command("play") & filters.group)
async def play_handler(_, message):
    query = " ".join(message.command[1:])
    if not query:
        return await message.reply("❗ Usage: /play song name")

    reply = await message.reply("🔎 Searching…")

    track = search_spotify_track(query)
    if not track:
        return await reply.edit("❌ No results found.")

    group_id = message.chat.id
    db.add_song(group_id, track)

    join_button = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🎧 Join Room", url=f"{BASE_WEB_URL}/room/{group_id}")]]
    )

    await reply.edit(
        f"♬ **Started Streaming**\n\n"
        f"⋆ **Title:** {track['title']}\n"
        f"⋆ **Duration:** {track['duration']}\n"
        f"⋆ **Requested by:** {message.from_user.first_name}",
        reply_markup=join_button
    )

# -------------------------------
# /settings
# -------------------------------
@bot.on_message(filters.command("settings") & filters.group)
async def settings(_, message):
    owner_status = (await bot.get_chat_member(message.chat.id, message.from_user.id)).status

    if owner_status not in ["administrator", "creator"]:
        return await message.reply("❗ Only admins can open settings.")

    settings = db.get_settings(message.chat.id)

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Everyone" if settings["allowed"] == "everyone" else "Admins",
                    callback_data=f"change_{settings['allowed']}"
                )
            ]
        ]
    )

    await message.reply("⚙️ *Who can use skip/pause/resume/end?*", reply_markup=keyboard)

# -------------------------------
# Start bot
# -------------------------------
print("Bot started!")
bot.run()  # Pyrogram v2 handles the loop internally
