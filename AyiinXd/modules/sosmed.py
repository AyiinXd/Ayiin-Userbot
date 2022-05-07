# Port by Koala 🐨/@manuskarakitann
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot/>
# t.me/SharingUserbot & t.me/Lunatic0de
# Nyenyenye bacot

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.messages import DeleteHistoryRequest

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string


@ayiin_cmd(pattern="sosmed(?: |$)(.*)")
async def insta(event):
    xxnx = event.pattern_match.group(1)
    if xxnx:
        link = xxnx
    elif event.is_reply:
        link = await event.get_reply_message()
    else:
        return await eod(
            event, get_string("sosmed_1")
        )
    xx = await eor(event, get_string("com_5"))
    chat = "@SaveAsbot"
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=523131145)
            )
            await event.client.send_message(chat, link)
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await event.client.send_message(chat, link)
            response = await response
        if response.text.startswith("Forward"):
            await xx.edit(get_string("sosmed_2"))
        else:
            await xx.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            await event.client(DeleteHistoryRequest(peer=chat, max_id=0))
            await xx.delete()


@ayiin_cmd(pattern="dez(?: |$)(.*)")
async def DeezLoader(event):
    if event.fwd_from:
        return
    dlink = event.pattern_match.group(1)
    if ".com" not in dlink:
        await eod(
            event, get_string("sosdez_1")
        )
    else:
        await eor(event, get_string("com_5"))
    chat = "@DeezLoadBot"
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.get_response()
            await conv.send_message(dlink)
            details = await conv.get_response()
            song = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.get_response()
            await conv.send_message(dlink)
            details = await conv.get_response()
            song = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_file(event.chat_id, song, caption=details.text)
        await event.delete()


@ayiin_cmd(pattern="tiktok(?: |$)(.*)")
async def _(event):
    xxnx = event.pattern_match.group(1)
    if xxnx:
        d_link = xxnx
    elif event.is_reply:
        d_link = await event.get_reply_message()
    else:
        return await eod(
            event, get_string("sostik_1")
        )
    xx = await eor(event, get_string("sostik_2"))
    chat = "@thisvidbot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            video = await conv.get_response()
            text = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            video = await conv.get_response()
            text = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_file(event.chat_id, video)
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, r.id, msg.id, details.id, video.id, text.id]
        )
        await xx.delete()


CMD_HELP.update(
    {
        "sosmed": f"**Plugin : **`sosmed`\
        \n\n  »  **Perintah :** `{cmd}sosmed` <link>\
        \n  »  **Kegunaan : **Download Media Dari Pinterest / Tiktok / Instagram.\
        \n\n  »  **Perintah :** `{cmd}dez` <link>\
        \n  »  **Kegunaan : **Download Lagu Via Deezloader\
    "
    }
)


CMD_HELP.update(
    {
        "tiktok": f"**Plugin : **`tiktok`\
        \n\n  »  **Perintah :** `{cmd}tiktok` <link>\
        \n  »  **Kegunaan : **Download Video Tiktok Tanpa Watermark\
    "
    }
)
