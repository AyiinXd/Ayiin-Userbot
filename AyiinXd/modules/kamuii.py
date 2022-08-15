# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

import os

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string


@ayiin_cmd(pattern="kamuii(:? |$)([1-8])?")
async def _(fry):
    xx = await eor(fry, get_string("kamui_1"))
    level = fry.pattern_match.group(2)
    if fry.fwd_from:
        return
    if not fry.reply_to_msg_id:
        await eod(xx, get_string("failed3"))
        return
    reply_message = await fry.get_reply_message()
    if not reply_message.media:
        await eod(xx, get_string("com_4"))
        return
    if reply_message.sender.bot:
        await eod(xx, get_string("failed3"))
        return
    chat = "@image_deepfrybot"
    message_id_to_reply = fry.message.reply_to_msg_id
    async with fry.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(reply_message)
            if level:
                m = f"/deepfry {level}"
                msg_level = await conv.send_message(m, reply_to=msg.id)
                r = await conv.get_response()
            response = await conv.get_response()
            await fry.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await fry.client(UnblockRequest(chat))
            msg = await conv.send_message(reply_message)
            if level:
                m = f"/deepfry {level}"
                msg_level = await conv.send_message(m, reply_to=msg.id)
                r = await conv.get_response()
            response = await conv.get_response()
            await fry.client.send_read_acknowledge(conv.chat_id)
        if response.text.startswith("Forward"):
            await xx.edit(get_string("kamui_2"))
        else:
            downloaded_file_name = await fry.client.download_media(
                response.media, TEMP_DOWNLOAD_DIRECTORY
            )
            await fry.client.send_file(
                fry.chat_id,
                downloaded_file_name,
                force_document=False,
                reply_to=message_id_to_reply,
            )
            try:
                msg_level
            except NameError:
                await fry.client.delete_messages(conv.chat_id, [msg.id, response.id])
            else:
                await fry.client.delete_messages(
                    conv.chat_id, [msg.id, response.id, r.id, msg_level.id]
                )
    await fry.delete()
    return os.remove(downloaded_file_name)


CMD_HELP.update(
    {
        "kamuii": f"**Plugin : **`kamuii`\
        \n\n  »  **Perintah :** `{cmd}kamuii` atau `{cmd}kamuii` [level(1-8)]\
        \n  »  **Kegunaan : **Untuk mengubah foto/sticker menjadi penyok.\
    "
    }
)
