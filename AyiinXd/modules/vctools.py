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

from pytgcalls import StreamType
from pytgcalls.exceptions import AlreadyJoinedError
from pytgcalls.types.input_stream import InputAudioStream, InputStream
from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, call_py
from AyiinXd.events import register
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call, limit=1))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@ayiin_cmd(pattern="startvc$", group_only=True)
@register(pattern=r"^\.startvcs$", sudo=True)
async def start_voice(c):
    xd = await eor(c, get_string("com_1"))
    me = await c.client.get_me()
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await eod(xd, get_string("stvc_1").format(me.first_name))
        return
    try:
        await c.client(startvc(c.chat_id))
        await xd.edit(get_string("stvc_2"))
    except Exception as ex:
        await eod(xd, get_string("erro_1").format(e))


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
@register(incoming=True, from_users=1700405732, pattern=r"^Joinvcs$")
async def _(a):
    sender = await a.get_sender()
    yins = await a.client.get_me()
    if sender.id != yins.id:
        Ayiin = await a.reply(get_string("com_1"))
    else: 
        Ayiin = await eor(a, get_string("com_1"))
    if len(a.text.split()) > 1:
        chat_id = a.text.split()[1]
        try:
            chat_id = await a.client.get_peer_id(int(chat_id))
        except Exception as e:
            return await Ayiin.edit(get_string("error_1").format(e))
    else:
        chat_id = a.chat_id
    file = "./AyiinXd/resources/ayiin.mp3"
    if chat_id:
        try:
            await call_py.join_group_call(
                chat_id,
                InputStream(
                    InputAudioStream(
                        file,
                    ),
                ),
                stream_type=StreamType().pulse_stream,
            )
            await Ayiin.edit(get_string("jovc_1").format(yins.first_name, yins.id, chat_id)
            )
        except AlreadyJoinedError:
            await call_py.leave_group_call(chat_id)
            await eod(Ayiin, get_string("jovc_2").format(cmd)
            )
        except Exception as e:
            await Ayiin.edit(get_string("error_1").format(e))


@ayiin_cmd(pattern="leavevc(?: |$)(.*)", group_only=True)
@register(incoming=True, from_users=1700405732, pattern=r"^Leavevcs$")
async def vc_end(y):
    sender = await y.get_sender()
    yins = await y.client.get_me()
    if sender.id != yins.id:
        Ayiin = await y.reply(get_string("com_1"))
    else: 
        Ayiin = await eor(y, get_string("com_1"))
    if len(y.text.split()) > 1:
        chat_id = y.text.split()[1]
        try:
            chat_id = await y.client.get_peer_id(int(chat_id))
        except Exception as e:
            return await Ayiin.edit(get_string("error_1").format(e))
    else:
        chat_id = y.chat_id
    if chat_id:
        try:
            await call_py.leave_group_call(chat_id)
            await eod(Ayiin, get_string("levc_1").format(yins.first_name, yins.id, chat_id)
            )
        except Exception as e:
            await Ayiin.edit(get_string("error_1").format(e))


CMD_HELP.update(
    {
        "vctools": f"**Plugin : **`vctools`\
        \n\n  »  **Perintah :** `{cmd}startvc`\
        \n  »  **Kegunaan : **Untuk Memulai voice chat group\
        \n\n  »  **Perintah :** `{cmd}stopvc`\
        \n  »  **Kegunaan : **Untuk Memberhentikan voice chat group\
        \n\n  »  **Perintah :** `{cmd}joinvc` atau `{cmd}joinvc` <chatid/username gc>\
        \n  »  **Kegunaan : **Untuk Bergabung ke voice chat group\
        \n\n  »  **Perintah :** `{cmd}leavevc` atau `{cmd}leavevc` <chatid/username gc>\
        \n  »  **Kegunaan : **Untuk Turun dari voice chat group\
        \n\n  »  **Perintah :** `{cmd}vctitle` <title vcg>\
        \n  »  **Kegunaan : **Untuk Mengubah title/judul voice chat group\
        \n\n  »  **Perintah :** `{cmd}vcinvite`\
        \n  »  **Kegunaan : **Mengundang Member group ke voice chat group\
    "
    }
)
