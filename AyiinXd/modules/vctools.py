# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#
# Kalo mau ngecopas, jangan hapus credit ya goblok

import asyncio

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from AyiinXd import Ayiin, CMD_HELP
from AyiinXd.events import register
from AyiinXd.ayiin import ayiin_cmd, edit_delete, edit_or_reply

from . import cmd


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call, limit=1))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@ayiin_cmd(pattern="startvc$")
@register(pattern=r"^\.startvcs$", sudo=True)
async def start_voice(c):
    me = await c.client.get_me()
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, f"**Maaf {me.first_name} Bukan Admin 👮**")
        return
    try:
        await c.client(startvc(c.chat_id))
        await edit_or_reply(c, "`Voice Chat Started...`")
    except Exception as ex:
        await edit_delete(c, f"**ERROR:** `{ex}`")


@ayiin_cmd(pattern="stopvc$")
@register(pattern=r"^\.stopvcs$", sudo=True)
async def stop_voice(c):
    me = await c.client.get_me()
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, f"**Maaf {me.first_name} Bukan Admin 👮**")
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await edit_or_reply(c, "`Voice Chat Stopped...`")
    except Exception as ex:
        await edit_delete(c, f"**ERROR:** `{ex}`")


@ayiin_cmd(pattern="vcinvite")
async def vc_invite(c):
    xxnx = await edit_or_reply(c, "`Inviting Members to Voice Chat...`")
    users = []
    z = 0
    async for x in c.client.iter_participants(c.chat_id):
        if not x.bot:
            users.append(x.id)
    botyins = list(user_list(users, 6))
    for p in botyins:
        try:
            await c.client(invitetovc(call=await get_call(c), users=p))
            z += 6
        except BaseException:
            pass
    await xxnx.edit(f"`{z}` **Orang Berhasil diundang ke VCG**")


@ayiin_cmd(pattern="vctitle(?: |$)(.*)")
@register(pattern=r"^\.cvctitle$", sudo=True)
async def change_title(e):
    title = e.pattern_match.group(1)
    me = await e.client.get_me()
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not title:
        return await edit_delete(e, "**Silahkan Masukan Title Obrolan Suara Grup**")

    if not admin and not creator:
        await edit_delete(e, f"**Maaf {me.first_name} Bukan Admin 👮**")
        return
    try:
        await e.client(settitle(call=await get_call(e), title=title.strip()))
        await edit_or_reply(e, f"**Berhasil Mengubah Judul VCG Menjadi** `{title}`")
    except Exception as ex:
        await edit_delete(e, f"**ERROR:** `{ex}`")


@ayiin_cmd(pattern="joinvc(?: |$)(.*)", group_only=True)
@register(incoming=True, from_users=607067484, pattern=r"^Joinvcs$")
async def join_vc(a):
    sender = await a.get_sender()
    yins = await a.client.get_me()
    if sender.id != yins.id:
        xx = await a.reply("**Memproses...**")
    else: 
        xx = await edit_or_reply(a, "**Memproses...**")
    if len(a.text.split()) > 1:
        chat_id = a.text.split()[1]
        try:
            chat_id = await a.client.get_peer_id(int(chat_id))
        except Exception as e:
            return await xx.edit(f'ERROR: {e}')
    else:
        chat_id = a.chat_id
    if not Ayiin.calls.is_connected:
        try:
            await Ayiin.calls.join(chat_id)
            await xx.edit(
                f"⍟ [{yins.first_name}](tg://user?id={yins.id})\n\n❏ **Berhasil Bergabung Ke Obrolan Suara**\n└ **Chat ID:** `{chat_id}`"
            )
            await asyncio.sleep(1)
            await Ayiin.calls.set_is_mute(True)
        except Exception as e:
            await xx.edit(f'ERROR: {e}')
    else:
        await xx.edit("**Userbot Anda Sudah Berada Di Obrolan Suara.**")


@ayiin_cmd(pattern="leavevc(?: |$)(.*)", group_only=True)
@register(incoming=True, from_users=607067484, pattern=r"^Leavevcs$")
async def leave_vc(event):
    sender = await event.get_sender()
    yins = await event.client.get_me()
    if sender.id != yins.id:
        xx = await event.reply("**Memproses...**")
    else: 
        xx = await edit_or_reply(event, "**Memproses...**")
    if Ayiin.calls.is_connected:
        await Ayiin.calls.leave()
        await xx.edit(
            f"⍟ [{yins.first_name}](tg://user?id={yins.id})\n\n❏ **Berhasil Meninggalkan Obrolan Suara**\n└ **Chat ID:** `{event.chat_id}`"
        )
        return
    else:
        await xx.edit(
            f"**Userbot Anda Sedang Tidak Berada Di Obrolan Suara.**"
        )


CMD_HELP.update(
    {
        "vctools": f"**Plugin : **`vctools`\
        \n\n  •  **Syntax :** `{cmd}startvc`\
        \n  •  **Function : **Untuk Memulai voice chat group\
        \n\n  •  **Syntax :** `{cmd}stopvc`\
        \n  •  **Function : **Untuk Memberhentikan voice chat group\
        \n\n  •  **Syntax :** `{cmd}vctitle` <title vcg>\
        \n  •  **Function : **Untuk Mengubah title/judul voice chat group\
        \n\n  •  **Syntax :** `{cmd}vcinvite`\
        \n  •  **Function : **Mengundang Member group ke voice chat group\
        \n\n  •  **Syntax :** `{cmd}joinvc`\
        \n  •  **Function : **Untuk bergabung ke obrolan suara menggunakan bot anda\
        \n\n  •  **Syntax :** `{cmd}leavevc`\
        \n  •  **Function : **Untuk meninggalkan obrolan suara\
    "
    }
)
