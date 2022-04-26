import asyncio
from time import time
from datetime import datetime
from config import BOT_USERNAME
from config import GROUP_SUPPORT, UPDATES_CHANNEL
from NIXA.filters import command
from NIXA.command import commandpro
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from NIXA.main import bot as Client

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/852ec1d19ae76335aea02.jpg",
        caption=f"""**ʜᴇʏ ɢᴜʏꜱ 
ᴛʜɪꜱ ʙᴏᴛ ʜᴀꜱ ᴀ ʟᴏᴛ ᴏꜰ ꜰᴇᴀᴛᴜʀᴇꜱ ʙᴀꜱᴇᴅ ᴏɴ ᴀ.ɪ ᴀɴᴅ ʜɪɢʜ ꜱᴏᴜɴᴅ Qᴜᴀʟɪᴛʏ ᴏꜰ ꜱᴏɴɢꜱ.
ᴀɴᴅ ᴛʜɪꜱ ᴍᴜꜱɪᴄ ʙᴏᴛ ꜱᴍᴀꜱʜ ᴛʜᴇᴍ ᴏꜰ ᴀʟʟ ꜱᴇʀᴠᴇʀ ᴏꜰ ᴍᴜꜱɪᴄ ʙᴏᴛ ᴀꜱꜱ..
ᴘᴏᴡᴇʀᴇᴅ ʙʏ [sᴜᴍɪᴛ ʏᴀᴅᴀᴠ](t.me/Simple_Mundaa)
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚕️ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ ⚕️", url=f"https://youtube.com/channel/UCtI7hbY-BD7wvuIzoSU0cEw"
                    ),
                    InlineKeyboardButton(
                        "🎃 ᴏᴡɴᴇʀ 🎃", url="https://t.me/Simple_Mundaa"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📢 ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "✨ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ", url=f"https://t.me/{GROUP_SUPPORT}"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/stats"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/bf9f444677e4d565542a6.jpg",
        caption=f"""ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ  ғᴏʀ ᴀɴʏ ǫᴜᴇʀʏ ʏᴏᴜ ᴄᴀɴ ᴊᴏɪɴ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ᴀɴᴅ ᴄʜᴀɴɴᴇʟ.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ•", url=f"https://youtube.com/channel/UCtI7hbY-BD7wvuIzoSU0cEw")
                ]
            ]
        ),
    )

 
