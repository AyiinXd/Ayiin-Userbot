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


@ayiin_cmd(pattern="pdf(?: |$)(.*)")
async def _(event):
    if not event.reply_to_msg_id:
        return await eor(event, get_string("pdf_4"))
    reply_message = await event.get_reply_message()
    chat = "@office2pdf_bot"
    xx = await eor(event, get_string("pdf_1"))
    try:
        async with event.client.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("/start")
                response = await conv.get_response()
                msg = await conv.send_message(reply_message)
                convert = await conv.send_message("/ready2conv")
                cnfrm = await conv.get_response()
                editfilename = await conv.send_message("Yes")
                enterfilename = await conv.get_response()
                filename = await conv.send_message("Ayiin-Userbot")
                started = await conv.get_response()
                pdf = await conv.get_response()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.client(UnblockRequest(chat))
                return await xx.edit(get_string("pdf_2")
                )
            await event.client.send_message(event.chat_id, pdf)
            await event.client.delete_messages(
                conv.chat_id,
                [
                    msg_start.id,
                    response.id,
                    msg.id,
                    started.id,
                    filename.id,
                    editfilename.id,
                    enterfilename.id,
                    cnfrm.id,
                    pdf.id,
                    convert.id,
                ],
            )
            await xx.delete()
    except TimeoutError:
        return await xx.edit(get_string("pdf_3")
        )


CMD_HELP.update(
    {
        "pdf": f"**Plugin : **`pdf`\
        \n\n  »  **Perintah :** `{cmd}pdf` <reply text>\
        \n  »  **Kegunaan : **Untuk Mengconvert teks menjadi file PDF menggunakan @office2pdf_bot\
    "
    }
)
