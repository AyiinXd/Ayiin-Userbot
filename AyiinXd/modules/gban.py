# Copyright (C) 2020 Catuserbot <https://github.com/sandy1709/catuserbot>
# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot

import asyncio
from datetime import datetime
from io import BytesIO

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import Channel

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, chataction, edit_or_reply, get_user_from_event
from AyiinXd.database.gban import add_gbanned, del_gbanned, cek_gbanned, get_gbanned
from AyiinXd.events import register

from . import DEVS, cmd, var
from .admin import BANNED_RIGHTS, UNBAN_RIGHTS


async def admin_groups(grp):
    admgroups = []
    async for dialog in grp.client.iter_dialogs():
        entity = dialog.entity
        if (
            isinstance(entity, Channel)
            and entity.megagroup
            and (entity.creator or entity.admin_rights)
        ):
            admgroups.append(entity.id)
    return admgroups


def mentionuser(name, userid):
    return f"[{name}](tg://user?id={userid})"


@ayiin_cmd(pattern="gban(?: |$)(.*)")
@register(pattern=r"^\.cgban(?: |$)(.*)", sudo=True)
async def gban(event):
    if event.fwd_from:
        return
    sender = await event.get_sender()
    me = await event.client.get_me()
    if sender.id != me.id:
        gbun = await event.reply("`Pemrosesan larangan global...`")
    else:
        gbun = await edit_or_reply(event, "`Pemrosesan larangan global...`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, gbun)
    if not user:
        return
    if user.id == (await event.client.get_me()).id:
        await gbun.edit("**𝙉𝙜𝙖𝙥𝙖𝙞𝙣 𝙉𝙜𝙚𝙂𝙗𝙖𝙣 𝘿𝙞𝙧𝙞 𝙎𝙚𝙣𝙙𝙞𝙧𝙞 𝙂𝙤𝙗𝙡𝙤𝙠 🐽**")
        return
    if user.id in DEVS:
        await gbun.edit("**Apakah Anda Gila ?.. Dia Adalah Developer Ayiin-Userbot 🤪**")
        return
    if cek_gbanned(user.id):
        await gbun.edit(
            f"**𝙎𝙞** [𝙅𝙖𝙢𝙚𝙩](tg://user?id={user.id}) **𝙄𝙣𝙞 𝙎𝙪𝙙𝙖𝙝 𝘼𝙙𝙖 𝘿𝙞 𝘿𝙖𝙛𝙩𝙖𝙧 𝙂𝘽𝙖𝙣𝙣𝙚𝙙**"
        )
    else:
        add_gbanned(user.id, user.first_name, reason)
    san = []
    san = await admin_groups(event)
    count = 0
    fiz = len(san)
    if fiz == 0:
        await gbun.edit("**𝘼𝙣𝙙𝙖 𝙏𝙞𝙙𝙖𝙠 𝙈𝙚𝙢𝙥𝙪𝙣𝙮𝙖𝙞 𝙂𝙘 𝙔𝙖𝙣𝙜 𝘼𝙣𝙙𝙖 𝘼𝙙𝙢𝙞𝙣 🥺**")
        return
    await gbun.edit(
        f"**𝙄𝙣𝙞𝙩𝙞𝙖𝙩𝙞𝙣𝙜 𝙂𝙗𝙖𝙣 𝙊𝙛 𝙏𝙝𝙚** [𝙅𝙖𝙢𝙚𝙩](tg://user?id={user.id}) **𝙄𝙣** `{len(san)}` **𝙂𝙧𝙤𝙪𝙥𝙨**"
    )
    for i in range(fiz):
        try:
            await event.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                var.BOTLOG_CHATID,
                f"**𝘼𝙣𝙙𝙖 𝙏𝙞𝙙𝙖𝙠 𝙈𝙚𝙢𝙞𝙡𝙞𝙠𝙞 𝙄𝙯𝙞𝙣 𝘽𝙖𝙣𝙣𝙚𝙙 𝘿𝙞 :**\n**𝙂𝙧𝙤𝙪𝙥 𝘾𝙝𝙖𝙩 :** `{event.chat_id}`",
            )
    end = datetime.now()
    timetaken = (end - start).seconds
    if reason:
        await gbun.edit(
            f"**\\#𝙂𝘽𝙖𝙣𝙣𝙚𝙙_𝙐𝙨𝙚𝙧//**\n\n**𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚 :** [{user.first_name}](tg://user?id={user.id})\n**𝙐𝙨𝙚𝙧 𝙄𝘿 :** `{user.id}`\n**𝘼𝙘𝙩𝙞𝙤𝙣 : 𝙂𝘽𝙖𝙣𝙣𝙚𝙙 𝙄𝙣 {count} 𝙂𝙧𝙤𝙪𝙥𝙨**\n**𝘿𝙪𝙧𝙖𝙩𝙞𝙤𝙣 𝙂𝙗𝙖𝙣𝙣𝙚𝙙 :** `{timetaken}` **𝙎𝙚𝙘𝙤𝙣𝙙𝙨**!!\n**𝙍𝙚𝙖𝙨𝙤𝙣 :** `{reason}`\n**𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 : ✧ ᴀʏɪɪɴ-ᴜsᴇʀʙᴏᴛ ✧**"
        )
    else:
        await gbun.edit(
            f"**\\#𝙂𝘽𝙖𝙣𝙣𝙚𝙙_𝙐𝙨𝙚𝙧//**\n\n**𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚 :** [{user.first_name}](tg://user?id={user.id})\n**𝙐𝙨𝙚𝙧 𝙄𝘿 :** `{user.id}`\n**𝘼𝙘𝙩𝙞𝙤𝙣 : 𝙂𝘽𝙖𝙣𝙣𝙚𝙙 𝙄𝙣 {count} 𝙂𝙧𝙤𝙪𝙥𝙨**\n**𝘿𝙪𝙧𝙖𝙩𝙞𝙤𝙣 𝙂𝙗𝙖𝙣𝙣𝙚𝙙 :** `{timetaken}` **𝙎𝙚𝙘𝙤𝙣𝙙𝙨**!!\n**𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 : ✧ ᴀʏɪɪɴ-ᴜsᴇʀʙᴏᴛ ✧**"
        )


