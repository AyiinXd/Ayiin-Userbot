# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot module containing commands for interacting with dogbin(https://del.dog)"""

import os

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from AyiinXd.ayiin.pastebin import PasteBin

from . import cmd, var


@ayiin_cmd(pattern="paste(?: (-d|-n|-h|-k|-s)|$)?(?: ([\\s\\S]+)|$)")
async def paste(pstl):
    """For .paste command, pastes the text directly to a pastebin."""
    service = pstl.pattern_match.group(1)
    match = pstl.pattern_match.group(2)
    reply_id = pstl.reply_to_msg_id

    if not (match or reply_id):
        return await eod(pstl, "`Elon Musk bilang saya tidak bisa menempelkan kekosongan.`")

    if match:
        message = match.strip()
    elif reply_id:
        message = await pstl.get_reply_message()
        if message.media:
            downloaded_file_name = await pstl.client.download_media(
                message,
                var.TEMP_DOWNLOAD_DIRECTORY,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = "".join(m.decode("UTF-8") for m in m_list)
            os.remove(downloaded_file_name)
        else:
            message = message.message

    xxnx = await eor(pstl, "`Menempelkan teks ...`")
    async with PasteBin(message) as client:
        if service:
            service = service.strip()
            if service not in ["-d", "-n", "-k", "-s", "-h"]:
                return await xxnx.edit("Invalid flag")
            await client(client.service_match[service])
        else:
            await client.post()

        if client:
            reply_text = f"**Ditempel dengan sukses!**\n\n[URL]({client.link})\n[View RAW]({client.raw_link})"
        else:
            reply_text = "**Gagal mencapai Layanan Pastebin**"

    await xxnx.edit(reply_text, link_preview=False)


CMD_HELP.update(
    {
        "paste": f"**Plugin : **`paste`\
        \n\n  »  **Perintah :** `{cmd}paste` <text/reply>\
        \n  »  **Kegunaan : **Untuk Menyimpan text ke ke layanan pastebin gunakan flags [`-d`, `-n`, `-h`, `-s`, `-k`]\
        \n\n  •  **NOTE :** `-d` = **Dogbin** atau `-n` = **Nekobin** atau `-h` = **Hastebin** atau `-k` = **katbin** atau `-s` = **spacebin**\
    "
    }
)
