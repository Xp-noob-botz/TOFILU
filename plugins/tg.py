import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from telegraph import upload_file
from pyrogram.types import Message

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            "sticker"
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj

@Client.on_message(filters.command("telegraph") & filters.private)
async def telegraph_upload(bot, update):
    replied = update.reply_to_message
    if not replied:
        await update.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴠɪᴅᴇᴏ ᴜɴᴅᴇʀ 5 ᴍʙ. <code>/telegraph</code>")
        return
    file_info = get_file_id(replied)
    if not file_info:
        await update.reply_text("ɴᴏᴛ ꜱᴜᴘᴘᴏʀᴛᴇᴅ!")
        return
    text = await update.reply_text(text="ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛᴏ ᴍʏ ꜱᴇʀᴠᴇʀ ...", disable_web_page_preview=True)   
    media = await update.reply_to_message.download()   
    await text.edit_text(text="ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴄᴏᴍᴘʟᴇᴛᴇᴅ. ɴᴏᴡ ɪ ᴀᴍ ᴜᴘʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀ.ᴘʜ ʟɪɴᴋ ...", disable_web_page_preview=True)                                            
    try:
        response = upload_file(media)
    except Exception as error:
        print(error)
        await text.edit_text(text=f"Error :- {error}", disable_web_page_preview=True)       
        return    
    try:
        os.remove(media)
    except Exception as error:
        print(error)
        return    
    await text.edit_text(
        text=f"<b>Link :-</b>\n\n<code>https://graph.org{response[0]}</code>",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(text="ᴏᴘᴇɴ ʟɪɴᴋ", url=f"https://graph.org{response[0]}"),
            InlineKeyboardButton(text="ꜱʜᴀʀᴇ ʟɪɴᴋ", url=f"https://telegram.me/share/url?url=https://graph.org{response[0]}")
            ],[
            InlineKeyboardButton(text="✗ ᴄʟᴏꜱᴇ ✗", callback_data="close")
            ]])
        )
