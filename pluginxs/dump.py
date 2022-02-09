import os
import asyncio
from main import xbot as Client
from pyrogram import Client, filters

XCHAT_ID = int(os.environ.get("XCHAT_ID"))
DELETE_DELAY = 8

def detect_type(message):
    if message.audio:
        return message.audio
    else:
        return

@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        text=f"Hello",
        disable_web_page_preview=True,
        parse_mode="html",
    )

@Client.on_message(filters.audio & ~filters.channel & ~filters.private)
async def media_receive_handler(client, message):
    file = detect_type(message)
    file_name = ""
    if file:
        file_name = file.file_name
    await message.forward(chat_id=XCHAT_ID)
    reply = await message.reply_text(f"Dumpped")
    await _delay_delete_messages((reply, message), DELETE_DELAY)
    
async def _delay_delete_messages(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for message in messages:
        await message.delete()
