from pyrogram import filters
from pyrogram.types import Message

from SWEET_TOXIC_MUSIC import app
from SWEET_TOXIC_MUSIC.core.call import SWEET_TOXIC_DEVIL

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await SWEET_TOXIC_DEVIL.stop_stream_force(message.chat.id)
