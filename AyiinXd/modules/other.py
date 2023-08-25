# Copyright (c) 2021 Man-Userbot
# Created by mrismanaziz
# FROM <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#
# Thanks To Ultroid <https://github.com/TeamUltroid/Ultroid>
# Thanks To Geez-UserBot <https://github.com/vckyou/Geez-UserBot>

import os

from telethon import events
from telethon.errors.rpcerrorlist import ChatAdminRequiredError, YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.types import ChannelParticipantsKicked

from AyiinXd import CMD_HELP, LOGS
from AyiinXd.ayiin import ayiin_cmd, eod, eor

from . import cmd


@ayiin_cmd(pattern="open(?: |$)(.*)")
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    with open(b, "r") as a:
        c = a.read()
    await eor(event, "**Berhasil Membaca Berkas**")
    if len(c) > 4095:
        await eor(
            event,
            c,
            deflink=True,
            linktext="**Berhasil Membaca Berkas**"
        )
    else:
        await event.client.send_message(event.chat_id, f"`{c}`")
        await event.delete()
    os.remove(b)


@ayiin_cmd(pattern="sendbot (.*)")
async def _(event):
    if event.fwd_from:
        return
    chat = str(event.pattern_match.group(1).split(" ", 1)[0])
    link = str(event.pattern_match.group(1).split(" ", 1)[1])
    if not link:
        return await eor(event, "**Maaf BOT Tidak Merespond.**")

    botid = await event.client.get_entity(chat)
    xx = await eor(event, "**Memproses...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=botid)
            )
            msg = await event.client.send_message(chat, link)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            msg = await event.client.send_message(chat, link)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except BaseException:
            await eod(xx, "**Tidak dapat menemukan bot itu 🥺**")
        await xx.edit(f"**Pesan Terkirim:** `{link}`\n**Kepada: {chat}**")
        await event.client.send_message(event.chat_id, response.message)
        await event.client.send_read_acknowledge(event.chat_id)
        await event.client.delete_messages(conv.chat_id, [msg.id, response.id])


@ayiin_cmd(pattern="allunban$")
async def _(event):
    xx = await eor(event, "`Searching Participant Lists...`")
    p = 0
    title = (await event.get_chat()).title
    async for i in event.client.iter_participants(
        event.chat_id,
        filter=ChannelParticipantsKicked,
        aggressive=True,
    ):
        try:
            await event.client.edit_permissions(event.chat_id, i, view_messages=True)
            p += 1
        except ChatAdminRequiredError:
            pass
        except BaseException as er:
            LOGS.exeption(er)
    await xx.edit(f"**Berhasil unbanned** `{p}` **Orang di Grup {title}**")


@ayiin_cmd(pattern="(?:dm)\\s?(.*)?")
async def _(event):
    p = event.pattern_match.group(1)
    m = p.split(" ")
    chat_id = m[0]
    try:
        chat_id = int(chat_id)
    except BaseException:
        pass
    mssg = await event.get_reply_message()
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await eor(event, "**Berhasil Mengirim Pesan Anda.**")
    msg = "".join(f"{i} " for i in m[1:])
    if not msg:
        return
    try:
        await event.client.send_message(chat_id, msg)
        await eor(event, "**Berhasil Mengirim Pesan Anda.**")
    except BaseException:
        await eod(event, "**Gagal Mengirim Pesan.**", time=10)


@ayiin_cmd(pattern="fwdreply ?(.*)")
async def _(e):
    message = e.pattern_match.group(1)
    if not e.reply_to_msg_id:
        return await eor(e, "**Mohon Balas Ke Pesan Penggunanya**")
    if not message:
        return await eor(e, "`Tidak ditemukan pesan untuk disampaikan`")
    msg = await e.get_reply_message()
    fwd = await msg.forward_to(msg.sender_id)
    await fwd.reply(message)
    await eod(e, "**Silahkan Cek di Private**", time=10)


@ayiin_cmd(pattern="getlink(?: |$)(.*)")
async def _(event):
    xx = await eor(event, "**Memprosess...**")
    try:
        e = await event.client(
            ExportChatInviteRequest(event.chat_id),
        )
        await xx.edit(f"**Tautan Undang: {e.link}**")
    except ChatAdminRequiredError:
        return await xx.edit("**Gagal Dikarenakan Bukan Admin :)**")


