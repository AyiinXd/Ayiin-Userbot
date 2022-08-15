# Copyright (C) 2020 Alfiananda P.A
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

import asyncio
import time

from telethon.tl.types import DocumentAttributeFilename

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, bash, eor, progress
from Stringyins import get_string


@ayiin_cmd(pattern="ssvideo(?: |$)(.*)")
async def ssvideo(event):
    if not event.reply_to_msg_id:
        await eor(event, get_string("failed3"))
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await eor(event, get_string("ssvideo_4"))
        return
    try:
        frame = int(event.pattern_match.group(1))
        if frame > 10:
            return await eor(event, get_string("ssvideo_1"))
    except BaseException:
        return await eor(event, get_string("ssvideo_2"))
    if reply_message.photo:
        return await eor(event, get_string("ssvideo_3"))
    if (
        DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
        in reply_message.media.document.attributes
    ):
        return await eor(event, get_string("error_5"))
    if (
        DocumentAttributeFilename(file_name="sticker.webp")
        in reply_message.media.document.attributes
    ):
        return await eor(event, get_string("error_5"))
    c_time = time.time()
    await eor(event, get_string("com_5"))
    ss = await event.client.download_media(
        reply_message,
        "anu.mp4",
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "[DOWNLOAD]")
        ),
    )
    try:
        await eor(event, get_string("com_1"))
        command = f"vcsi -g {frame}x{frame} {ss} -o ss.png "
        await bash(command)
        await event.client.send_file(
            event.chat_id,
            "ss.png",
            reply_to=event.reply_to_msg_id,
        )
        await event.delete()
        await bash("rm -rf *.png")
        await bash("rm -rf *.mp4")
    except BaseException as e:
        await bash("rm -rf *.png")
        await bash("rm -rf *.mp4")
        return await eor(event, get_string("error_1").format(e))


CMD_HELP.update(
    {
        "ssvideo": f"**Plugin : **`ssvideo`\
        \n\n  »  **Perintah :** `{cmd}ssvideo <frame>`\
        \n  »  **Kegunaan : **Untuk Screenshot video dari frame per frame\
    "
    }
)
