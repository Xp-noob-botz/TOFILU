import time
import random
from pyrogram import Client, filters
import asyncio

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    m=await message.reply_sticker("CAACAgQAAxkBAAILs2YVUuG747DVSVDPgBkSRis39jbaAAIXAwACcnEXJWSGFvSlUt95HgQ") 
    await message.reply_text("ʙᴜᴅᴅʏ ɪ ᴀᴍ ꜱᴛɪʟʟ ᴀʟɪᴠᴇ :) ʜɪᴛ /start \nʜɪᴛ /ping ᴛᴏ ᴄʜᴇᴄᴋ ᴍʏ ᴘɪɴɢ 🦋")
    await asyncio.sleep(30)
    await m.delete()


@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"🏓ᴘᴏɴɢ - {time_taken_s:.3f} ms")
