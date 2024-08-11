from pyrogram import Client, filters

@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"**ꜱᴛɪᴄᴋᴇʀ ɪᴅ ɪꜱ**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** ᴜɴɪQᴜᴇ ɪᴅ ɪꜱ ** \n\n`{message.reply_to_message.sticker.file_unique_id}`\n\nJoine - @PandaWep", quote=True)
    else: 
       await message.reply("<b>ᴏᴏᴘꜱ !! ɴᴏᴛ ᴀ ꜱᴛɪᴄᴋᴇʀ ꜰɪʟᴇ</b>")
