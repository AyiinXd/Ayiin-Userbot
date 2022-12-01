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

from AyiinXd import BOTLOG_CHATID
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, DEVS, WHITELIST
from AyiinXd.events import register
from AyiinXd.ayiin import (
    _format,
    eod,
    eor,
    get_user_from_event,
    ayiin_cmd,
    ayiin_handler,
    media_type,
)
from AyiinXd.ayiin.logger import logging

from Stringyins import get_string


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


@ayiin_cmd(pattern="setgpic( -s| -d)$", group_only=True)
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
                return await eor(event, get_string("inv_med"), time=10)
        if photo:
            try:
                await event.client(
                    EditPhotoRequest(
                        event.chat_id, await event.client.upload_file(photo)
                    )
                )
                await eor(event, get_string("ch_ppch"), time=10)
            except PhotoCropSizeSmallError:
                return await eor(event, get_string("pto_sml"), time=10)
            except ImageProcessFailedError:
                return await eor(event, get_string("pp_eror"), time=10)
            except Exception as e:
                return await eor(event, get_string("error_1").format(e))
    else:
        try:
            await event.client(EditPhotoRequest(event.chat_id, InputChatPhotoEmpty()))
        except Exception as e:
            return await eor(event, get_string("error_1").format(e))
        await eor(event, get_string("sgp_1", time=30))


@ayiin_cmd(pattern="promote(?:\\s|$)([\\s\\S]*)", group_only=True)
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
    await eor(event, get_string("prom_1"))
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
    except BadRequestError:
        return await eod(event, get_string("no_perm"))
    await eor(event, get_string("prom_2"), time=30)


@ayiin_cmd(pattern="demote(?:\\s|$)([\\s\\S]*)", group_only=True)
@register(pattern=r"^\.cdemote(?:\s|$)([\s\S]*)", sudo=True)
async def demote(event):
    "To demote a person in group"
    user, _ = await get_user_from_event(event)
    if not user:
        return
    await eor(event, get_string("`deot_1"))
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
        return await eor(event, get_string("no_perm"))
    await eor(event, get_string("deot_2"), time=30)


