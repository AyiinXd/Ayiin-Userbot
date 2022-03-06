# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

from asyncio import sleep

from telethon.errors import (
    BadRequestError,
    ImageProcessFailedError,
    PhotoCropSizeSmallError,
)
from telethon.errors.rpcerrorlist import (
    ChatAdminRequiredError,
    UserAdminInvalidError,
    UserIdInvalidError,
)
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChatAdminRights,
    ChatBannedRights,
    InputChatPhotoEmpty,
    MessageMediaPhoto,
)

from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, DEVS, WHITELIST
from userbot.events import register
from userbot.utils import (
    _format,
    edit_delete,
    edit_or_reply,
    get_user_from_event,
    ayiin_cmd,
    ayiin_handler,
    media_type,
)
from userbot.utils.logger import logging

# =================== CONSTANT ===================
PP_TOO_SMOL = "**Gambar Terlalu Kecil**"
PP_ERROR = "**Gagal Memproses Gambar**"
NO_ADMIN = "**Gagal dikarenakan Bukan Admin :)**"
NO_PERM = "**Tidak Mempunyai Izin!**"
NO_SQL = "**Berjalan Pada Mode Non-SQL**"
CHAT_PP_CHANGED = "**Berhasil Mengubah Profil Grup**"
INVALID_MEDIA = "**Media Tidak Valid**"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


LOGS = logging.getLogger(__name__)
MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)
# ================================================


@ayiin_cmd(pattern="setgpic( -s| -d)$")
@register(pattern=r"^\.csetgpic( -s| -d)$", sudo=True)
async def set_group_photo(event):
    "For changing Group dp"
    flag = (event.pattern_match.group(1)).strip()
    if flag == "-s":
        replymsg = await event.get_reply_message()
        photo = None
        if replymsg and replymsg.media:
            if isinstance(replymsg.media, MessageMediaPhoto):
                photo = await event.client.download_media(message=replymsg.photo)
            elif "image" in replymsg.media.document.mime_type.split("/"):
                photo = await event.client.download_file(replymsg.media.document)
            else:
                return await edit_delete(event, INVALID_MEDIA)
        if photo:
            try:
                await event.client(
                    EditPhotoRequest(
                        event.chat_id, await event.client.upload_file(photo)
                    )
                )
                await edit_delete(event, CHAT_PP_CHANGED)
            except PhotoCropSizeSmallError:
                return await edit_delete(event, PP_TOO_SMOL)
            except ImageProcessFailedError:
                return await edit_delete(event, PP_ERROR)
            except Exception as e:
                return await edit_delete(event, f"**ERROR : **`{str(e)}`")
    else:
        try:
            await event.client(EditPhotoRequest(event.chat_id, InputChatPhotoEmpty()))
        except Exception as e:
            return await edit_delete(event, f"**ERROR : **`{e}`")
        await edit_delete(event, "**Foto Profil Grup Berhasil dihapus.**", 30)


@ayiin_cmd(pattern="promote(?:\\s|$)([\\s\\S]*)")
@register(pattern=r"^\.cpromote(?:\s|$)([\s\S]*)", sudo=True)
async def promote(event):
    new_rights = ChatAdminRights(
        add_admins=False,
        change_info=True,
        invite_users=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    user, rank = await get_user_from_event(event)
    if not rank:
        rank = "admin"
    if not user:
        return
    eventyins = await edit_or_reply(event, "`Promoting...`")
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
    except BadRequestError:
        return await eventyins.edit(NO_PERM)
    await edit_delete(eventyins, "`Promoted Successfully!`", 30)


@ayiin_cmd(pattern="demote(?:\\s|$)([\\s\\S]*)")
@register(pattern=r"^\.cdemote(?:\s|$)([\s\S]*)", sudo=True)
async def demote(event):
    "To demote a person in group"
    user, _ = await get_user_from_event(event)
    if not user:
        return
    eventyins = await edit_or_reply(event, "`Demoting...`")
    newrights = ChatAdminRights(
        add_admins=None,
        invite_users=None,
        change_info=None,
        ban_users=None,
        delete_messages=None,
        pin_messages=None,
        manage_call=None,
    )
    rank = "admin"
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, newrights, rank))
    except BadRequestError:
        return await eventyins.edit(NO_PERM)
    await edit_delete(eventyins, "`Demoted Successfully!`", 30)


