# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# This file is a part of < https://github.com/mrismanaziz/Man-Userbot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

from telethon.tl.functions.channels import LeaveChannelRequest

from AyiinXd import BLACKLIST_CHAT
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eor
from Stringyins import get_string


@ayiin_cmd(pattern="kickme$", allow_sudo=False)
async def kickme(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await eor(
            event, get_string("ayiin_1"))
    user = await event.client.get_me()
    await eor(event, get_string("kikme_1").format(user.first_name))
    await event.client.kick_participant(event.chat_id, "me")


@ayiin_cmd(pattern="kikme$", allow_sudo=False)
async def kikme(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await eor(
            event, get_string("ayiin_1")
        )
    await eor(event, get_string("kikme_2"))
    await event.client.kick_participant(event.chat_id, "me")


@ayiin_cmd(pattern="leaveall$", allow_sudo=False)
async def kickmeall(event):
    Yins = await eor(event, get_string("kikme_3"))
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await event.client(LeaveChannelRequest(chat))
            except BaseException:
                er += 1
    await Yins.edit(get_string("kikme_4").format(done, er)
    )


CMD_HELP.update(
    {
        "kickme": f"**Plugin : **`kickme`\
        \n\n  »  **Perintah :** `{cmd}kickme`\
        \n  »  **Kegunaan : **Keluar grup dengan menampilkan pesan Master has left this group, bye!!\
        \n\n  »  **Perintah :** `{cmd}kikme`\
        \n  »  **Kegunaan : **Keluar grup dengan menampilkan pesan GC NYA JELEK GOBLOK KELUAR DULU AH CROTT 🥴\
        \n\n  »  **Perintah :** `{cmd}leaveall`\
        \n  »  **Kegunaan : **Keluar dari semua grup telegram yang anda gabung.\
    "
    }
)