@ayiin_cmd(pattern="ban(?:\\s|$)([\\s\\S]*)", group_only=True)
@register(pattern=r"^\.cban(?:\s|$)([\s\S]*)", sudo=True)
async def ban(bon):
    me = await bon.client.get_me()
    chat = await bon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await eor(bon, get_string("no_admn"))

    user, reason = await get_user_from_event(bon)
    if not user:
        return
    ayiin = await eor(bon, get_string("band_1"))
    try:
        await bon.client(EditBannedRequest(bon.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        return await eor(bon, get_string("no_perm"))
    if reason:
        await ayiin.edit(get_string("band_2").format(user.first_name, user.id, str(user.id), reason, me.first_name))
    else:
        await ayiin.edit(get_string("band_2").format(user.first_name, user.id, str(user.id), reason, me.first_name)
                         )


@ayiin_cmd(pattern="unban(?:\\s|$)([\\s\\S]*)", group_only=True)
@register(pattern=r"^\.cunban(?:\s|$)([\s\S]*)", sudo=True)
async def nothanos(unbon):
    chat = await unbon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await eor(unbon, get_string("no_admn"))
    await eor(unbon, get_string("com_1"))
    user = await get_user_from_event(unbon)
    user = user[0]
    if not user:
        return
    try:
        await unbon.client(EditBannedRequest(unbon.chat_id, user.id, UNBAN_RIGHTS))
        await eor(unbon, get_string("band_4"), time=10)
    except UserIdInvalidError:
        await eor(unbon, get_string("band_5"), time=10)


@ayiin_cmd(pattern="mute(?: |$)(.*)", group_only=True)
@register(pattern=r"^\.cmute(?: |$)(.*)", sudo=True)
async def spider(spdr):
    try:
        from AyiinXd.modules.sql_helper.spam_mute_sql import mute
    except AttributeError:
        return await eor(spdr, get_string("not_sql"))
    chat = await spdr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await eor(spdr, get_string("no_admn"))
    user, reason = await get_user_from_event(spdr)
    if not user:
        return
    self_user = await spdr.client.get_me()
    if user.id == self_user.id:
        return await eor(spdr, get_string("mute_1"))
    if user.id in DEVS:
        return await eor(spdr, get_string("mute_2"))
    if user.id in WHITELIST:
        return await spdr.edit(get_string("mute_3"))
    await eor(spdr, get_string("mute_4").format(user.first_name, user.id, user.id, self_user.first_name)
                     )
    if mute(spdr.chat_id, user.id) is False:
        return await eor(spdr, get_string("mute_7"))
    try:
        await spdr.client(EditBannedRequest(spdr.chat_id, user.id, MUTE_RIGHTS))
        if reason:
            await eor(spdr, get_string("mute_5").format(user.first_name, user.id, user.id, reason, self_user.first_name)
                             )
        else:
            await eor(spdr, get_string("mute_6").format(user.first_name, user.id, user.id, self_user.first_name)
                             )
    except UserIdInvalidError:
        return await eor(spdr, get_string("error_2"), time=10)


@ayiin_cmd(pattern="unmute(?: |$)(.*)", group_only=True)
@register(pattern=r"^\.cunmute(?: |$)(.*)", sudo=True)
async def unmoot(unmot):
    chat = await unmot.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await eor(unmot, get_string("no_admn"), time=10)
    try:
        from AyiinXd.modules.sql_helper.spam_mute_sql import unmute
    except AttributeError:
        return await eor(unmot, get_string("not_sql"))
    await eor(unmot, get_string("com_1"))
    user = await get_user_from_event(unmot)
    user = user[0]
    if not user:
        return

    if unmute(unmot.chat_id, user.id) is False:
        return await eor(unmot, get_string("unmt_1"))
    try:
        await unmot.client(EditBannedRequest(unmot.chat_id, user.id, UNBAN_RIGHTS))
        await eor(unmot, get_string("unmt_2"))
    except UserIdInvalidError:
        return await eor(unmot, get_string("error_2"))


@ayiin_handler()
async def muter(moot):
    try:
        from AyiinXd.modules.sql_helper.gmute_sql import is_gmuted
        from AyiinXd.modules.sql_helper.spam_mute_sql import is_muted
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


@ayiin_cmd(pattern="ungmute(?: |$)(.*)", group_only=True)
@register(pattern=r"^\.cungmute(?: |$)(.*)", sudo=True)
async def ungmoot(un_gmute):
    chat = await un_gmute.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await eor(un_gmute, get_string("no_admn"), time=10)
    try:
        from AyiinXd.modules.sql_helper.gmute_sql import ungmute
    except AttributeError:
        return await eor(un_gmute, get_string("not_sql"), time=10)
    ayiin = await eor(un_gmute, get_string("com_1"))
    user = await get_user_from_event(un_gmute)
    user = user[0]
    if not user:
        return
    await ayiin.edit(get_string("ungm_1"))
    if ungmute(user.id) is False:
        await ayiin.edit(get_string("ungm_2"))
    else:
        await eor(un_gmute, get_string("ungm_3"), time=10)


@ayiin_cmd(pattern="gmute(?: |$)(.*)", group_only=True)
@register(pattern=r"^\.cgmute(?: |$)(.*)", sudo=True)
async def gspider(gspdr):
    chat = await gspdr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await eor(gspdr, get_string("no_admn"), time=10)
    try:
        from AyiinXd.modules.sql_helper.gmute_sql import gmute
    except AttributeError:
        return await gspdr.edit(get_string("not_sql"), time=10)
    ayiin = await eor(gspdr, get_string("com_1"))
    user, reason = await get_user_from_event(gspdr)
    if not user:
        return
    self_user = await gspdr.client.get_me()
    if user.id == self_user.id:
        return await ayiin.edit(get_string("mute_1"))
    if user.id in DEVS:
        return await ayiin.edit(get_string("gmut_1"))
    if user.id in WHITELIST:
        return await ayiin.edit(get_string("gmut_2"))
    await ayiin.edit(get_string("gmut_3"))
    if gmute(user.id) is False:
        await eor(gspdr, get_string("gmut_4"))
    elif reason:
        await ayiin.edit(get_string("gmut_5").format(user.first_name, user.id, user.id, reason, self_user.first_name)
                         )
    else:
        await ayiin.edit(get_string("gmut_6").format(user.first_name, user.id, user.id, self_user.first_name)
                         )


@ayiin_cmd(pattern="zombies(?: |$)(.*)", group_only=True)
async def rm_deletedacc(show):
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = get_string("zomb_1")
    if con != "clean":
        await eor(show, get_string("zomb_2"))
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
                await sleep(1)
        if del_u > 0:
            del_status = get_string("zomb_3").format(del_u, cmd)
        return await show.edit(del_status)
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await eor(show, get_string("zomb_4"))
    await eor(show, get_string("zomb_5"))
    del_u = 0
    del_a = 0
    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                return await eor(show, get_string("zomb_6"))
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await show.client(EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1
    if del_u > 0:
        del_status = get_string("zomb_7").format(del_u)
    if del_a > 0:
        del_status = get_string("zomb_8").format(del_u, del_a)
    await show.edit(del_status)
    await sleep(2)
    await show.delete()
    if BOTLOG_CHATID:
        await show.client.send_message(
            BOTLOG_CHATID, get_string("zomb_9").format(del_u, show.chat.title, show.chat_id)
        )


@ayiin_cmd(pattern="admins$", group_only=True)
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
        return await eor(event, get_string("pinn_1"), time=30)
    options = event.pattern_match.group(1)
    is_silent = bool(options)
    try:
        await event.client.pin_message(event.chat_id, to_pin, notify=is_silent)
    except BadRequestError:
        return await eod(event, get_string("no_perm"), time=5)
    except Exception as e:
        return await eod(event, get_string("error_1").format(e), time=5)
    await eor(event, get_string("pinn_2"))


@ayiin_cmd(pattern="unpin( all|$)")
@register(pattern=r"^\.cunpin( all|$)", sudo=True)
async def pin(event):
    to_unpin = event.reply_to_msg_id
    options = (event.pattern_match.group(1)).strip()
    if not to_unpin and options != "all":
        return await eor(event, get_string("upin_1").format(cmd), time=20,
                               )
    try:
        if to_unpin and not options:
            await event.client.unpin_message(event.chat_id, to_unpin)
        elif options == "all":
            await event.client.unpin_message(event.chat_id)
        else:
            return await eor(event, get_string("upin_2").format(cmd), time=20,
                             )
    except BadRequestError:
        return await eor(event, get_string("no_perm"), time=10)
    except Exception as e:
        return await eor(event, get_string("error_1").format(e), time=10)
    await eor(event, get_string("upin_3"))


@ayiin_cmd(pattern="kick(?: |$)(.*)", group_only=True)
@register(pattern=r"^\.ckick(?: |$)(.*)", sudo=True)
async def kick(usr):
    chat = await usr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        return await eor(usr, get_string("no_admn"))
    user, reason = await get_user_from_event(usr)
    if not user:
        return await eor(usr, get_string("kick_1"))
    xxnx = await eor(usr, get_string("com_1"))
    try:
        await usr.client.kick_participant(usr.chat_id, user.id)
        await sleep(0.5)
    except Exception as e:
        noperm = get_string("no_perm") + "\n" + e
        return await eod(usr, noperm)
    if reason:
        await xxnx.edit(get_string("kick_2").format(user.first_name, user.id, reason)
                        )
    else:
        await xxnx.edit(get_string("kick_3").format(user.first_name, user.id)
                        )


@ayiin_cmd(pattern=r"undlt( -u)?(?: |$)(\d*)?")
async def _iundlt(event):
    catevent = await eor(event, get_string("undl_1"))
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
    deleted_msg = get_string("undl_2").format(lim)
    if not flag:
        for msg in adminlog:
            ruser = (
                await event.client(GetFullUserRequest(msg.old.from_id.user_id))
            ).user
            _media_type = media_type(msg.old)
            if _media_type is None:
                deleted_msg += get_string("undl_3").format(
                    msg.old.message, _format.mentionuser(
                        ruser.first_name, ruser.id))
            else:
                deleted_msg += get_string("undl_3").format(_media_type, _format.mentionuser(ruser.first_name, ruser.id))
        await eor(catevent, deleted_msg)
    else:
        main_msg = await eor(catevent, deleted_msg)
        for msg in adminlog:
            ruser = (
                await event.client(GetFullUserRequest(msg.old.from_id.user_id))
            ).user
            _media_type = media_type(msg.old)
            if _media_type is None:
                await main_msg.reply(get_string("undl_4").format(msg.old.message, _format.mentionuser(ruser.first_name, ruser.id))
                                     )
            else:
                await main_msg.reply(get_string("undl_4").format(msg.old.message, _format.mentionuser(ruser.first_name, ruser.id)),
                                     file=msg.old.media,
                                     )


CMD_HELP.update(
    {
        "admin": f"**Plugin : **`admin`\
        \n\n  »  **Perintah :** `{cmd}promote <username/reply> <nama title (optional)>`\
        \n  »  **Kegunaan : **Mempromosikan member sebagai admin.\
        \n\n  »  **Perintah :** `{cmd}demote <username/balas ke pesan>`\
        \n  »  **Kegunaan : **Menurunkan admin sebagai member.\
        \n\n  »  **Perintah :** `{cmd}ban <username/balas ke pesan> <alasan (optional)>`\
        \n  »  **Kegunaan : **Membanned Pengguna dari grup.\
        \n\n  »  **Perintah :** `{cmd}unban <username/reply>`\
        \n  »  **Kegunaan : **Unbanned pengguna jadi bisa join grup lagi.\
        \n\n  »  **Perintah :** `{cmd}mute <username/reply> <alasan (optional)>`\
        \n  »  **Kegunaan : **Membisukan Seseorang Di Grup, Bisa Ke Admin Juga.\
        \n\n  »  **Perintah :** `{cmd}unmute <username/reply>`\
        \n  »  **Kegunaan : **Membuka bisu orang yang dibisukan.\
        \n  »  **Kegunaan : ** Membuka global mute orang yang dibisukan.\
        \n\n  »  **Perintah :** `{cmd}all`\
        \n  »  **Kegunaan : **Tag semua member dalam grup.\
        \n\n  »  **Perintah :** `{cmd}admins`\
        \n  »  **Kegunaan : **Melihat daftar admin di grup.\
        \n\n  »  **Perintah :** `{cmd}setgpic <flags> <balas ke gambar>`\
        \n  »  **Kegunaan : **Untuk mengubah foto profil grup atau menghapus gambar foto profil grup.\
        \n  •  **Flags :** `-s` = **Untuk mengubah foto grup** atau `-d` = **Untuk menghapus foto grup**\
    "
    }
)


CMD_HELP.update(
    {
        "pin": f"**Plugin : **`pin`\
        \n\n  »  **Perintah :** `{cmd}pin` <reply chat>\
        \n  »  **Kegunaan : **Untuk menyematkan pesan dalam grup.\
        \n\n  »  **Perintah :** `{cmd}pin loud` <reply chat>\
        \n  »  **Kegunaan : **Untuk menyematkan pesan dalam grup (tanpa notifikasi) / menyematkan secara diam diam.\
        \n\n  »  **Perintah :** `{cmd}unpin` <reply chat>\
        \n  »  **Kegunaan : **Untuk melepaskan pin pesan dalam grup.\
        \n\n  »  **Perintah :** `{cmd}unpin all`\
        \n  »  **Kegunaan : **Untuk melepaskan semua sematan pesan dalam grup.\
    "
    }
)


CMD_HELP.update(
    {
        "undelete": f"**Plugin : **`undelete`\
        \n\n  »  **Perintah :** `{cmd}undlt` <jumlah chat>\
        \n  »  **Kegunaan : **Untuk mendapatkan pesan yang dihapus baru-baru ini di grup\
        \n\n  »  **Perintah :** `{cmd}undlt -u` <jumlah chat>\
        \n  »  **Kegunaan : **Untuk mendapatkan pesan media yang dihapus baru-baru ini di grup \
        \n  •  **Flags :** `-u` = **Gunakan flags ini untuk mengunggah media.**\
        \n\n  •  **NOTE : Membutuhkan Hak admin Grup** \
    "
    }
)


CMD_HELP.update(
    {
        "gmute": f"**Plugin : **`gmute`\
        \n\n  »  **Perintah :** `{cmd}gmute` <username/reply> <alasan (optional)>\
        \n  »  **Kegunaan : **Untuk Membisukan Pengguna di semua grup yang kamu admin.\
        \n\n  »  **Perintah :** `{cmd}ungmute` <username/reply>\
        \n  »  **Kegunaan : **Untuk Membuka global mute Pengguna di semua grup yang kamu admin.\
    "
    }
)


CMD_HELP.update(
    {
        "zombies": f"**Plugin : **`zombies`\
        \n\n  »  **Perintah :** `{cmd}zombies`\
        \n  »  **Kegunaan : **Untuk mencari akun terhapus dalam grup\
        \n\n  »  **Perintah :** `{cmd}zombies clean`\
        \n  »  **Kegunaan : **untuk menghapus Akun Terhapus dari grup.\
    "
    }
)