@ayiin_cmd(pattern="ban(?:\\s|$)([\\s\\S]*)")
@register(pattern=r"^\.cban(?:\s|$)([\s\S]*)", sudo=True)
async def ban(bon):
    me = await bon.client.get_me()
    chat = await bon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await edit_or_reply(bon, NO_ADMIN)

    user, reason = await get_user_from_event(bon)
    if not user:
        return
    ayiin = await edit_or_reply(bon, "`Processing Banned...`")
    try:
        await bon.client(EditBannedRequest(bon.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        return await edit_or_reply(bon, NO_PERM)
    if reason:
        await ayiin.edit(
            bon,
            r"\\**#𝘽𝙖𝙣𝙣𝙚𝙙_𝙐𝙨𝙚𝙧**//"
            f"\n\n**𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚 :** [{user.first_name}](tg://user?id={user.id})\n"
            f"**𝙐𝙨𝙚𝙧 𝙄𝘿 :** `{str(user.id)}`\n"
            f"**𝘼𝙘𝙩𝙞𝙤𝙣 :** `𝘽𝙖𝙣𝙣𝙚𝙙 𝙐𝙨𝙚𝙧`\n"
            f"**𝙍𝙚𝙖𝙨𝙤𝙣 :** `{reason}`\n"
            f"**𝘽𝙖𝙣𝙣𝙚𝙙 𝘽𝙮 :** `{me.first_name}`\n"
            f"**𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 : ✧ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧**",
        )
    else:
        await ayiin.edit(
            bon,
            f"\\\\**#𝘽𝙖𝙣𝙣𝙚𝙙_𝙐𝙨𝙚𝙧**//"
            f"\n\n**𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚 :** [{user.first_name}](tg://user?id={user.id})\n"
            f"**𝙐𝙨𝙚𝙧 𝙄𝘿 :** `{user.id}`\n"
            f"**𝘼𝙘𝙩𝙞𝙤𝙣 :** `𝘽𝙖𝙣𝙣𝙚𝙙 𝙐𝙨𝙚𝙧`\n"
            f"**𝘽𝙖𝙣𝙣𝙚𝙙 𝘽𝙮 :** `{me.first_name}`\n"
            f"**𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 : ✧ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧**",
        )


@ayiin_cmd(pattern="unban(?:\\s|$)([\\s\\S]*)")
@register(pattern=r"^\.cunban(?:\s|$)([\s\S]*)", sudo=True)
async def nothanos(unbon):
    chat = await unbon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await edit_delete(unbon, NO_ADMIN)
    ayiin = await edit_or_reply(unbon, "`Processing...`")
    user = await get_user_from_event(unbon)
    user = user[0]
    if not user:
        return
    try:
        await unbon.client(EditBannedRequest(unbon.chat_id, user.id, UNBAN_RIGHTS))
        await edit_delete(ayiin, "`Unban Berhasil Dilakukan!`")
    except UserIdInvalidError:
        await edit_delete(ayiin, "`Sepertinya Terjadi ERROR!`")


@ayiin_cmd(pattern="mute(?: |$)(.*)")
@register(pattern=r"^\.cmute(?: |$)(.*)", sudo=True)
async def spider(spdr):
    try:
        from userbot.modules.sql_helper.spam_mute_sql import mute
    except AttributeError:
        return await edit_or_reply(spdr, NO_SQL)
    chat = await spdr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await edit_or_reply(spdr, NO_ADMIN)
    user, reason = await get_user_from_event(spdr)
    if not user:
        return
    self_user = await spdr.client.get_me()
    if user.id == self_user.id:
        return await edit_or_reply(
            ayiin, "**Tidak Bisa Membisukan Diri Sendiri..（>﹏<）**"
        )
    if user.id in DEVS:
        return await ayiin.edit("**Gagal Mute, dia adalah Pembuat Saya 🤪**")
    if user.id in WHITELIST:
        return await ayiin.edit("**Gagal Mute, dia adalah admin suhu udara 🤪**")
    await ayiin.edit(
        r"\\**#𝙈𝙪𝙩𝙚𝙙_𝙐𝙨𝙚𝙧**//"
        f"\n\n**𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚 :** [{user.first_name}](tg://user?id={user.id})\n"
        f"**𝙐𝙨𝙚𝙧 𝙄𝘿 :** `{user.id}`\n"
        f"**𝘼𝙘𝙩𝙞𝙤𝙣 :** `𝙈𝙪𝙩𝙚𝙙 𝙐𝙨𝙚𝙧`\n"
        f"**𝙈𝙪𝙩𝙚𝙙 𝘽𝙮 :** `{self_user.first_name}`\n"
        f"**𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 : ✧ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧**"
    )
    if mute(spdr.chat_id, user.id) is False:
        return await edit_delete(ayiin, "**ERROR:** `Pengguna Sudah Dibisukan.`")
    try:
        await spdr.client(EditBannedRequest(spdr.chat_id, user.id, MUTE_RIGHTS))
        if reason:
            await ayiin.edit(
                r"\\**#𝙈𝙪𝙩𝙚𝙙_𝙐𝙨𝙚𝙧**//"
                f"\n\n**𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚 :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**𝙐𝙨𝙚𝙧 𝙄𝘿 :** `{user.id}`\n"
                f"**𝙍𝙚𝙖𝙨𝙤𝙣 :** `{reason}`\n"
                f"**𝙈𝙪𝙩𝙚𝙙 𝘽𝙮 :** `{self_user.first_name}`\n"
                f"**𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 : ✧ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧**"
            )
        else:
            await ayiin.edit(
                r"\\**#𝙈𝙪𝙩𝙚𝙙_𝙐𝙨𝙚𝙧**//"
                f"\n\n**𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚 :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**𝙐𝙨𝙚𝙧 𝙄𝘿 :** `{user.id}`\n"
                f"**𝘼𝙘𝙩𝙞𝙤𝙣 :** `𝙈𝙪𝙩𝙚𝙙 𝙐𝙨𝙚𝙧`\n"
                f"**𝙈𝙪𝙩𝙚𝙙 𝘽𝙮 :** `{self_user.first_name}`\n"
                f"**𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 : ✧ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧**"
            )
    except UserIdInvalidError:
        return await edit_delete(ayiin, "**Terjadi ERROR!**")


@ayiin_cmd(pattern="unmute(?: |$)(.*)")
@register(pattern=r"^\.cunmute(?: |$)(.*)", sudo=True)
async def unmoot(unmot):
    chat = await unmot.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await edit_delete(unmot, NO_ADMIN)
    try:
        from userbot.modules.sql_helper.spam_mute_sql import unmute
    except AttributeError:
        return await unmot.edit(NO_SQL)
    ayiin = await edit_or_reply(unmot, "`Processing...`")
    user = await get_user_from_event(unmot)
    user = user[0]
    if not user:
        return

    if unmute(unmot.chat_id, user.id) is False:
        return await edit_delete(unmot, "**ERROR! Pengguna Sudah Tidak Dibisukan.**")
    try:
        await unmot.client(EditBannedRequest(unmot.chat_id, user.id, UNBAN_RIGHTS))
        await edit_delete(ayiin, "**Berhasil Melakukan Unmute!**")
    except UserIdInvalidError:
        return await edit_delete(ayiin, "**Terjadi ERROR!**")


@ayiin_handler()
async def muter(moot):
    try:
        from userbot.modules.sql_helper.gmute_sql import is_gmuted
        from userbot.modules.sql_helper.spam_mute_sql import is_muted
    except AttributeError:
        return
    muted = is_muted(moot.chat_id)
    gmuted = is_gmuted(moot.sender_id)
    rights = ChatBannedRights(
        until_date=None,
        send_messages=True,
        send_media=True,
        send_stickers=True,
        send_gifs=True,
        send_games=True,
        send_inline=True,
        embed_links=True,
    )
    if muted:
        for i in muted:
            if str(i.sender) == str(moot.sender_id):
                await moot.delete()
                await moot.client(
                    EditBannedRequest(moot.chat_id, moot.sender_id, rights)
                )
    for i in gmuted:
        if i.sender == str(moot.sender_id):
            await moot.delete()


@ayiin_cmd(pattern="ungmute(?: |$)(.*)")
@register(pattern=r"^\.cungmute(?: |$)(.*)", sudo=True)
async def ungmoot(un_gmute):
    chat = await un_gmute.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await edit_delete(un_gmute, NO_ADMIN)
    try:
        from userbot.modules.sql_helper.gmute_sql import ungmute
    except AttributeError:
        return await edit_delete(un_gmute, NO_SQL)
    ayiin = await edit_or_reply(un_gmute, "`Processing...`")
    user = await get_user_from_event(un_gmute)
    user = user[0]
    if not user:
        return
    await ayiin.edit("`Membuka Global Mute Pengguna...`")
    if ungmute(user.id) is False:
        await ayiin.edit("**ERROR!** Pengguna Sedang Tidak Di Gmute.")
    else:
        await edit_delete(un_gmute, "**Berhasil! Pengguna Sudah Tidak Dibisukan**")


@ayiin_cmd(pattern="gmute(?: |$)(.*)")
@register(pattern=r"^\.cgmute(?: |$)(.*)", sudo=True)
async def gspider(gspdr):
    chat = await gspdr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await edit_delete(gspdr, NO_ADMIN)
    try:
        from userbot.modules.sql_helper.gmute_sql import gmute
    except AttributeError:
        return await gspdr.edit(NO_SQL)
    ayiin = await edit_or_reply(gspdr, "`Processing...`")
    user, reason = await get_user_from_event(gspdr)
    if not user:
        return
    self_user = await gspdr.client.get_me()
    if user.id == self_user.id:
        return await ayiin.edit("**Tidak Bisa Membisukan Diri Sendiri..（>﹏<）**")
    if user.id in DEVS:
        return await ayiin.edit("**Gagal Global Mute, Dia Adalah Pembuat Saya 🤪**")
    if user.id in WHITELIST:
        return await ayiin.edit("**Gagal Mute, dia adalah suhu cuaca 🤪**")
    await ayiin.edit("**Berhasil Membisukan Pengguna!**")
    if gmute(user.id) is False:
        await edit_delete(gspdr, "**ERROR! Pengguna Sudah Dibisukan.**")
    elif reason:
        await ayiin.edit(
            r"\\**#𝙂𝙈𝙪𝙩𝙚𝙙_𝙐𝙨𝙚𝙧**//"
            f"\n\n**𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚 :** [{user.first_name}](tg://user?id={user.id})\n"
            f"**𝙐𝙨𝙚𝙧 𝙄𝘿 :** `{user.id}`\n"
            f"**𝙍𝙚𝙖𝙨𝙤𝙣 :** `{reason}`\n"
            f"**𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 : ✧ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧**"
        )
    else:
        await ayiin.edit(
            r"\\**#𝙂𝙢𝙪𝙩𝙚𝙙_𝙐𝙨𝙚𝙧**//"
            f"\n\n**𝙁𝙞𝙧𝙨𝙩 𝙉𝙖𝙢𝙚 :** [{user.first_name}](tg://user?id={user.id})\n"
            f"**𝙐𝙨𝙚𝙧 𝙄𝘿:** `{user.id}`\n"
            f"**𝘼𝙘𝙩𝙞𝙤𝙣 :** `𝙂𝙡𝙤𝙗𝙖𝙡 𝙈𝙪𝙩𝙚𝙙`\n"
            f"**𝙂𝙢𝙪𝙩𝙚𝙙 𝘽𝙮 :** `{self_user.first_name}`\n"
            f"**𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 : ✧ 𝙰𝚈𝙸𝙸𝙽-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧**"
        )


@ayiin_cmd(pattern="zombies(?: |$)(.*)")
async def rm_deletedacc(show):
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "**Grup Bersih, Tidak Menemukan Akun Terhapus.**"
    if con != "clean":
        await show.edit("`Mencari Akun Depresi...`")
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = (
                f"**Menemukan** `{del_u}` **Akun Depresi/Terhapus/Zombie Dalam Grup Ini,**"
                f"\n**Bersihkan Itu Menggunakan Perintah** `{cmd}zombies clean`"
            )
        return await show.edit(del_status)
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await show.edit("**Maaf Kamu Bukan Admin!**")
    await show.edit("`Menghapus Akun Depresi...`")
    del_u = 0
    del_a = 0
    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                return await show.edit("`Tidak Memiliki Izin Banned Dalam Grup Ini`")
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await show.client(EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1
    if del_u > 0:
        del_status = f"**Membersihkan** `{del_u}` **Akun Terhapus**"
    if del_a > 0:
        del_status = (
            f"**Membersihkan** `{del_u}` **Akun Terhapus** "
            f"\n`{del_a}` **Akun Admin Yang Terhapus Tidak Dihapus.**"
        )
    await show.edit(del_status)
    await sleep(2)
    await show.delete()
    if BOTLOG_CHATID:
        await show.client.send_message(
            BOTLOG_CHATID,
            "**#ZOMBIES**\n"
            f"**Membersihkan** `{del_u}` **Akun Terhapus!**"
            f"\n**GRUP:** {show.chat.title}(`{show.chat_id}`)",
        )


@ayiin_cmd(pattern="admins$")
async def get_admin(show):
    info = await show.client.get_entity(show.chat_id)
    title = info.title or "Grup Ini"
    mentions = f"<b>♕︎ Daftar Admin Grup {title}:</b> \n"
    try:
        async for user in show.client.iter_participants(
            show.chat_id, filter=ChannelParticipantsAdmins
        ):
            if not user.deleted:
                link = f'<a href="tg://user?id={user.id}">{user.first_name}</a>'
                mentions += f"\n✧ {link}"
            else:
                mentions += f"\n⍟ Akun Terhapus <code>{user.id}</code>"
    except ChatAdminRequiredError as err:
        mentions += f" {str(err)}" + "\n"
    await show.edit(mentions, parse_mode="html")


@ayiin_cmd(pattern="pin( loud|$)")
@register(pattern=r"^\.cpin( loud|$)", sudo=True)
async def pin(event):
    to_pin = event.reply_to_msg_id
    if not to_pin:
        return await edit_delete(event, "`Reply Pesan untuk Melakukan Pin.`", 30)
    options = event.pattern_match.group(1)
    is_silent = bool(options)
    try:
        await event.client.pin_message(event.chat_id, to_pin, notify=is_silent)
    except BadRequestError:
        return await edit_delete(event, NO_PERM, 5)
    except Exception as e:
        return await edit_delete(event, f"`{e}`", 5)
    await edit_delete(event, "`Pinned Successfully!`")


@ayiin_cmd(pattern="unpin( all|$)")
@register(pattern=r"^\.cunpin( all|$)", sudo=True)
async def pin(event):
    to_unpin = event.reply_to_msg_id
    options = (event.pattern_match.group(1)).strip()
    if not to_unpin and options != "all":
        return await edit_delete(
            event,
            f"**Reply ke Pesan untuk melepas Pin atau Gunakan** `{cmd}unpin all` **untuk melepas pin semua**",
            45,
        )
    try:
        if to_unpin and not options:
            await event.client.unpin_message(event.chat_id, to_unpin)
        elif options == "all":
            await event.client.unpin_message(event.chat_id)
        else:
            return await edit_delete(
                event,
                f"**Reply ke Pesan untuk melepas pin atau gunakan** `{cmd}unpin all`",
                45,
            )
    except BadRequestError:
        return await edit_delete(event, NO_PERM, 5)
    except Exception as e:
        return await edit_delete(event, f"`{e}`", 5)
    await edit_delete(event, "`Unpinned Successfully!`")


@ayiin_cmd(pattern="kick(?: |$)(.*)")
@register(pattern=r"^\.ckick(?: |$)(.*)", sudo=True)
async def kick(usr):
    chat = await usr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await edit_delete(usr, NO_ADMIN)
    user, reason = await get_user_from_event(usr)
    if not user:
        return await edit_delete(usr, "**Tidak Dapat Menemukan Pengguna.**")
    xxnx = await edit_or_reply(usr, "`Processing...`")
    try:
        await usr.client.kick_participant(usr.chat_id, user.id)
        await sleep(0.5)
    except Exception as e:
        return await edit_delete(usr, f"{NO_PERM}\n{e}")
    if reason:
        await xxnx.edit(
            f"[{user.first_name}](tg://user?id={user.id}) **Telah Dikick Dari Grup**\n**Alasan:** `{reason}`"
        )
    else:
        await xxnx.edit(
            f"[{user.first_name}](tg://user?id={user.id}) **Telah Dikick Dari Grup**",
        )


@ayiin_cmd(pattern=r"undlt( -u)?(?: |$)(\d*)?")
async def _iundlt(event):
    catevent = await edit_or_reply(event, "`Searching recent actions...`")
    flag = event.pattern_match.group(1)
    if event.pattern_match.group(2) != "":
        lim = int(event.pattern_match.group(2))
        if lim > 15:
            lim = int(15)
        if lim <= 0:
            lim = int(1)
    else:
        lim = int(5)
    adminlog = await event.client.get_admin_log(
        event.chat_id, limit=lim, edit=False, delete=True
    )
    deleted_msg = f"**{lim} Pesan yang dihapus di grup ini:**"
    if not flag:
        for msg in adminlog:
            ruser = (
                await event.client(GetFullUserRequest(msg.old.from_id.user_id))
            ).user
            _media_type = media_type(msg.old)
            if _media_type is None:
                deleted_msg += f"\n☞ __{msg.old.message}__ **Dikirim oleh** {_format.mentionuser(ruser.first_name ,ruser.id)}"
            else:
                deleted_msg += f"\n☞ __{_media_type}__ **Dikirim oleh** {_format.mentionuser(ruser.first_name ,ruser.id)}"
        await edit_or_reply(catevent, deleted_msg)
    else:
        main_msg = await edit_or_reply(catevent, deleted_msg)
        for msg in adminlog:
            ruser = (
                await event.client(GetFullUserRequest(msg.old.from_id.user_id))
            ).user
            _media_type = media_type(msg.old)
            if _media_type is None:
                await main_msg.reply(
                    f"{msg.old.message}\n**Dikirim oleh** {_format.mentionuser(ruser.first_name ,ruser.id)}"
                )
            else:
                await main_msg.reply(
                    f"{msg.old.message}\n**Dikirim oleh** {_format.mentionuser(ruser.first_name ,ruser.id)}",
                    file=msg.old.media,
                )


CMD_HELP.update(
    {
        "admin": f"**Plugin : **`admin`\
        \n\n  •  **Syntax :** `{cmd}promote <username/reply> <nama title (optional)>`\
        \n  •  **Function : **Mempromosikan member sebagai admin.\
        \n\n  •  **Syntax :** `{cmd}demote <username/balas ke pesan>`\
        \n  •  **Function : **Menurunkan admin sebagai member.\
        \n\n  •  **Syntax :** `{cmd}ban <username/balas ke pesan> <alasan (optional)>`\
        \n  •  **Function : **Membanned Pengguna dari grup.\
        \n\n  •  **Syntax :** `{cmd}unban <username/reply>`\
        \n  •  **Function : **Unbanned pengguna jadi bisa join grup lagi.\
        \n\n  •  **Syntax :** `{cmd}mute <username/reply> <alasan (optional)>`\
        \n  •  **Function : **Membisukan Seseorang Di Grup, Bisa Ke Admin Juga.\
        \n\n  •  **Syntax :** `{cmd}unmute <username/reply>`\
        \n  •  **Function : **Membuka bisu orang yang dibisukan.\
        \n  •  **Function : ** Membuka global mute orang yang dibisukan.\
        \n\n  •  **Syntax :** `{cmd}all`\
        \n  •  **Function : **Tag semua member dalam grup.\
        \n\n  •  **Syntax :** `{cmd}admins`\
        \n  •  **Function : **Melihat daftar admin di grup.\
        \n\n  •  **Syntax :** `{cmd}setgpic <flags> <balas ke gambar>`\
        \n  •  **Function : **Untuk mengubah foto profil grup atau menghapus gambar foto profil grup.\
        \n  •  **Flags :** `-s` = **Untuk mengubah foto grup** atau `-d` = **Untuk menghapus foto grup**\
    "
    }
)


CMD_HELP.update(
    {
        "pin": f"**Plugin : **`pin`\
        \n\n  •  **Syntax :** `{cmd}pin` <reply chat>\
        \n  •  **Function : **Untuk menyematkan pesan dalam grup.\
        \n\n  •  **Syntax :** `{cmd}pin loud` <reply chat>\
        \n  •  **Function : **Untuk menyematkan pesan dalam grup (tanpa notifikasi) / menyematkan secara diam diam.\
        \n\n  •  **Syntax :** `{cmd}unpin` <reply chat>\
        \n  •  **Function : **Untuk melepaskan pin pesan dalam grup.\
        \n\n  •  **Syntax :** `{cmd}unpin all`\
        \n  •  **Function : **Untuk melepaskan semua sematan pesan dalam grup.\
    "
    }
)


CMD_HELP.update(
    {
        "undelete": f"**Plugin : **`undelete`\
        \n\n  •  **Syntax :** `{cmd}undlt` <jumlah chat>\
        \n  •  **Function : **Untuk mendapatkan pesan yang dihapus baru-baru ini di grup\
        \n\n  •  **Syntax :** `{cmd}undlt -u` <jumlah chat>\
        \n  •  **Function : **Untuk mendapatkan pesan media yang dihapus baru-baru ini di grup \
        \n  •  **Flags :** `-u` = **Gunakan flags ini untuk mengunggah media.**\
        \n\n  •  **NOTE : Membutuhkan Hak admin Grup** \
    "
    }
)


CMD_HELP.update(
    {
        "gmute": f"**Plugin : **`gmute`\
        \n\n  •  **Syntax :** `{cmd}gmute` <username/reply> <alasan (optional)>\
        \n  •  **Function : **Untuk Membisukan Pengguna di semua grup yang kamu admin.\
        \n\n  •  **Syntax :** `{cmd}ungmute` <username/reply>\
        \n  •  **Function : **Untuk Membuka global mute Pengguna di semua grup yang kamu admin.\
    "
    }
)


CMD_HELP.update(
    {
        "zombies": f"**Plugin : **`zombies`\
        \n\n  •  **Syntax :** `{cmd}zombies`\
        \n  •  **Function : **Untuk mencari akun terhapus dalam grup\
        \n\n  •  **Syntax :** `{cmd}zombies clean`\
        \n  •  **Function : **untuk menghapus Akun Terhapus dari grup.\
    "
    }
)
