import os
import logging
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputFile,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)
from utils.db import DB
from utils.spotify_api import search_track
from utils.helpers import download_audio, format_track

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

db = DB()
APP_URL = os.getenv("APP_URL")

# ------------------------------------------------------
#   /start
# ------------------------------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to the Music Room Bot!\n\n"
        "🎧 Use /play <song> to add music to your room.\n"
        "📟 Use /queue to view current queue.\n"
        "⚙️ Use /settings to configure room settings."
    )

# ------------------------------------------------------
#   /play <query>
# ------------------------------------------------------
async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    if not context.args:
        return await update.message.reply_text("❗ Usage: /play <song name>")

    query = " ".join(context.args)
    track = search_track(query)

    if not track:
        return await update.message.reply_text("❌ No results found.")

    db.add_to_queue(chat_id, track)

    join_button = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎧 Join Room", url=f"{APP_URL}/room?chat_id={chat_id}")]
    ])

    await update.message.reply_text(
        format_track(track, update.effective_user),
        reply_markup=join_button
    )

# ------------------------------------------------------
#   /queue
# ------------------------------------------------------
async def queue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    q = db.get_queue(chat_id)

    if not q:
        return await update.message.reply_text("📭 Queue is empty.")

    text = "🎶 **Current Queue:**\n\n"
    for i, t in enumerate(q, 1):
        text += f"{i}. {t['title']} — {t['artist']}\n"

    await update.message.reply_text(text)

# ------------------------------------------------------
#   /skip
# ------------------------------------------------------
async def skip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    if not db.can_skip(chat_id, update.effective_user.id):
        return await update.message.reply_text("❌ Only admins can skip.")

    db.skip_track(chat_id)
    await update.message.reply_text("⏭ Track skipped.")

# ------------------------------------------------------
#   /resume
# ------------------------------------------------------
async def resume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text("▶️ Resume feature placeholder")

# ------------------------------------------------------
#   /pause
# ------------------------------------------------------
async def pause(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text("⏸️ Pause feature placeholder")

# ------------------------------------------------------
#   /settings
# ------------------------------------------------------
async def settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    settings = db.get_settings(chat_id)

    kb = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                f"Everyone Skip: {'ON' if settings['everyone_skip'] else 'OFF'}",
                callback_data="toggle_skip"
            )
        ],
        [
            InlineKeyboardButton(
                f"Everyone End: {'ON' if settings['everyone_end'] else 'OFF'}",
                callback_data="toggle_end"
            )
        ]
    ])

    await update.message.reply_text("⚙️ Room Settings:", reply_markup=kb)

# ------------------------------------------------------
#   Callback Buttons
# ------------------------------------------------------
async def callback_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat.id

    if query.data == "toggle_skip":
        db.toggle_setting(chat_id, "everyone_skip")
        await query.edit_message_text("✔️ Updated settings.")
    elif query.data == "toggle_end":
        db.toggle_setting(chat_id, "everyone_end")
        await query.edit_message_text("✔️ Updated settings.")

# ------------------------------------------------------
#   /download (admin only) – optional
# ------------------------------------------------------
async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("❗ Usage: /download <yt-url>")

    url = context.args[0]
    file_path = download_audio(url)

    if file_path:
        await update.message.reply_audio(InputFile(file_path))
    else:
        await update.message.reply_text("❌ Failed to download audio.")

# ------------------------------------------------------
#   MAIN
# ------------------------------------------------------
def main():
    bot = ApplicationBuilder().token(os.getenv("TOKEN")).build()

    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(CommandHandler("play", play))
    bot.add_handler(CommandHandler("queue", queue))
    bot.add_handler(CommandHandler("skip", skip))
    bot.add_handler(CommandHandler("pause", pause))
    bot.add_handler(CommandHandler("resume", resume))
    bot.add_handler(CommandHandler("settings", settings))
    bot.add_handler(CommandHandler("download", download))

    bot.add_handler(CallbackQueryHandler(callback_button))

    bot.run_polling()

if __name__ == "__main__":
    main()
