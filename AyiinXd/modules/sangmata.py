# Copyright (C) 2021 Catuserbot <https://github.com/sandy1709/catuserbot>
# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
import re
import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import (
    _format,
    ayiin_cmd,
    eod,
    eor,
    get_user_from_event,
)

from . import cmd

@ayiin_cmd(pattern="sg(u)?(?:\\s|$)([\\s\\S]*)")
async def _(event):
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not input_str and not reply_message:
        await eod(
            event,
            "**Maaf Pengguna Tidak Ditemukan.**",
            time=90
        )
    user, rank = await get_user_from_event(event, secondgroup=True)
    if not user:
        return
    uid = user.id
    chat = "@SangMata_BOT"
    yinsevent = await eor(event, "**Memproses....**")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(f"{uid}")
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message(f"{uid}")
        responses = []
        while True:
            try:
                response = await conv.get_response(timeout=2)
            except asyncio.TimeoutError:
                break
            responses.append(response.text)
        await event.client.send_read_acknowledge(conv.chat_id)
    if not responses:
        await eod(yinsevent, "**Orang Ini Belum Pernah Mengganti Namanya**", time=90)
    if "No records found" in responses:
        await eod(yinsevent, "**Orang Ini Belum Pernah Mengganti Namanya**", time=90)
    names, usernames = await sangmata_seperator(responses)
    cmd = event.pattern_match.group(1)
    ayiin = None
    check = (usernames, "Username") if cmd == "u" else (names, "Name")
    user_name = (
        f"{user.first_name} {user.last_name}"
        if user.last_name
        else user.first_name
    )
    output = f"** User Info :**  {_format.mentionuser(user_name, user.id)}\n** {check[1]} History :**\n{check[0]}"
    await eor(yinsevent, output)

async def sangmata_seperator(sanga_list):
    string = "".join(info[info.find("\n") + 1 :] for info in sanga_list)
    string = re.sub(r"^$\n", "", string, flags=re.MULTILINE)
    name, username = string.split("Usernames**")
    name = name.split("Names")[1]
    return name, username

CMD_HELP.update(
    {
        "sangmata": f"**Plugin : **`sangmata`\
        \n\n  »  **Perintah :** `{cmd}sg` <sambil reply chat>\
        \n  »  **Kegunaan : **Mendapatkan Riwayat Nama Pengguna selama di telegram.\
        \n\n  »  **Perintah :** `{cmd}sgu` <sambil reply chat>\
        \n  »  **Kegunaan : **Mendapatkan Riwayat Username Pengguna selama di telegram.\
    "
    }
)