@ayiin_cmd(pattern="tmsg (.*)")
async def _(event):
    k = await event.get_reply_message()
    u = event.pattern_match.group(1)
    if k:
        a = await event.client.get_messages(event.chat_id, 0, from_user=k.sender_id)
        return await event.edit(f"**Total ada** `{a.total}` **Chat Yang dikirim Oleh** {u} **di Grup Chat ini**"
        )
    if not u:
        u = "me"
    a = await event.client.get_messages(event.chat_id, 0, from_user=u)
    await eor(
        event,
        f"**Total ada** `{a.total}` **Chat Yang dikirim Oleh Saya di Grup Chat ini**"
    )


@ayiin_cmd(pattern="limit(?: |$)(.*)")
async def _(event):
    xx = await eor(event, "**Memproses...**")
    async with event.client.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.client(UnblockRequest("@SpamBot"))
            await conv.send_message("/start")
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        await xx.edit(f"~ {response.message.message}")


@ayiin_cmd(pattern="view")
async def _(event):
    reply_message = await event.get_reply_message()
    if not reply_message:
        await eor(event, "**Mohon Reply ke Link**")
        return
    if not reply_message.text:
        await eor(event, "**Mohon Reply ke Link**")
        return
    chat = "@chotamreaderbot"
    xx = await eor(event, "**Memproses...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=272572121)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        if response.text.startswith(""):
            await xx.edit("Aku Bodoh Atau Anda Bodoh?")
        else:
            await xx.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "view": f"**Plugin : **`view`\
        \n\n  »  **Perintah :** `{cmd}view` <reply ke link>\
        \n  »  **Kegunaan : **Untuk Melihat isi web dengan instan view telegraph.\
    "
    }
)


CMD_HELP.update(
    {
        "open": f"**Plugin : **`open`\
        \n\n  »  **Perintah :** `{cmd}open` <reply ke file>\
        \n  »  **Kegunaan : **Untuk Melihat isi File Menjadi Text yang dikirim menjadi pesan telegram.\
    "
    }
)


CMD_HELP.update(
    {
        "dm": f"**Plugin : **`dm`\
        \n\n  »  **Perintah :** `{cmd}dm` <username> <text>\
        \n  »  **Kegunaan : **Untuk mengirim chat dengan menggunakan userbot.\
        \n\n  »  **Perintah :** `{cmd}fwdreply` <username> <text>\
        \n  »  **Kegunaan : **Untuk meneruskan chat yang di reply dengan membalasnya ke pc.\
    "
    }
)


CMD_HELP.update(
    {
        "sendbot": f"**Plugin : **`sendbot`\
        \n\n  »  **Perintah :** `{cmd}sendbot` <username bot> <text>\
        \n  »  **Kegunaan : **Untuk mengirim ke bot dan mendapatkan respond chat dengan menggunakan userbot.\
    "
    }
)


CMD_HELP.update(
    {
        "tmsg": f"**Plugin : **`tmsg`\
        \n\n  »  **Perintah :** `{cmd}tmsg` <username/me>\
        \n  »  **Kegunaan : **Untuk Menghitung total jumlah chat yang sudah dikirim.\
    "
    }
)


CMD_HELP.update(
    {
        "getlink": f"**Plugin : **`getlink`\
        \n\n  »  **Perintah :** `{cmd}getlink`\
        \n  »  **Kegunaan : **Untuk Mendapatkan link invite grup chat.\
    "
    }
)


CMD_HELP.update(
    {
        "unbanall": f"**Plugin : **`unbanall`\
        \n\n  »  **Perintah :** `{cmd}unbanall`\
        \n  »  **Kegunaan : **Untuk Menghapus Semua Pengguna yang dibanned di Daftar Banned GC.\
    "
    }
)

CMD_HELP.update(
    {
        "limit": f"**Plugin : **`limit`\
        \n\n  »  **Perintah :** `{cmd}limit`\
        \n  »  **Kegunaan : **Untuk Mengecek akun anda sedang terkena limit atau tidak dengan menggunakan @spambot.\
    "
    }
)
