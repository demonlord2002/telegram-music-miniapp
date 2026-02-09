Let's discuss can you create this chat bot repository possible? More advanced buttons inlines and cute It feels friendly, playful, and intelligent — just like chatting with a smart companion ✨
Cute & fun neko-style responses and images
Anime-inspired interaction vibes

✨ Features
🤖 AI-Powered Conversations - Smart responses using advanced AI
🔄 Bot Cloning System - Clone and host multiple bots
🌍 Multi-Language Support - Supports multiple languages
📊 Statistics & Analytics - Track bot usage and performance
💬 Group & Private Chat - Works in both groups and private messages
🎭 Shayri Generator - Get random romantic shayris
📡 Broadcast System - Send messages to all users/groups
⚡ Fast & Reliable - Built with async/await for optimal performance
🛠️ Easy Deployment - Multiple deployment options

🎮 Bot Commands
👑 Admin Commands
/clone <token> - Clone a bot using token
/delallclone - Delete all cloned bots (Owner only)
/gcast <message> - Broadcast message to all chats
/stats - Get bot statistics
📱 User Commands
/start - Start the bot
/help - Show help menu
/ping - Check bot response time
/id - Get your user ID
/lang - Change bot language
/chatbot on/off - Enable/disable chatbot
/status - Check chatbot status
/shayri - Get random shayri
/repo - Get source code
🔧 Clone Management
/cloned - List all cloned bots
/delclone <token> - Delete specific cloned bot
/listchatbot - Get detailed bot list (Authorized users only)

ChatBot/
├── ShrutiCHATBOT/           # Main bot package
│   ├── mplugin/             # Plugin modules
│   ├── helpers/             # Helper functions
│   └── database/            # Database operations
├── main.py                  # Bot entry point
├── config.py               # Configuration file
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── .env.example          # Environment template
└── README.md             # This file

Heroku supported and now tell me  can I create create the GitHub repository so can you give me a code please 🥺 
And important thing cloned bots this comment supported acpt /gcast <message> - Broadcast message to all chats when I put this comment my main bot all cloned bot bordcaste message sending anything links or message then cloned bot mentioned that bot bio cloned by @NelumiChatBot mentioned and also put out cloned bots description write like professional developer format 
And now can you give repoistry structure code please 🥺 correctly working on heroku please write a code professional developer 👇😭❤️ and don't mention Shruti mention Nelumi 
It's a Nelumi Chat Bot project and important thing add tamil and imporve thanglish because this bot starting stage adopt tamil peoplezz language this 2k gen suitable knowledge feed please 🥺 thanglish is very important this bot once Admin a group anazyle to thanglish how take the words return to reply or mention to Grup members enjoyed first thing this bot observe it skill improve because which grup this bot have that group suitable language chat better please improve that observed saved database it's helpful return talk and don't copy link or telegram group link it's spam 😭 you copy it memory or database again you give another group it's spam please 🥺 ignore that you tell don't do spam say 
And you add Grup stickers memory to reply Grup members just observed saved telegram sticker important thing don't save 18+ NSF content  and important all cloned bots observed memorys or database also grow helps please share the database observation memorys it's help bot individual development  and important use database Mongodb and telegram chennal it's helpful  and add app.jeson it's important deployed i have gemini pro it's helpful? I give u and add yours api key deepseek also please 🥺 it's helpful thanglish observed now please understand i describe all features i need clone the bot free it's users take clone it's free /clone <token> - Clone a bot using token this comment only free use all members 
Admins only do
/delallclone - Delete all cloned bots (Owner only)
/gcast <message> - Broadcast message to all chats
/stats - Get bot statistics
Don't miss anything 😭 

now i give chatbot repository i give you that old code can you update i want those things and features asked everything i want please 🥺 👇
RAUSHAN/database/__init__.py
from pymongo import MongoClient

import config

vickdb = MongoClient(config.MONGO_URL)
vick = vickdb["VickDb"]["Vick"]


from .chats import *
from .users import *

RAUSHAN/database/chats.py
from RAUSHAN import db

chatsdb = db.chatsdb


async def get_served_chats() -> list:
    chats = chatsdb.find({"chat_id": {"$lt": 0}})
    if not chats:
        return []
    chats_list = []
    for chat in await chats.to_list(length=1000000000):
        chats_list.append(chat)
    return chats_list


async def is_served_chat(chat_id: int) -> bool:
    chat = await chatsdb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def add_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if is_served:
        return
    return await chatsdb.insert_one({"chat_id": chat_id})


async def remove_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if not is_served:
        return
    return await chatsdb.delete_one({"chat_id": chat_id})

RAUSHAN/database/users.py
from RAUSHAN import db

usersdb = db.users


async def is_served_user(user_id: int) -> bool:
    user = await usersdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def get_served_users() -> list:
    users_list = []
    async for user in usersdb.find({"user_id": {"$gt": 0}}):
        users_list.append(user)
    return users_list


async def add_served_user(user_id: int):
    is_served = await is_served_user(user_id)
    if is_served:
        return
    return await usersdb.insert_one({"user_id": user_id})

RAUSHAN/modules/helpers/__init__.py
from typing import Callable

from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message

from RAUSHAN import OWNER, AMBOT


def is_admins(func: Callable) -> Callable:
    async def non_admin(c: AMBOT, m: Message):
        if m.from_user.id == OWNER:
            return await func(c, m)

        admin = await c.get_chat_member(m.chat.id, m.from_user.id)
        if admin.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await func(c, m)

    return non_admin


from .inline import *
from .read import *

RAUSHAN/modules/helpers/inline.py
from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from RAUSHAN import BOT_USERNAME, OWNER

