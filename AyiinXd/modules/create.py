# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for filter commands """

from telethon.tl import functions

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eor
from Stringyins import get_string


@ayiin_cmd(pattern="buat (gb|g|c)(?: |$)(.*)")
async def _(grop):
    """For .create command, Creating New Group & Channel"""
    if grop.text[0].isalpha() or grop.text[0] in ("/", "#", "@", "!"):
        return
    if grop.fwd_from:
        return
    type_of_group = grop.pattern_match.group(1)
    group_name = grop.pattern_match.group(2)
    if type_of_group == "gb":
        try:
            result = await grop.client(
                functions.messages.CreateChatRequest(
                    users=["@MissRose_bot"],
                    # Not enough users (to create a chat, for example)
                    # Telegram, no longer allows creating a chat with
                    # ourselves
                    title=group_name,
                )
            )
            created_chat_id = result.chats[0].id
            result = await grop.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await eor(
                grop,
                get_string("create_1").format(
                    group_name, group_name, result.link
                )
            )
        except Exception as e:
            await grop.edit(str(e))
    elif type_of_group in ["g", "c"]:
        try:
            r = await grop.client(
                functions.channels.CreateChannelRequest(
                    title=group_name,
                    about=get_string("create_2"),
                    megagroup=type_of_group != "c",
                )
            )

            created_chat_id = r.chats[0].id
            result = await grop.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await eor(
                grop,
                get_string("create_1").format(
                    group_name, group_name, result.link
                )
            )
        except Exception as e:
            await grop.edit(str(e))


CMD_HELP.update(
    {
        "membuat": f"**Plugin : **`membuat`\
        \n\n  »  **Perintah :** `{cmd}buat g` <nama grup>\
        \n  »  **Kegunaan : **Membuat grup telegram.\
        \n\n  »  **Perintah :** `{cmd}buat gb` <nama grup>\
        \n  »  **Kegunaan : **Membuat Grup bersama bot.\
        \n\n  »  **Perintah :** `{cmd}buat c` <nama channel>\
        \n  »  **Kegunaan : **Membuat sebuah Channel.\
    "
    }
)
