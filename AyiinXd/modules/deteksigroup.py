# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport


from telethon.errors.rpcerrorlist import YouBlockedUserError
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, bot
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@ayiin_cmd(pattern="dgrup(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not event.reply_to_msg_id:
        await eod(event, get_string("dgrp_1").format(cmd))
        return
    if input_str:
        try:
            ayiinid = int(input_str)
        except ValueError:
            try:
                a = await event.client.get_entity(input_str)
            except ValueError:
                await eod(event, get_string("dgrp_3"))
            ayiinid = a.id
    else:
        ayiinid = reply_message.sender_id
    chat = "@tgscanrobot"
    yins = await eor(event, get_string("com_7"))
    async with bot.conversation(chat) as conv:
        try:
            await conv.send_message(f"{ayiinid}")
        except YouBlockedUserError:
            await event.reply(get_string("dgrp_2")
                              )
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await yins.edit(response.text)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "deteksigrup": f"**Plugin : **`deteksigrup`\
        \n\n  »  **Perintah :** `{cmd}dgrup <Id/Username Grup>`\
        \n  »  **Kegunaan : **Untuk Melihat Riwayat Grup\
    "
    }
)