DEV_OP = [
    [
        InlineKeyboardButton(
            text=" ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ᴏᴡɴᴇʀ", user_id=OWNER),
        InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴍᴅs", callback_data="HELP"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="ᴄʟᴏsᴇ",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="◁", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="ᴄʜᴀᴛʙᴏᴛ", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="ᴛᴏᴏʟs", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="◁", callback_data="BACK"),
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data=f"addchat"),
        InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data=f"rmchat"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="sᴏᴏɴ..", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="◁", callback_data="SBACK"),
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="◁", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ", callback_data="HELP"),
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="ʜᴇʟᴘ", url=f"https://t.me/{BOT_USERNAME}?start=help"
        ),
        InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="ʜᴇʟᴘ", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="ᴏᴡɴᴇʀ", user_id=OWNER),
        InlineKeyboardButton(text="sᴏᴜʀᴄᴇ", callback_data="SOURCE"),
    ],
    [
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/{UPDATE_CHNL}"),
        InlineKeyboardButton(text="◁", callback_data="BACK"),
    ],
]
RAUSHAN/modules/helpers/read.py
from config import OWNER_USERNAME, SUPPORT_GRP
from RAUSHAN import BOT_NAME, BOT_USERNAME

START = f"""
**╭───────────────────⦿**\n**│❍ ʜᴇʏ ɪ ᴀᴍ {BOT_NAME} •**\n**├───────────────────⦿**\n**│❍ ɪ ʀᴇᴀᴅ ʏᴏᴜʀ ᴍɪɴᴅ •**\n**│❍ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ •**\n**├───────────────────⦿**\n**│❍ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs •**\n**│❍ ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ •**\n**│❍ ғᴏʀ ᴀᴄᴛɪᴠᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ •**\n**│❍ ᴜsᴀɢᴇ /chatbot [ᴏɴ/ᴏғғ] •**\n**│❍ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ •**\n**│❍ 24x7 ᴛɪᴍᴇ ᴏɴʟɪɴᴇ •**\n**├───────────────────⦿**\n**│❍ ᴍᴀᴅᴇ ʙʏ...[˹ 𝐑𝐄𝐃 - 𝐋𝐈𝐍𝐄 ™ ˼](https://t.me/+QuuoMVb6zys0MDA1)♡**\n**╰───────────────────⦿
"""

HELP_READ = f"""
<u>**ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ {BOT_NAME}**</u>
**ᴀʀᴇ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ!**
**ᴀʟʟ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ:/**
**──────────────**
<b>๏ ᴏᴡɴᴇʀ @{OWNER_USERNAME}</b>
"""

TOOLS_DATA_READ = f"""
<u>**ᴛᴏᴏʟs ғᴏʀ {BOT_NAME} ᴀʀᴇ:**</u>
**➻ ᴜsᴇ /ping ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴛʜᴇ ᴘɪɴɢ ᴏғ {BOT_NAME}**
**──────────────**
**➻ ᴜsᴇ /id ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴜsᴇʀ ɪᴅ, ᴄʜᴀᴛ ɪᴅ ᴀɴᴅ ᴍᴇssᴀɢᴇ ɪᴅ ᴀʟʟ ɪɴ ᴀ sɪɴɢʟᴇ ᴍᴇssᴀɢᴇ.**
**───────────────**
<b>๏ ᴏᴡɴᴇʀ @{OWNER_USERNAME}</b>
"""

CHATBOT_READ = f"""
<u>*ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ {BOT_NAME}**</u>
**➻ ᴜsᴇ /chatbot ᴛᴏ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ.**
**๏ ɴᴏᴛᴇ ➻ ᴛʜᴇ ᴀʙᴏᴠᴇ ᴄᴏᴍᴍᴀɴᴅ ғᴏʀ ᴄʜᴀᴛʙᴏᴛ ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ!!**
**───────────────**
<b>๏ ᴏᴡɴᴇʀ @{OWNER_USERNAME}</b>
"""

SOURCE_READ = f"**ʜᴇʏ, ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏғ [{BOT_NAME}](https://t.me/{BOT_USERNAME}). ɪs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.**\n**ᴘʟᴇᴀsᴇ ғᴏʀᴋ ᴛʜᴇ ʀᴇᴘᴏ & ɢɪᴠᴇ ᴛʜᴇ sᴛᴀʀ ✯**\n**──────────────────**\n**ʜᴇʀᴇ ɪs ᴛʜᴇ [sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ](https://github.com)**\n**──────────────────**\n**ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴀᴛ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/{SUPPORT_GRP}).\n\n<b>๏ ᴏᴡɴᴇʀ @{OWNER_USERNAME}</b>"

ADMIN_READ = f"sᴏᴏɴ"

ABOUT_READ = f"""
**➻ [{BOT_NAME}](https://t.me/{BOT_USERNAME}) ɪs ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛ-ʙᴏᴛ.**
**➻ [{BOT_NAME}](https://t.me/{BOT_USERNAME}) ʀᴇᴘʟɪᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴛᴏ ᴀ ᴜsᴇʀ.**
**➻ ʜᴇʟᴘs ʏᴏᴜ ɪɴ ᴀᴄᴛɪᴠᴀᴛɪɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘs.**
**➻ ᴡʀɪᴛᴛᴇɴ ɪɴ [ᴘʏᴛʜᴏɴ](https://www.python.org) ᴡɪᴛʜ [ᴍᴏɴɢᴏ-ᴅʙ](https://www.mongodb.com) ᴀs ᴀ ᴅᴀᴛᴀʙᴀsᴇ**
**───────────────**
**➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ [{BOT_NAME}](https://t.me/{BOT_USERNAME})**
"""
RAUSHAN/modules/__init__.py
import glob
from os.path import basename, dirname, isfile


async def all_modules():
    mod_paths = glob.glob(dirname(__file__) + "/*.py")

    all_modules = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]

    return sorted(all_modules)

RAUSHAN/modules/callback.py