@ayiin_cmd(pattern="ungban(?: |$)(.*)")
@register(pattern=r"^\.cungban(?: |$)(.*)", sudo=True)
async def ungban(event):
    if event.fwd_from:
        return
    sender = await event.get_sender()
    me = await event.client.get_me()
    if sender.id != me.id:
        ungbun = await event.reply("`𝙐𝙣𝙂𝙗𝙖𝙣𝙣𝙞𝙣𝙜...`")
    else:
        ungbun = await edit_or_reply(event, "`𝙐𝙣𝙂𝙗𝙖𝙣𝙣𝙞𝙣𝙜...`")
    start = datetime.now()
    user, reason = await get_user_from_event(event, ungbun)
    if not user:
        return
    if cek_gbanned(user.id):
        del_gbanned(user.id)
    else:
        await ungbun.edit(
            f"**𝙎𝙞** [𝙅𝙖𝙢𝙚𝙩](tg://user?id={user.id}) **𝙄𝙣𝙞 𝙏𝙞𝙙𝙖𝙠 𝘼𝙙𝙖 𝘿𝙖𝙡𝙖𝙢 𝘿𝙖𝙛𝙩𝙖𝙧 𝙂𝙗𝙖𝙣 𝘼𝙣𝙙𝙖**"
        )
        return
    san = []
    san = await admin_groups(event)
    count = 0
    fiz = len(san)
    if fiz == 0:
        await ungbun.edit("**𝘼𝙣𝙙𝙖 𝙏𝙞𝙙𝙖𝙠 𝙈𝙚𝙢𝙥𝙪𝙣𝙮𝙖𝙞 𝙂𝙘 𝙔𝙖𝙣𝙜 𝘼𝙣𝙙𝙖 𝘼𝙙𝙢𝙞𝙣 🥺**")
        return
    await ungbun.edit(
        f"**𝙄𝙣𝙞𝙩𝙞𝙖𝙩𝙞𝙣𝙜 𝙐𝙣𝙜𝙗𝙖𝙣 𝙊𝙛 𝙏𝙝𝙚** [𝙅𝙖𝙢𝙚𝙩](tg://user?id={user.id}) **𝙄𝙣** `{len(san)}` **𝙂𝙧𝙤𝙪𝙥**"
    )
    for i in range(fiz):
        try:
            await event.client(EditBannedRequest(san[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await event.client.send_message(
                var.BOTLOG_CHATID,
                f"**𝘼𝙣𝙙𝙖 𝙏𝙞𝙙𝙖𝙠 𝙈𝙚𝙢𝙞𝙡𝙞𝙠𝙞 𝙄𝙯𝙞𝙣 𝘽𝙖𝙣𝙣𝙚𝙙 𝘿𝙞 :**\n**𝙂𝙧𝙤𝙪𝙥 𝘾𝙝𝙖𝙩 :** `{event.chat_id}`",
            )
    end = datetime.now()
    timetaken = (end - start).seconds
    if reason:
        await ungbun.edit(
            f"**𝙐𝙣𝙂𝙗𝙖𝙣𝙣𝙚𝙙** [{user.first_name}](tg://user?id={user.id}`) **𝙄𝙣** `{count}` **𝙂𝙧𝙤𝙪𝙥𝙨 𝙄𝙣** `{timetaken}` **𝙎𝙚𝙘𝙤𝙣𝙙𝙨**!!\n**𝙍𝙚𝙖𝙨𝙤𝙣 :** `{reason}`"
        )
    else:
        await ungbun.edit(
            f"**𝙐𝙣𝙂𝙗𝙖𝙣𝙣𝙚𝙙** [{user.first_name}](tg://user?id={user.id}) **𝙄𝙣** `{count}` **𝙂𝙧𝙤𝙪𝙥𝙨 𝙄𝙣** `{timetaken}` **𝙎𝙚𝙘𝙤𝙣𝙙𝙨**!!\n**𝙍𝙚𝙢𝙤𝙫𝙚𝙙 𝙁𝙧𝙤𝙢 𝙂𝙗𝙖𝙣𝙡𝙞𝙨𝙩**"
        )


@ayiin_cmd(pattern="listgban$")
async def gablist(event):
    if event.fwd_from:
        return
    gbanned_users = get_gbanned()
    GBANNED_LIST = "**𝙇𝙞𝙨𝙩 𝙂𝙡𝙤𝙗𝙖𝙡 𝘽𝙖𝙣𝙣𝙚𝙙 𝙎𝙖𝙖𝙩 𝙄𝙣𝙞**\n\n"
    if gbanned_users:
        for a_user in gbanned_users:
            mention = mentionuser(a_user[1], a_user[0])
            if a_user[2]:
                GBANNED_LIST += f"**☞︎︎︎ User:** {mention}\n**☞︎︎︎ 𝙍𝙚𝙖𝙨𝙤𝙣:** `{a_user[2]}`\n"
            else:
                GBANNED_LIST += (
                    f"**☞︎︎︎ User:** {mention}\n**☞︎︎︎ Reason:** `No Reason`\n"
                )
        if len(GBANNED_LIST) >= 4096:
            with BytesIO(str.encode(GBANNED_LIST)) as fileuser:
                fileuser.name = "list-gban.txt"
                await event.client.send_file(
                    event.chat_id,
                    fileuser,
                    force_document=True,
                    thumb="AyiinXd/resources/logo.jpg",
                    caption="**List Global Banned**",
                    allow_cache=False,
                )
    else:
        GBANNED_LIST = "𝘽𝙚𝙡𝙪𝙢 𝘼𝙙𝙖 𝙋𝙚𝙣𝙜𝙜𝙪𝙣𝙖 𝙔𝙖𝙣𝙜 𝘿𝙞-𝙂𝙗𝙖𝙣"
    await edit_or_reply(event, GBANNED_LIST)


@chataction()
async def _(event):
    if event.user_joined or event.added_by:
        user = await event.get_user()
        chat = await event.get_chat()
        if cek_gbanned(user.id) and chat.admin_rights:
            try:
                await event.client.edit_permissions(
                    chat.id,
                    user.id,
                    view_messages=False,
                )
                await event.reply(
                    f"**#𝙂𝙗𝙖𝙣𝙣𝙚𝙙_𝙐𝙨𝙚𝙧** 𝙅𝙤𝙞𝙣𝙚𝙙.\n\n** • 𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚:** [{user.first_name}](tg://user?id={user.id})\n • **𝘼𝙘𝙩𝙞𝙤𝙣:** `Banned`"
                )
            except BaseException:
                pass


# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot


CMD_HELP.update(
    {
        "gban": f"**Plugin : **`gban`\
        \n\n  »  **Perintah :** `{cmd}gban` <username/id>\
        \n  »  **Kegunaan : **Melakukan Banned Secara Global Ke Semua Grup Dimana anda Sebagai Admin.\
        \n\n  »  **Perintah :** `{cmd}ungban` <username/id>\
        \n  »  **Kegunaan : **Membatalkan Global Banned\
        \n\n  »  **Perintah :** `{cmd}listgban`\
        \n  »  **Kegunaan : **Menampilkan List Global Banned\
    "
    }
)
