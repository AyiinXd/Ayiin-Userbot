# 🍀 © @tofik_dn
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
# ⚠️ Do not remove credits

from secrets import choice

from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, edit_or_reply

from . import cmd, var


@ayiin_cmd(pattern="asupan$")
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@tedeasupancache", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(asupannya), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan video asupan.**")


@ayiin_cmd(pattern="desahcewe$")
async def _(event):
    if event.chat_id in var.BLACKLIST_CHAT:
        return await edit_or_reply(
            event, "**Perintah ini Dilarang digunakan di Group ini**"
        )
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        desahcewe = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancewesangesange", filter=InputMessagesFilterVoice
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(desahcewe), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan desahan cewe.**")


@ayiin_cmd(pattern="desahcowo$")
async def _(event):
    if event.chat_id in var.BLACKLIST_CHAT:
        return await edit_or_reply(
            event, "**Perintah ini Dilarang digunakan di Group ini**"
        )
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        desahcowo = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancowokkkk", filter=InputMessagesFilterVoice
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(desahcowo), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan desahan cowo.**")


CMD_HELP.update(
    {
        "asupan": f"**Plugin : **`asupan`\
        \n\n  »  **Perintah :** `{cmd}asupan`\
        \n  »  **Kegunaan : **Untuk Mengirim video asupan secara random.\
        \n\n  »  **Perintah :** `{cmd}desahcowo`\
        \n  »  **Kegunaan : **Untuk Mengirim voice desah cowo secara random.\
        \n\n  »  **Perintah :** `{cmd}desahcewe`\
        \n  »  **Kegunaan : **Untuk Mengirim voice desah cewe secara random.\
    "
    }
)