# Don't remove This Line From Here. Tg: @ll_ALPHA_BABY_lll
# Github :-RAUSHAN


from pyrogram.enums import ChatMemberStatus as CMS
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup

from RAUSHAN import AMBOT
from RAUSHAN.database import vick
from RAUSHAN.modules.helpers import (
    ABOUT_BTN,
    ABOUT_READ,
    ADMIN_READ,
    BACK,
    CHATBOT_BACK,
    CHATBOT_READ,
    DEV_OP,
    HELP_BTN,
    HELP_READ,
    MUSIC_BACK_BTN,
    SOURCE_READ,
    START,
    TOOLS_DATA_READ,
)


@AMBOT.on_callback_query()
async def cb_handler(_, query: CallbackQuery):
    if query.data == "HELP":
        await query.message.edit_text(
            text=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
            disable_web_page_preview=True,
        )
    elif query.data == "CLOSE":
        await query.message.delete()
        await query.answer("ᴄʟᴏsᴇᴅ ᴍᴇɴᴜ!", show_alert=True)
    elif query.data == "BACK":
        await query.message.edit(
            text=START,
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
    elif query.data == "SOURCE":
        await query.message.edit(
            text=SOURCE_READ,
            reply_markup=InlineKeyboardMarkup(BACK),
            disable_web_page_preview=True,
        )
    elif query.data == "ABOUT":
        await query.message.edit(
            text=ABOUT_READ,
            reply_markup=InlineKeyboardMarkup(ABOUT_BTN),
            disable_web_page_preview=True,
        )
    elif query.data == "ADMINS":
        await query.message.edit(
            text=ADMIN_READ,
            reply_markup=InlineKeyboardMarkup(MUSIC_BACK_BTN),
        )
    elif query.data == "TOOLS_DATA":
        await query.message.edit(
            text=TOOLS_DATA_READ,
            reply_markup=InlineKeyboardMarkup(CHATBOT_BACK),
        )
    elif query.data == "BACK_HELP":
        await query.message.edit(
            text=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
    elif query.data == "CHATBOT_CMD":
        await query.message.edit(
            text=CHATBOT_READ,
            reply_markup=InlineKeyboardMarkup(CHATBOT_BACK),
        )
    elif query.data == "CHATBOT_BACK":
        await query.message.edit(
            text=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
    elif query.data == "addchat":
        user_id = query.from_user.id
        user_status = (await query.message.chat.get_member(user_id)).status
        if user_status not in [CMS.OWNER, CMS.ADMINISTRATOR]:
            return await query.answer(
                "ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴇᴠᴇɴ ᴀɴ ᴀᴅᴍɪɴ, ᴅᴏɴ'ᴛ ᴛʀʏ ᴛʜɪs ᴇxᴘʟᴏsɪᴠᴇ sʜɪᴛ!",
                show_alert=True,
            )
        else:
            is_vick = vick.find_one({"chat_id": query.message.chat.id})
            if not is_vick:
                await query.edit_message_text(f"**ᴄʜᴀᴛ-ʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.**")
            if is_vick:
                vick.delete_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(
                    f"**ᴄʜᴀᴛ-ʙᴏᴛ ᴇɴᴀʙʟᴇᴅ ʙʏ** {query.from_user.mention}."
                )
    elif query.data == "rmchat":
        user_id = query.from_user.id
        user_status = (await query.message.chat.get_member(user_id)).status
        if user_status not in [CMS.OWNER, CMS.ADMINISTRATOR]:
            await query.answer(
                "ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴇᴠᴇɴ ᴀɴ ᴀᴅᴍɪɴ, ᴅᴏɴ'ᴛ ᴛʀʏ ᴛʜɪs ᴇxᴘʟᴏsɪᴠᴇ sʜɪᴛ!",
                show_alert=True,
            )
            return
        else:
            is_vick = vick.find_one({"chat_id": query.message.chat.id})
            if not is_vick:
                vick.insert_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(
                    f"**ᴄʜᴀᴛ-ʙᴏᴛ ᴅɪsᴀʙʟᴇᴅ ʙʏ** {query.from_user.mention}."
                )
            if is_vick:
                await query.edit_message_text("**ᴄʜᴀᴛ-ʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ.**")

RAUSHAN/modules/chatbot.py
import random

from pymongo import MongoClient
from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from pyrogram.types import InlineKeyboardMarkup, Message

from config import MONGO_URL
from RAUSHAN import AMBOT
from RAUSHAN.modules.helpers import CHATBOT_ON, is_admins


@AMBOT.on_message(filters.command(["chatbot"]) & filters.group & ~filters.bot)
@is_admins
async def chaton_off(_, m: Message):
    await m.reply_text(
        f"ᴄʜᴀᴛ: {m.chat.id}\n**ᴄʜᴏᴏsᴇ ᴀɴ ᴏᴩᴛɪᴏɴ ᴛᴏ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ ᴄʜᴀᴛʙᴏᴛ.**",
        reply_markup=InlineKeyboardMarkup(CHATBOT_ON),
    )
    return


@AMBOT.on_message(
    (filters.text | filters.sticker | filters.group) & ~filters.private & ~filters.bot,
)
async def chatbot_text(client: Client, message: Message):
    try:
        if (
            message.text.startswith("!")
            or message.text.startswith("/")
            or message.text.startswith("?")
            or message.text.startswith("@")
            or message.text.startswith("#")
        ):
            return
    except Exception:
        pass
    chatdb = MongoClient(MONGO_URL)
    chatai = chatdb["Word"]["WordDb"]

    if not message.reply_to_message:
        vickdb = MongoClient(MONGO_URL)
        vick = vickdb["VickDb"]["Vick"]
        is_vick = vick.find_one({"chat_id": message.chat.id})
        if not is_vick:
            await client.send_chat_action(message.chat.id, ChatAction.TYPING)
            K = []
            is_chat = chatai.find({"word": message.text})
            k = chatai.find_one({"word": message.text})
            if k:
                for x in is_chat:
                    K.append(x["text"])
                hey = random.choice(K)
                is_text = chatai.find_one({"text": hey})
                Yo = is_text["check"]
                if Yo == "sticker":
                    await message.reply_sticker(f"{hey}")
                if not Yo == "sticker":
                    await message.reply_text(f"{hey}")

    if message.reply_to_message:
        vickdb = MongoClient(MONGO_URL)
        vick = vickdb["VickDb"]["Vick"]
        is_vick = vick.find_one({"chat_id": message.chat.id})
        if message.reply_to_message.from_user.id == client.id:
            if not is_vick:
                await client.send_chat_action(message.chat.id, ChatAction.TYPING)
                K = []
                is_chat = chatai.find({"word": message.text})
                k = chatai.find_one({"word": message.text})
                if k:
                    for x in is_chat:
                        K.append(x["text"])
                    hey = random.choice(K)
                    is_text = chatai.find_one({"text": hey})
                    Yo = is_text["check"]
                    if Yo == "sticker":
                        await message.reply_sticker(f"{hey}")
                    if not Yo == "sticker":
                        await message.reply_text(f"{hey}")
        if not message.reply_to_message.from_user.id == client.id:
            if message.sticker:
                is_chat = chatai.find_one(
                    {
                        "word": message.reply_to_message.text,
                        "id": message.sticker.file_unique_id,
                    }
                )
                if not is_chat:
                    chatai.insert_one(
                        {
                            "word": message.reply_to_message.text,
                            "text": message.sticker.file_id,
                            "check": "sticker",
                            "id": message.sticker.file_unique_id,
                        }
                    )
            if message.text:
                is_chat = chatai.find_one(
                    {"word": message.reply_to_message.text, "text": message.text}
                )
                if not is_chat:
                    chatai.insert_one(
                        {
                            "word": message.reply_to_message.text,
                            "text": message.text,
                            "check": "none",
                        }
                    )


@AMBOT.on_message(
    (filters.sticker | filters.group | filters.text) & ~filters.private & ~filters.bot,
)
async def chatbot_sticker(client: Client, message: Message):
    try:
        if (
            message.text.startswith("!")
            or message.text.startswith("/")
            or message.text.startswith("?")
            or message.text.startswith("@")
            or message.text.startswith("#")
        ):
            return
    except Exception:
        pass
    chatdb = MongoClient(MONGO_URL)
    chatai = chatdb["Word"]["WordDb"]

    if not message.reply_to_message:
        vickdb = MongoClient(MONGO_URL)
        vick = vickdb["VickDb"]["Vick"]
        is_vick = vick.find_one({"chat_id": message.chat.id})
        if not is_vick:
            await client.send_chat_action(message.chat.id, ChatAction.TYPING)
            K = []
            is_chat = chatai.find({"word": message.sticker.file_unique_id})
            k = chatai.find_one({"word": message.text})
            if k:
                for x in is_chat:
                    K.append(x["text"])
                hey = random.choice(K)
                is_text = chatai.find_one({"text": hey})
                Yo = is_text["check"]
                if Yo == "text":
                    await message.reply_text(f"{hey}")
                if not Yo == "text":
                    await message.reply_sticker(f"{hey}")

    if message.reply_to_message:
        vickdb = MongoClient(MONGO_URL)
        vick = vickdb["VickDb"]["Vick"]
        is_vick = vick.find_one({"chat_id": message.chat.id})
        if message.reply_to_message.from_user.id == Client.id:
            if not is_vick:
                await client.send_chat_action(message.chat.id, ChatAction.TYPING)
                K = []
                is_chat = chatai.find({"word": message.text})
                k = chatai.find_one({"word": message.text})
                if k:
                    for x in is_chat:
                        K.append(x["text"])
                    hey = random.choice(K)
                    is_text = chatai.find_one({"text": hey})
                    Yo = is_text["check"]
                    if Yo == "text":
                        await message.reply_text(f"{hey}")
                    if not Yo == "text":
                        await message.reply_sticker(f"{hey}")
        if not message.reply_to_message.from_user.id == Client.id:
            if message.text:
                is_chat = chatai.find_one(
                    {
                        "word": message.reply_to_message.sticker.file_unique_id,
                        "text": message.text,
                    }
                )
                if not is_chat:
                    toggle.insert_one(
                        {
                            "word": message.reply_to_message.sticker.file_unique_id,
                            "text": message.text,
                            "check": "text",
                        }
                    )
            if message.sticker:
                is_chat = chatai.find_one(
                    {
                        "word": message.reply_to_message.sticker.file_unique_id,
                        "text": message.sticker.file_id,
                    }
                )
                if not is_chat:
                    chatai.insert_one(
                        {
                            "word": message.reply_to_message.sticker.file_unique_id,
                            "text": message.sticker.file_id,
                            "check": "none",
                        }
                    )


@AMBOT.on_message(
    (filters.text | filters.sticker | filters.group) & ~filters.private & ~filters.bot,
)
async def chatbot_pvt(client: Client, message: Message):
    try:
        if (
            message.text.startswith("!")
            or message.text.startswith("/")
            or message.text.startswith("?")
            or message.text.startswith("@")
            or message.text.startswith("#")
        ):
            return
    except Exception:
        pass
    chatdb = MongoClient(MONGO_URL)
    chatai = chatdb["Word"]["WordDb"]
    if not message.reply_to_message:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)
        K = []
        is_chat = chatai.find({"word": message.text})
        for x in is_chat:
            K.append(x["text"])
        hey = random.choice(K)
        is_text = chatai.find_one({"text": hey})
        Yo = is_text["check"]
        if Yo == "sticker":
            await message.reply_sticker(f"{hey}")
        if not Yo == "sticker":
            await message.reply_text(f"{hey}")
    if message.reply_to_message:
        if message.reply_to_message.from_user.id == client.id:
            await client.send_chat_action(message.chat.id, ChatAction.TYPING)
            K = []
            is_chat = chatai.find({"word": message.text})
            for x in is_chat:
                K.append(x["text"])
            hey = random.choice(K)
            is_text = chatai.find_one({"text": hey})
            Yo = is_text["check"]
            if Yo == "sticker":
                await message.reply_sticker(f"{hey}")
            if not Yo == "sticker":
                await message.reply_text(f"{hey}")


@AMBOT.on_message(
    (filters.sticker | filters.sticker | filters.group)
    & ~filters.private
    & ~filters.bot,
)
async def chatbot_sticker_pvt(client: Client, message: Message):
    try:
        if (
            message.text.startswith("!")
            or message.text.startswith("/")
            or message.text.startswith("?")
            or message.text.startswith("@")
            or message.text.startswith("#")
        ):
            return
    except Exception:
        pass
    chatdb = MongoClient(MONGO_URL)
    chatai = chatdb["Word"]["WordDb"]
    if not message.reply_to_message:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)
        K = []
        is_chat = chatai.find({"word": message.sticker.file_unique_id})
        for x in is_chat:
            K.append(x["text"])
        hey = random.choice(K)
        is_text = chatai.find_one({"text": hey})
        Yo = is_text["check"]
        if Yo == "text":
            await message.reply_text(f"{hey}")
        if not Yo == "text":
            await message.reply_sticker(f"{hey}")
    if message.reply_to_message:
        if message.reply_to_message.from_user.id == client.id:
            await client.send_chat_action(message.chat.id, ChatAction.TYPING)
            K = []
            is_chat = chatai.find({"word": message.sticker.file_unique_id})
            for x in is_chat:
                K.append(x["text"])
            hey = random.choice(K)
            is_text = chatai.find_one({"text": hey})
            Yo = is_text["check"]
            if Yo == "text":
                await message.reply_text(f"{hey}")
            if not Yo == "text":
                await message.reply_sticker(f"{hey}")

RAUSHAN/modules/eval.py
import os
import re
import subprocess
import sys
import traceback
from inspect import getfullargspec
from io import StringIO
from time import time

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from RAUSHAN import OWNER, dev


async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {a}" for a in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)


async def edit_or_reply(msg: Message, **kwargs):
    func = msg.edit_text if msg.from_user.is_self else msg.reply
    spec = getfullargspec(func.__wrapped__).args
    await func(**{k: v for k, v in kwargs.items() if k in spec})


@dev.on_edited_message(
    filters.command("eval")
    & filters.user(OWNER)
    & ~filters.forwarded
    & ~filters.via_bot
)
@dev.on_message(
    filters.command("eval")
    & filters.user(OWNER)
    & ~filters.forwarded
    & ~filters.via_bot
)
async def executor(client: dev, message: Message):
    if len(message.command) < 2:
        return await edit_or_reply(message, text="ᴡʜᴀᴛ ʏᴏᴜ ᴡᴀɴɴᴀ ᴇxᴇᴄᴜᴛᴇ ʙᴀʙʏ ?")
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await message.delete()
    t1 = time()
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = "\n"
    if exc:
        evaluation += exc
    elif stderr:
        evaluation += stderr
    elif stdout:
        evaluation += stdout
    else:
        evaluation += "Success"
    final_output = f"<b>⥤ ʀᴇsᴜʟᴛ :</b>\n<pre language='python'>{evaluation}</pre>"
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(evaluation))
        t2 = time()
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="⏳",
                        callback_data=f"runtime {t2-t1} Seconds",
                    )
                ]
            ]
        )
        await message.reply_document(
            document=filename,
            caption=f"<b>⥤ ᴇᴠᴀʟ :</b>\n<code>{cmd[0:980]}</code>\n\n<b>⥤ ʀᴇsᴜʟᴛ :</b>\nAttached Document",
            quote=False,
            reply_markup=keyboard,
        )
        await message.delete()
        os.remove(filename)
    else:
        t2 = time()
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="⏳",
                        callback_data=f"runtime {round(t2-t1, 3)} Seconds",
                    ),
                    InlineKeyboardButton(
                        text="🗑",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        )
        await edit_or_reply(message, text=final_output, reply_markup=keyboard)


