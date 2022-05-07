# Copyright (C) 2021 Man-Userbot
# Created by mrismanaziz
# FROM <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

from asyncio.exceptions import TimeoutError

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eor
from Stringyins import get_string


@ayiin_cmd(pattern="short(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    msg_link = await event.get_reply_message()
    d_link = event.pattern_match.group(1)
    if msg_link:
        d_link = msg_link.text
        xx = await eor(event, get_string("shortlink_1"))
    elif "https" not in d_link:
        await eor(
            event, get_string("shortlink_2")
        )
    else:
        xx = await eor(event, get_string("shortlink_1"))
    chat = "@ShortUrlBot"
    try:
        async with event.client.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("/start")
                bot_reply = await conv.get_response()
                msg = await conv.send_message(d_link)
                response = await conv.get_response()
                url = await conv.get_response()
                sponser = await conv.get_response()
                await event.client.send_read_acknowledge(conv.chat_id)
                await event.edit(response.text)
            except YouBlockedUserError:
                await event.client(UnblockRequest(chat))
                return await xx.edit(get_string("shortlink_3"))
            await event.client.send_message(event.chat_id, url)
            await event.client.delete_messages(
                conv.chat_id,
                [msg_start.id, response.id, msg.id, bot_reply.id, sponser.id, url.id],
            )
            await event.delete()
    except TimeoutError:
        return await xx.edit(get_string("error_8").format("@ShortUrlBot")
        )


CMD_HELP.update(
    {
        "shortlink": f"**Plugin : **`shortlink`\
        \n\n  »  **Perintah :** `{cmd}short` <url/reply link>\
        \n  »  **Kegunaan : **Untuk menyimpelkan link url menjadi pendek menggunakan @ShortUrlBot\
    "
    }
)
