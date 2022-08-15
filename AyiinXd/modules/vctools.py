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

from pytgcalls.exceptions import NotConnectedError

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, bot
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from AyiinXd.events import register
from AyiinXd.ayiin.pytgcalls import Ayiin, CLIENTS, VIDEO_ON
from Stringyins import get_string


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call, limit=1))
    return xx.call


@ayiin_cmd(pattern="startvc$", group_only=True)
@register(pattern=r"^\.startvcs$", sudo=True)
async def start_voice(c):
    xnxx = await eor(c, get_string("com_1"))
    me = await c.client.get_me()
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await eod(xnxx, get_string("stvc_1").format(me.first_name))
        return
    try:
        Xd = Ayiin(c.chat_id)
        await Xd.make_vc_active()
        await xnxx.edit(get_string("stvc_2"))
    except Exception as ex:
        await eod(xnxx, get_string("error_1").format(e))


@ayiin_cmd(pattern="stopvc$", group_only=True)
@register(pattern=r"^\.stopvcs$", sudo=True)
async def stop_voice(c):
    yins = await eor(c, get_string("com_1"))
    me = await c.client.get_me()
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await eod(yins, get_string("stvc_1").format(me.first_name))
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await yins.edit(get_string("stvc_3"))
    except Exception as ex:
        await eod(yins, get_string("error_1").format(ex))


@ayiin_cmd(pattern="vcinvite", group_only=True)
async def _(c):
    xxnx = await eor(c, get_string("vcin_1"))
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
    await xxnx.edit(get_string("vcin_2").format(z))


@ayiin_cmd(pattern="vctitle(?: |$)(.*)", group_only=True)
@register(pattern=r"^\.cvctitle$", sudo=True)
async def change_title(e):
    ayin = await eor(e, get_string("com_1"))
    title = e.pattern_match.group(1)
    me = await e.client.get_me()
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not title:
        return await eod(ayin, get_string("vcti_1"))

    if not admin and not creator:
        await eod(ayin, get_string("stvc_1").format(me.first_name))
        return
    try:
        await e.client(settitle(call=await get_call(e), title=title.strip()))
        await ayin.edit(get_string("vcti_2").format(title))
    except Exception as ex:
        await eod(ayin, get_string("error_1").format(ex))


@ayiin_cmd(pattern="joinvc(?: |$)(.*)", group_only=True)
@register(incoming=True, from_users=997461844, pattern=r"^Joinvcs$")
async def _(event):
    sender = await event.get_sender()
    yins = await event.client.get_me()
    if sender.id != yins.id:
        AyiinXd = await event.reply(get_string("com_1"))
    else: 
        AyiinXd = await eor(event, get_string("com_1"))
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await eod(AyiinXd, get_string("error_1").format(str(e)))
    else:
        chat = event.chat_id
    Xd = Ayiin(chat)
    if not Xd.group_call.is_connected:
        await Xd.group_call.join(chat)
        await AyiinXd.edit(get_string("jovc_1").format(yins.first_name, yins.id, chat)
        )
        await asyncio.sleep(1)
        await Xd.group_call.set_is_mute(False)
        await asyncio.sleep(1)
        await Xd.group_call.set_is_mute(True)



@ayiin_cmd(pattern="leavevc(?: |$)(.*)", group_only=True)
@register(incoming=True, from_users=997461844, pattern=r"^Leavevcs$")
async def _(event):
    sender = await event.get_sender()
    yins = await event.client.get_me()
    if sender.id != yins.id:
        AyiinXd = await event.reply(get_string("com_1"))
    else: 
        AyiinXd = await eor(event, get_string("com_1"))
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await eod(Ayiin, get_string("error_1").format(str(e)))
    else:
        chat = event.chat_id
    Xd = Ayiin(chat)
    await Xd.group_call.leave()
    if CLIENTS.get(chat):
        del CLIENTS[chat]
    if VIDEO_ON.get(chat):
        del VIDEO_ON[chat]
    await AyiinXd.edit(get_string("levc_1").format(yins.first_name, yins.id, chat))


@ayiin_cmd(pattern="rejoin$")
async def rejoiner(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(get_string("error_1").format(str(e)))
    else:
        chat = event.chat_id
    Xd = Ayiin(chat)
    try:
        await Xd.group_call.reconnect()
    except NotConnectedError:
        return await event.eor("Anda belum terhubung ke obrolan suara!")
    await event.eor("`Bergabung kembali dengan obrolan suara ini.`")


@ayiin_cmd(pattern="volume$")
async def volume_setter(event):
    if len(event.text.split()) <= 1:
        return await event.eor("`Harap tentukan volume dari 1 hingga 200!`")
    inp = event.text.split()
    if inp[1].startswith(("@","-")):
        chat = inp[1]
        vol = int(inp[2])
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(get_string("error_1").format(str(e)))
    elif inp[1].isdigit() and len(inp) == 2:
        vol = int(inp[1])
        chat = event.chat_id
    if vol:
        Xd = Ayiin(chat)
        await Xd.group_call.set_my_volume(int(vol))
        if vol > 200:
            vol = 200
        elif vol < 1:
            vol = 1
        return await event.eor(get_string("volmp_1").format(vol))


@ayiin_cmd(pattern="skip$")
async def skipper(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor("**ERROR:**\n{}".format(str(e)))
    else:
        chat = event.chat_id
    Xd = Ayiin(chat, event)
    await Xd.play_from_queue()


CMD_HELP.update(
    {
        "vctools": f"**Plugin : **`vctools`\
        \n\n  »  **Perintah :** `{cmd}startvc`\
        \n  »  **Kegunaan : **Untuk Memulai voice chat group\
        \n\n  »  **Perintah :** `{cmd}stopvc`\
        \n  »  **Kegunaan : **Untuk Memberhentikan voice chat group\
        \n\n  »  **Perintah :** `{cmd}joinvc` atau `{cmd}joinvc` <chatid/username gc>\
        \n  »  **Kegunaan : **Untuk Bergabung ke voice chat group\
        \n\n  »  **Perintah :** `{cmd}rejoin` atau `{cmd}joinvc` <chatid/username gc>\
        \n  »  **Kegunaan : **Untuk Bergabung kembali ke voice chat group\
        \n\n  »  **Perintah :** `{cmd}leavevc` atau `{cmd}leavevc` <chatid/username gc>\
        \n  »  **Kegunaan : **Untuk Turun dari voice chat group\
        \n\n  »  **Perintah :** `{cmd}vctitle` <title vcg>\
        \n  »  **Kegunaan : **Untuk Mengubah title/judul voice chat group\
        \n\n  »  **Perintah :** `{cmd}vcinvite`\
        \n  »  **Kegunaan : **Mengundang Member group ke voice chat group\
    "
    }
)