@dev.on_callback_query(filters.regex(r"runtime"))
async def runtime_func_cq(_, cq):
    runtime = cq.data.split(None, 1)[1]
    await cq.answer(runtime, show_alert=True)


@dev.on_callback_query(filters.regex("forceclose"))
async def forceclose_command(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    query, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        try:
            return await CallbackQuery.answer(
                "» ɪᴛ'ʟʟ ʙᴇ ʙᴇᴛᴛᴇʀ ɪғ ʏᴏᴜ sᴛᴀʏ ɪɴ ʏᴏᴜʀ ʟɪᴍɪᴛs ʙᴀʙʏ.", show_alert=True
            )
        except:
            return
    await CallbackQuery.message.delete()
    try:
        await CallbackQuery.answer()
    except:
        return


@dev.on_edited_message(
    filters.command("sh") & filters.user(OWNER) & ~filters.forwarded & ~filters.via_bot
)
@dev.on_message(
    filters.command("sh") & filters.user(OWNER) & ~filters.forwarded & ~filters.via_bot
)
async def shellrunner(client: dev, message: Message):
    if len(message.command) < 2:
        return await edit_or_reply(message, text="<b>ᴇxᴀᴍᴩʟᴇ :</b>\n/sh git pull")
    text = message.text.split(None, 1)[1]
    if "\n" in text:
        code = text.split("\n")
        output = ""
        for x in code:
            shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", x)
            try:
                process = subprocess.Popen(
                    shell,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
            except Exception as err:
                await edit_or_reply(message, text=f"<b>ERROR :</b>\n<pre>{err}</pre>")
            output += f"<b>{code}</b>\n"
            output += process.stdout.read()[:-1].decode("utf-8")
            output += "\n"
    else:
        shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", text)
        for a in range(len(shell)):
            shell[a] = shell[a].replace('"', "")
        try:
            process = subprocess.Popen(
                shell,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        except Exception as err:
            print(err)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errors = traceback.format_exception(
                etype=exc_type,
                value=exc_obj,
                tb=exc_tb,
            )
            return await edit_or_reply(
                message, text=f"<b>ERROR :</b>\n<pre>{''.join(errors)}</pre>"
            )
        output = process.stdout.read()[:-1].decode("utf-8")
    if str(output) == "\n":
        output = None
    if output:
        if len(output) > 4096:
            with open("output.txt", "w+") as file:
                file.write(output)
            await client.send_document(
                message.chat.id,
                "output.txt",
                reply_to_message_id=message.id,
                caption="<code>Output</code>",
            )
            return os.remove("output.txt")
        await edit_or_reply(message, text=f"<b>OUTPUT :</b>\n<pre>{output}</pre>")
    else:
        await edit_or_reply(message, text="<b>OUTPUT :</b>\n<code>None</code>")

RAUSHAN/modules/ids.py

from pyrogram import filters
from pyrogram.enums import ParseMode

from RAUSHAN import dev


@dev.on_message(filters.command("id"))
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.id
    reply = message.reply_to_message

    text = f"**[ᴍᴇssᴀɢᴇ ɪᴅ:]({message.link})** `{message_id}`\n"
    text += f"**[ʏᴏᴜʀ ɪᴅ:](tg://user?id={your_id})** `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"**[ʏᴏᴜʀ ɪᴅ:](tg://user?id={user_id})** `{user_id}`\n"

        except Exception:
            return await message.reply_text("ᴛʜɪs ᴜsᴇʀ ᴅᴏᴇsɴ'ᴛ ᴇxɪsᴛ.", quote=True)

    text += f"**[ᴄʜᴀᴛ ɪᴅ:](https://t.me/{chat.username})** `{chat.id}`\n\n"

    if (
        not getattr(reply, "empty", True)
        and not message.forward_from_chat
        and not reply.sender_chat
    ):
        text += f"**[ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ɪᴅ:]({reply.link})** `{reply.id}`\n"
        text += f"**[ʀᴇᴘʟɪᴇᴅ ᴜsᴇʀ ɪᴅ:](tg://user?id={reply.from_user.id})** `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += f"ᴛʜᴇ ғᴏʀᴡᴀʀᴅᴇᴅ ᴄʜᴀɴɴᴇʟ, {reply.forward_from_chat.title}, ʜᴀs ᴀɴ ɪᴅ ᴏғ `{reply.forward_from_chat.id}`\n\n"
        print(reply.forward_from_chat)

    if reply and reply.sender_chat:
        text += f"ɪᴅ ᴏғ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴄʜᴀᴛ/ᴄʜᴀɴɴᴇʟ, ɪs `{reply.sender_chat.id}`"
        print(reply.sender_chat)

    await message.reply_text(
        text,
        disable_web_page_preview=True,
        parse_mode=ParseMode.DEFAULT,
    )

RAUSHAN/modules/ping.py

# Don't remove This Line From Here.
# Telegram :- @ll_ALPHA_BABY_lll

import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import IMG, OWNER_USERNAME, STICKER
from RAUSHAN import BOT_NAME, dev
from RAUSHAN.database.chats import add_served_chat
from RAUSHAN.database.users import add_served_user
from RAUSHAN.modules.helpers import PNG_BTN


@dev.on_message(filters.command("ping", prefixes=["+", "/", "-", "?", "$", "&"]))
async def ping(_, message: Message):
    await message.reply_sticker(sticker=random.choice(STICKER))
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="ᴘɪɴɢ ᴘᴏɴɢ...",
    )
    try:
        await message.delete()
    except:
        pass

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"нєყ вαву!!\n{BOT_NAME} 𝚒ѕ al𝚒ve 🥀 αnd worĸɪng ғɪnє wɪтн ᴀ ᴘɪɴɢ oғ\n➥ `{ms}` ms\n\n<b> мα𝙳є ω𝚒тн ❣️ ву [𝘾𝙪𝙧𝙨𝙚𝙙 𝘾𝙝𝙞𝙡𝙙 🤍](https://t.me/{OWNER_USERNAME}) </b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)

RAUSHAN/modules/start.py

# Don't remove This Line From Here.
# Telegram :- @ll_ALPHA_BABY_lll

import asyncio
import random

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import EMOJIOS, IMG, STICKER
from RAUSHAN import BOT_NAME, AMBOT, dev
from RAUSHAN.database.chats import add_served_chat
from RAUSHAN.database.users import add_served_user
from RAUSHAN.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)


@AMBOT.on_message(filters.command(["start", "aistart"]) & ~filters.bot)
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("__ᴅʜɪʏᴀ ʜᴇʀᴇ..__")
        await asyncio.sleep(0.2)
        await accha.edit("__sᴛᴀʀᴛɪɴɢ..__")
        await asyncio.sleep(0.2)
        await accha.edit("__sᴛᴀʀᴛᴇᴅ..__")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=f"""**╭───────────────────⦿**\n**│⛩️ ʜᴇʏ ɪ ᴀᴍ {BOT_NAME} •**\n**├───────────────────⦿**\n**│-꩜> ɪ ʀᴇᴀᴅ ʏᴏᴜʀ ᴍɪɴᴅ •**\n**│⚡︎ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ •**\n**├───────────────────⦿**\n**│ꑭ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs •**\n**│☘ ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ •**\n**│✿ ғᴏʀ ᴀᴄᴛɪᴠᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ •**\n**│✇ ᴜsᴀɢᴇ /chatbot [ᴏɴ/ᴏғғ] •**\n**│𖣐 ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ •**\n**│🔥 24x7 ᴛɪᴍᴇ ᴏɴʟɪɴᴇ •**\n**├───────────────────⦿**\n**│🦊 ᴍᴀᴅᴇ ʙʏ...[˹ 𝐑𝐄𝐃 - 𝐋𝐈𝐍𝐄 ™ ˼](https://t.me/+QuuoMVb6zys0MDA1)♡**\n**╰───────────────────⦿""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)


@dev.on_message(filters.command(["help"], prefixes=["+", ".", "/", "-", "?", "$"]))
async def help(client: AMBOT, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_photo(
            photo=random.choice(IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption="**❍ ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


@dev.on_message(filters.command("repo") & ~filters.bot)
async def repo(_, m: Message):
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )


@dev.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(IMG), caption=START)

RAUSHAN/modules/stats.py
from pyrogram import filters
from pyrogram.types import Message
import random
import asyncio
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
import traceback
from pyrogram.types import Message
from pyrogram import *
from pyrogram.types import *
from config import OWNER_ID
from RAUSHAN import dev, OWNER
from RAUSHAN.database.chats import get_served_chats
from RAUSHAN.database.users import get_served_users


@dev.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats(cli: dev, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""ᴛᴏᴛᴀʟ sᴛᴀᴛs ᴏғ {(await cli.get_me()).mention} :

➻ **ᴄʜᴀᴛs :** {chats}
➻ **ᴜsᴇʀs :** {users}"""
    )

async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : blocked the bot\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception:
        return 500, f"{user_id} : {traceback.format_exc()}\n"

@dev.on_message(filters.command("gcast") & filters.user(OWNER_ID))
async def broadcast(_, message):
    if not message.reply_to_message:
        await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ɪᴛ.")
        return    
    exmsg = await message.reply_text("sᴛᴀʀᴛᴇᴅ ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ!")
    all_chats = (await get_served_chats()) or {}
    all_users = (await get_served_users()) or {}
    done_chats = 0
    done_users = 0
    failed_chats = 0
    failed_users = 0
    for chat in all_chats:
        try:
            await send_msg(chat, message.reply_to_message)
            done_chats += 1
            await asyncio.sleep(0.1)
        except Exception:
            pass
            failed_chats += 1

    for user in all_users:
        try:
            await send_msg(user, message.reply_to_message)
            done_users += 1
            await asyncio.sleep(0.1)
        except Exception:
            pass
            failed_users += 1
    if failed_users == 0 and failed_chats == 0:
        await exmsg.edit_text(
            f"**sᴜᴄᴄᴇssғᴜʟʟʏ ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ ✅**\n\n**sᴇɴᴛ ᴍᴇssᴀɢᴇ ᴛᴏ** `{done_chats}` **ᴄʜᴀᴛs ᴀɴᴅ** `{done_users}` **ᴜsᴇʀs**",
        )
    else:
        await exmsg.edit_text(
            f"**sᴜᴄᴄᴇssғᴜʟʟʏ ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ ✅**\n\n**sᴇɴᴛ ᴍᴇssᴀɢᴇ ᴛᴏ** `{done_chats}` **ᴄʜᴀᴛs** `{done_users}` **ᴜsᴇʀs**\n\n**ɴᴏᴛᴇ:-** `ᴅᴜᴇ ᴛᴏ sᴏᴍᴇ ɪssᴜᴇ ᴄᴀɴ'ᴛ ᴀʙʟᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ` `{failed_users}` **ᴜsᴇʀs ᴀɴᴅ** `{failed_chats}` **ᴄʜᴀᴛs**",
        )

@dev.on_message(filters.command("promo") & filters.user(OWNER_ID))
async def announced(_, message):
    if message.reply_to_message:
      to_send=message.reply_to_message.id
    if not message.reply_to_message:
      return await message.reply_text("Reply To Some Post To Broadcast")
    chats = await get_served_chats() or []
    users = await get_served_users() or []
    print(chats)
    print(users)
    failed = 0
    for chat in chats:
      try:
        await dev.forward_messages(chat_id=int(chat), from_chat_id=message.chat.id, message_ids=to_send)
        await asyncio.sleep(1)
      except Exception:
        failed += 1
    
    failed_user = 0
    for user in users:
      try:
        await dev.forward_messages(chat_id=int(user), from_chat_id=message.chat.id, message_ids=to_send)
        await asyncio.sleep(1)
      except Exception as e:
        failed_user += 1


    await message.reply_text("Bʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇ. {} ɢʀᴏᴜᴘs ғᴀɪʟᴇᴅ ᴛᴏ ʀᴇᴄᴇɪᴠᴇ ᴛʜᴇ ᴍᴇssᴀɢᴇ, ᴘʀᴏʙᴀʙʟʏ ᴅᴜᴇ ᴛᴏ ʙᴇɪɴɢ ᴋɪᴄᴋᴇᴅ. {} ᴜsᴇʀs ғᴀɪʟᴇᴅ ᴛᴏ ʀᴇᴄᴇɪᴠᴇ ᴛʜᴇ ᴍᴇssᴀɢᴇ, ᴘʀᴏʙᴀʙʟʏ ᴅᴜᴇ ᴛᴏ ʙᴇɪɴɢ ʙᴀɴɴᴇᴅ. .".format(failed, failed_user))

RAUSHAN/AMBOT
python3 -m RAUSHAN

RAUSHAN/__init__.py
import asyncio
import importlib
import logging
import re
import sys
import time

from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pyrogram import Client

import config
from RAUSHAN.modules import all_modules

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

boot = time.time()
mongo = MongoCli(config.MONGO_URL)
db = mongo.Anonymous


OWNER = config.OWNER_ID
# DEVS = config.SUDO_USERS | config.OWNER_ID


class AMBOT(Client):
    def __init__(self):
        super().__init__(
            name="AMBOT",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            plugins=dict(root="RAUSHAN.modules"),
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.id = get_me.id
        self.name = get_me.mention
        self.username = get_me.username

    async def stop(self):
        await super().stop()


dev = Client(
    "Dev",
    bot_token=config.BOT_TOKEN,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    # plugins=dict(root="RAUSHAN.modules"),
)

dev.start()

BOT_ID = config.BOT_TOKEN.split(":")[0]
x = dev.get_me()
BOT_NAME = x.first_name + (x.last_name or "")
BOT_USERNAME = x.username
BOT_MENTION = x.mention
BOT_DC_ID = x.dc_id

RAUSHAN/__main__.py

from flask import Flask
import threading
import asyncio
from pyrogram import idle
from RAUSHAN import LOGGER, AMBOT

# 🟢 IMPORTANT: Import handlers to register /start, /help etc.
import RAUSHAN.modules.start  # This line is REQUIRED

# Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"  # ✅ FIXED: Removed U+00A0 characters

# Flask runner
def run_flask():
    app.run(host="0.0.0.0", port=8000)

# Async bot runner
async def run_bot():
    LOGGER.info("The PURVI CHAT BOT Started.")
    bot = AMBOT()
    await bot.start()
    await idle()

if __name__ == "__main__":
    # Start Flask in background
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Run the Telegram bot
    asyncio.run(run_bot())  # ✅ FIXED: Closing parenthesis added

requirements.txt

flask
pyrogram==2.0.106
pymongo
motor
requests
dnspython
tgcrypto==1.2.2
asyncio
python-dotenv
waitress

config.py

from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "21883517"))
API_HASH = getenv("API_HASH", "3bcae2750b491a61c5e4ab8edd07cd7f")
BOT_TOKEN = getenv("BOT_TOKEN", "7668734217:AAEu9GCpIb85MDXufk6GAXLKcYtw8bI3Y7c")
OWNER_ID = int(getenv("OWNER_ID", "7049074888"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Demonking:demonking007@cluster0.cmrd5ce.mongodb.net/")
SUPPORT_GRP = getenv("SUPPORT_GRP", "https://t.me/group_friendship_tamil")
UPDATE_CHNL = getenv("UPDATE_CHNL", "https://t.me/+QuuoMVb6zys0MDA1")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Rubesh_official_18")

# Random Start Images
IMG = [
    "https://graph.org/file/34c1ff73f9ae51eed974c-9913f3376d10e92eea.jpg",
    "https://graph.org/file/1f087933ac7612c0a77ff-88b2d7f7e2b0dd2a73.jpg",
    "https://graph.org/file/71415be05ef6bf4c18189-18f6c1d2c8fc81fcc0.jpg",
    "https://graph.org/file/80facdfa16e6b1d1c40bc-14758bc81032e72624.jpg",
    "https://graph.org/file/0428097801ed4aabf41ee-b23d4a093d305b3563.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgUAAxkBAAEBTKBoMeIDuThNUMwvosxdSCDq0aIUCQACfwYAAu3l8VZv8f4t1VtktzYE",
    "CAACAgUAAxkBAAEBTKJoMeI9tB0msMLsl8n-jG3kFSuMxQAC2QYAAvAp8Fb9yy558EKhazYE",
    "CAACAgUAAxkBAAEBTKZoMeMOvoiYYDgpUOiQJ_N_JoNPMQAC0Q8AAu8GKVd1IWP6F8MJVDYE",
]


EMOJIOS = [
    "🎲",
    "🔥",
    "⚡️",
    "⛈",
    "🌩",
    "🌦",
    "☀️",
    "💫",
    "🐳",
    "🦑",
]

heroku.yml

build:
  docker:
    worker: Dockerfile
run:
  worker: python3 -m RAU
SHAN

app.json

{
  "name": "𝐏ᴜʀᴠɪ 𝐂ʜᴀᴛ",
  "description": "A telegram bot",
  "logo": "https://telegra.ph/file/c319f8cffa722e5c4bb85.jpg",
  "keywords": [
    "Chatbot",
    "mongodb",
    "python",
    "pyrogram"
  ],
    "buildpacks": [{
    "url": "heroku/python"
  }],
  "repository": "https://github.com/rubeshofficial/Dhiyachatbot",
  "env": {
    "API_ID": {
      "description": "Get this value from my.telegram.org/apps.",
      "required": true,
      "value": "21883517"
    },
    "API_HASH": {
      "description": "Get this value from my.telegram.org/apps.",
      "required": true,
      "value": "3bcae2750b491a61c5e4ab8edd07cd7f"
    },
    "BOT_TOKEN": {
      "description": "A Bot token from @BotFather",
      "required": true,
      "value": "7668734217:AAEu9GCpIb85MDXufk6GAXLKcYtw8bI3Y7c"
    },
    "MONGO_URL": {
      "description": "Get a mongodb url from https://cloud.mongodb.com.",
      "required": true,
      "value": "mongodb+srv://Demonking:demonking007@cluster0.cmrd5ce.mongodb.net/"
    },
    "OWNER_ID": {
      "description": "User id of the user who will known as owner of the bot.",
      "required": true,
      "value": "7049074888"
    }
  }
}

Dockerfile

FROM python:latest

RUN apt-get update -y && apt-get upgrade -y

RUN pip3 install -U pip

COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirements.txt

CMD python3 -m RAUSHAN

Procfile
worker: python3 -m RAUSHAN

AMBOT
python3 -m RAUSHAN

Now give. Code like best professional developer write me please 🥺👇❤️
