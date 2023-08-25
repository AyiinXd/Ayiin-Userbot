# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
""" Userbot module containing userid, chatid and log commands"""

import asyncio
import csv
import random
from datetime import datetime
from math import sqrt
from secrets import choice

from emoji import emojize
from telethon import functions
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import (
    GetFullChannelRequest,
    GetParticipantsRequest,
    InviteToChannelRequest,
)
from telethon.tl.functions.messages import GetFullChatRequest, GetHistoryRequest
from telethon.tl.types import (
    ChannelParticipantAdmin,
    ChannelParticipantsAdmins,
    ChannelParticipantsBots,
    InputPeerUser,
    MessageActionChannelMigrateFrom,
)
from telethon.utils import get_input_location

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import eod, eor
from AyiinXd.events import register
from AyiinXd.modules.yinsping import absen
from AyiinXd.ayiin import ayiin_cmd, get_user_from_event

from . import cmd


@ayiin_cmd(pattern="userid$")
async def useridgetter(target):
    message = await target.get_reply_message()
    if message:
        if not message.forward:
            user_id = message.sender.id
            if message.sender.username:
                name = "@" + message.sender.username
            else:
                name = "**" + message.sender.first_name + "**"
        else:
            user_id = message.forward.sender.id
            if message.forward.sender.username:
                name = "@" + message.forward.sender.username
            else:
                name = "*" + message.forward.sender.first_name + "*"
        await eor(
            target,
            f"**Username:** {name} \n**User ID:** `{user_id}`"
        )


@ayiin_cmd(pattern="link(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await eor(mention, f"[{custom}](tg://user?id={user.id})")
    else:
        tag = (
            user.first_name.replace("\u2060", "")
            if user.first_name else user.username
        )
        await eor(mention, f"[{tag}](tg://user?id={user.id})")


@ayiin_cmd(pattern="bots(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = "**Bot Di Group Ini:** \n"
    input_str = event.pattern_match.group(1)
    to_write_chat = await event.get_input_chat()
    chat = None
    if not input_str:
        chat = to_write_chat
    else:
        mentions = f"Bot Dalam {input_str} Group: \n"
        try:
            chat = await event.client.get_entity(input_str)
        except Exception as e:
            await eor(event, f"**KESALAHAN : **`{str(e)}`")
            return None
    try:
        async for x in event.client.iter_participants(
            chat, filter=ChannelParticipantsBots
        ):
            if isinstance(x.participant, ChannelParticipantAdmin):
                mentions += "\n 👑 [{}](tg://user?id={}) `{}`".format(
                    x.first_name, x.id, x.id)
            else:
                mentions += "\n ⚜️ [{}](tg://user?id={}) `{}`".format(
                    x.first_name, x.id, x.id)
    except Exception as e:
        mentions += " " + str(e) + "\n"
    await eor(event, mentions)


@register(pattern=r"^\.absenall$", own=True)
async def _(event):
    await event.reply(choice(absen))


@ayiin_cmd(pattern="chatinfo(?: |$)(.*)")
async def info(event):
    xx = await eor(event, "`Menganalisa...`")
    chat = await get_chatinfo(event)
    caption = await fetch_info(chat, event)
    try:
        await xx.edit(caption, parse_mode="html")
    except Exception as e:
        print("Exception:", e)
        await xx.edit("**Terjadi Kesalah Yang Tidak Terduga.**")
    return


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except BaseException:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await eor(event, "`Saluran/grup tidak valid`")
            return None
        except ChannelPrivateError:
            await eod(
                event,
                "`Ini adalah saluran / grup pribadi atau saya dilarang dari sana`"
            )
            return None
        except ChannelPublicGroupNaError:
            await eod(event, "`Saluran atau supergrup tidak ada`")
            return None
        except (TypeError, ValueError):
            await eod(event, "`Saluran/grup tidak valid`")
            return None
    return chat_info


async def fetch_info(chat, event):
    chat_obj_info = await event.client.get_entity(chat.full_chat.id)
    broadcast = (
        chat_obj_info.broadcast if hasattr(
            chat_obj_info,
            "broadcast") else False)
    chat_type = "Channel" if broadcast else "Group"
    chat_title = chat_obj_info.title
    warn_emoji = emojize(":warning:")
    try:
        msg_info = await event.client(
            GetHistoryRequest(
                peer=chat_obj_info.id,
                offset_id=0,
                offset_date=datetime(2010, 1, 1),
                add_offset=-1,
                limit=1,
                max_id=0,
                min_id=0,
                hash=0,
            )
        )
    except Exception as e:
        msg_info = None
        print("Exception:", e)
    first_msg_valid = bool(
        msg_info and msg_info.messages and msg_info.messages[0].id == 1
    )
    creator_valid = bool(first_msg_valid and msg_info.users)
    creator_id = msg_info.users[0].id if creator_valid else None
    creator_firstname = (
        msg_info.users[0].first_name
        if creator_valid and msg_info.users[0].first_name is not None
        else "Akun Terhapus"
    )
    creator_username = (
        msg_info.users[0].username
        if creator_valid and msg_info.users[0].username is not None
        else None
    )
    created = msg_info.messages[0].date if first_msg_valid else None
    former_title = (
        msg_info.messages[0].action.title
        if first_msg_valid
        and isinstance(msg_info.messages[0].action, MessageActionChannelMigrateFrom)
        and msg_info.messages[0].action.title != chat_title
        else None
    )
    try:
        dc_id, location = get_input_location(chat.full_chat.chat_photo)
    except Exception as e:
        dc_id = "Unknown"
        str(e)

    description = chat.full_chat.about
    members = (
        chat.full_chat.participants_count
        if hasattr(chat.full_chat, "participants_count")
        else chat_obj_info.participants_count
    )
    admins = (chat.full_chat.admins_count if hasattr(
        chat.full_chat, "admins_count") else None)
    banned_users = (
        chat.full_chat.kicked_count if hasattr(
            chat.full_chat,
            "kicked_count") else None)
    restrcited_users = (
        chat.full_chat.banned_count if hasattr(
            chat.full_chat,
            "banned_count") else None)
    members_online = (
        chat.full_chat.online_count if hasattr(
            chat.full_chat,
            "online_count") else 0)
    group_stickers = (
        chat.full_chat.stickerset.title
        if hasattr(chat.full_chat, "stickerset") and chat.full_chat.stickerset
        else None
    )
    messages_viewable = msg_info.count if msg_info else None
    messages_sent = (
        chat.full_chat.read_inbox_max_id
        if hasattr(chat.full_chat, "read_inbox_max_id")
        else None
    )
    messages_sent_alt = (
        chat.full_chat.read_outbox_max_id
        if hasattr(chat.full_chat, "read_outbox_max_id")
        else None
    )
    exp_count = chat.full_chat.pts if hasattr(chat.full_chat, "pts") else None
    username = chat_obj_info.username if hasattr(
        chat_obj_info, "username") else None
    bots_list = chat.full_chat.bot_info  # this is a list
    bots = 0
    supergroup = (
        "<b>Yes</b>"
        if hasattr(chat_obj_info, "megagroup") and chat_obj_info.megagroup
        else "Tidak"
    )
    slowmode = ("<b>Yes</b>" if hasattr(chat_obj_info, "slowmode_enabled")
                and chat_obj_info.slowmode_enabled else "Tidak")
    slowmode_time = (
        chat.full_chat.slowmode_seconds if hasattr(
            chat_obj_info,
            "slowmode_enabled") and chat_obj_info.slowmode_enabled else None)
    restricted = (
        "<b>Yes</b>"
        if hasattr(chat_obj_info, "restricted") and chat_obj_info.restricted
        else "Tidak"
    )
    verified = (
        "<b>Yes</b>"
        if hasattr(chat_obj_info, "verified") and chat_obj_info.verified
        else "Tidak"
    )
    username = "@{}".format(username) if username else None
    creator_username = "@{}".format(
        creator_username) if creator_username else None

    if admins is None:
        try:
            participants_admins = await event.client(
                GetParticipantsRequest(
                    channel=chat.full_chat.id,
                    filter=ChannelParticipantsAdmins(),
                    offset=0,
                    limit=0,
                    hash=0,
                )
            )
            admins = participants_admins.count if participants_admins else None
        except Exception as e:
            print("Exception:", e)
    if bots_list:
        for _ in bots_list:
            bots += 1

    caption = "<b>INFORMASI OBROLAN:</b>\n"
    caption += f"ID: <code>{chat_obj_info.id}</code>\n"
    if chat_title is not None:
        caption += f"{chat_type} Nama: {chat_title}\n"
    if former_title is not None:  # Meant is the very first title
        caption += f"Nama Lama: {former_title}\n"
    if username is not None:
        caption += f"{chat_type} Type: Publik\n"
        caption += f"Link: {username}\n"
    else:
        caption += f"{chat_type} type: Privasi\n"
    if creator_username is not None:
        caption += f"Pembuat: {creator_username}\n"
    elif creator_valid:
        caption += (
            f'Pembuat: <a href="tg://user?id={creator_id}">{creator_firstname}</a>\n'
        )
    if created is not None:
        caption += f"Informasi Pembuatan: <code>{created.date().strftime('%b %d, %Y')} - {created.time()}</code>\n"
    else:
        caption += f"Informasi Pembuatan: <code>{chat_obj_info.date.date().strftime('%b %d, %Y')} - {chat_obj_info.date.time()}</code> {warn_emoji}\n"
    caption += f"Data Centre ID: {dc_id}\n"
    if exp_count is not None:
        chat_level = int((1 + sqrt(1 + 7 * exp_count / 14)) / 2)
        caption += f"{chat_type} Level: <code>{chat_level}</code>\n"
    if messages_viewable is not None:
        caption += f"Pesan Yang Dapat Dilihat: <code>{messages_viewable}</code>\n"
    if messages_sent:
        caption += f"Pesan Dikirim: <code>{messages_sent}</code>\n"
    elif messages_sent_alt:
        caption += f"Pesan Dikirim: <code>{messages_sent_alt}</code> {warn_emoji}\n"
    if members is not None:
        caption += f"Member: <code>{members}</code>\n"
    if admins is not None:
        caption += f"Admin: <code>{admins}</code>\n"
    if bots_list:
        caption += f"Bot: <code>{bots}</code>\n"
    if members_online:
        caption += f"Sedang Online: <code>{members_online}</code>\n"
    if restrcited_users is not None:
        caption += f"Pengguna Yang Dibatasi: <code>{restrcited_users}</code>\n"
    if banned_users is not None:
        caption += f"Banned Pengguna: <code>{banned_users}</code>\n"
    if group_stickers is not None:
        caption += f'{chat_type} Sticker: <a href="t.me/addstickers/{chat.full_chat.stickerset.short_name}">{group_stickers}</a>\n'
    caption += "\n"
    if not broadcast:
        caption += f"Mode Slow: {slowmode}"
        if (
            hasattr(chat_obj_info, "slowmode_enabled")
            and chat_obj_info.slowmode_enabled
        ):
            caption += f", <code>{slowmode_time}s</code>\n\n"
        else:
            caption += "\n\n"
        caption += f"Supergrup: {supergroup}\n\n"
    if hasattr(chat_obj_info, "Terbatas"):
        caption += f"Terbatas: {restricted}\n"
        if chat_obj_info.restricted:
            caption += f"> Platform: {chat_obj_info.restriction_reason[0].platform}\n"
            caption += f"> Alasan: {chat_obj_info.restriction_reason[0].reason}\n"
            caption += f"> Teks: {chat_obj_info.restriction_reason[0].text}\n\n"
        else:
            caption += "\n"
    if hasattr(chat_obj_info, "scam") and chat_obj_info.scam:
        caption += "Scam: <b>Yes</b>\n\n"
    if hasattr(chat_obj_info, "verified"):
        caption += f"Di Verifikasi Oleh Telegram: {verified}\n\n"
    if description:
        caption += f"Deskripsi: \n<code>{description}</code>\n"
    return caption


@ayiin_cmd(pattern="invite(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await eor(
            event,
            f"`{cmd}invite` pengguna ke grup chat, bukan ke Pesan Pribadi"
        )
    else:
        if not event.is_channel and event.is_group:
            # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
            for user_id in to_add_users.split():
                try:
                    if user_id.isdigit():
                        user_id = int(user_id)
                    await event.client(
                        functions.messages.AddChatUserRequest(
                            chat_id=event.chat_id, user_id=user_id, fwd_limit=1000000
                        )
                    )
                except Exception as e:
                    return await eod(event, f"**KESALAHAN : **`{str(e)}`")
        else:
            # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
            for user_id in to_add_users.split():
                try:
                    if user_id.isdigit():
                        user_id = int(user_id)
                    await event.client(
                        functions.channels.InviteToChannelRequest(
                            channel=event.chat_id, users=[user_id]
                        )
                    )
                except Exception as e:
                    return await eor(event, f"**KESALAHAN : **`{str(e)}`")

        await eod(event, "`Berhasil Diundang`")


# inviteall Ported By @VckyouuBitch
# From Geez - Projects <https://github.com/vckyou/Geez-UserBot>
# Copyright © Team Geez - Project


@ayiin_cmd(pattern="inviteall ?(.*)")
async def get_users(event):
    ayiin_ = event.text[11:]
    chat_ayiin = ayiin_.lower()
    restricted = ["@AyiinChats", "@ayiinchats", "@AyiinChat", "@ayiinchat"]
    if chat_ayiin in restricted:
        await eor(event, "**Anda tidak dapat Mengundang Anggota dari sana.**")
        await event.client.send_message(
            -1001797285258, "**Maaf Telah Mencuri Member dari Sini.**"
        )
        return
    if not ayiin_:
        return await eor(
            event,
            "**Berikan Link Grup Chat untuk menculik membernya**"
        )
    ayiin = await eor(event, f"**Mengundang Member Dari Group {ayiin_}**")
    ayiinuserbot = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await ayiin.edit("**Tidak bisa Menambahkan Member di sini Harap ketik di Grup Chat**")
    s = 0
    f = 0
    error = "None"
    await ayiin.edit("**Terminal Status**\n\n`Sedang Mengumpulkan Pengguna...`")
    async for user in event.client.iter_participants(ayiinuserbot.full_chat.id):
        try:
            await event.client(InviteToChannelRequest(channel=chat, users=[user.id]))
            s += 1
            await ayiin.edit(
                f"**Terminal Berjalan**\n\n• **Menambahkan** `{s}` **orang** \n• **Gagal Menambahkan** `{f}` **orang**\n\n**× Kesalahan Terakhir:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f += 1
    return await ayiin.edit(
        f"**Terminal Selesai** \n\n• **Berhasil Menambahkan** `{s}` **orang** \n• **Gagal Menambahkan** `{f}` **orang**"
    )


# Scraper & Add Member Telegram
# Coded By Abdul <https://github.com/DoellBarr>


@ayiin_cmd(pattern="getmember$")
async def scrapmem(event):
    chat = event.chat_id
    xx = await eor(event, "`Memproses...`")
    members = await event.client.get_participants(chat, aggressive=True)

    with open("members.csv", "w", encoding="UTF-8") as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\n")
        writer.writerow(["user_id", "hash"])
        for member in members:
            writer.writerow([member.id, member.access_hash])
    await xx.edit("**Berhasil Mengumpulkan Member**")


@ayiin_cmd(pattern="addmember$")
async def admem(event):
    xx = await eor(event, "**Proses Menambahkan** `0` **Member**")
    chat = await event.get_chat()
    users = []
    with open("members.csv", encoding="UTF-8") as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {"id": int(row[0]), "hash": int(row[1])}
            users.append(user)
    n = 0
    for user in users:
        n += 1
        if n % 30 == 0:
            await xx.edit(
                f"**Sudah Mencapai 30 anggota, Tunggu Selama** `{900 / 60}` **menit**"
            )
            await asyncio.sleep(900)
        try:
            userin = InputPeerUser(user["id"], user["hash"])
            await event.client(InviteToChannelRequest(chat, [userin]))
            await asyncio.sleep(random.randrange(5, 7))
            await xx.edit(f"**Proses Menambahkan** `{n}` **Member**")
        except TypeError:
            n -= 1
            continue
        except UserAlreadyParticipantError:
            n -= 1
            continue
        except UserPrivacyRestrictedError:
            n -= 1
            continue
        except UserNotMutualContactError:
            n -= 1
            continue


CMD_HELP.update(
    {
        "chat": f"**Plugin : **`chat`\
        \n\n  »  **Perintah :** `{cmd}userid`\
        \n  »  **Kegunaan : **untuk Mengambil ID obrolan saat ini\
        \n\n  »  **Perintah :** `{cmd}getbot`\
        \n  »  **Kegunaan : **Dapatkan List Bot dalam grup chat.\
        \n\n  »  **Perintah :** `{cmd}mutechat`\
        \n  »  **Kegunaan : **membisukan Grup chat (membutuhkan hak admin).\
        \n\n  »  **Perintah :** `{cmd}unmutechat`\
        \n  »  **Kegunaan : **Membuka Grup chat yang dibisukan (membutuhkan hak admin).\
        \n\n  »  **Perintah :** `{cmd}getbot`\
        \n  »  **Kegunaan : **Dapatkan List Bot dalam grup chat.\
        \n\n  »  **Perintah :** `{cmd}chatinfo [opsional: <reply/tag/chat id/invite link>]`\
        \n  »  **Kegunaan : **Mendapatkan info obrolan. Beberapa info mungkin dibatasi karena izin yang hilang.\
    "
    }
)


CMD_HELP.update(
    {
        "invite": f"**Plugin : **`invite`\
        \n\n  »  **Perintah :** `{cmd}invite` <username/user id>\
        \n  »  **Kegunaan : **Untuk Menambahkan/invite pengguna ke group chat.\
        \n\n  »  **Perintah :** `{cmd}inviteall` <username grup yang mau di culik membernya>\
        \n  »  **Kegunaan : **Untuk Menambahkan/invite pengguna dari grup yang ditargetkan ke grup Anda. (ketik perintah `{cmd}inviteall` di gc lu)\
    "
    }
)


CMD_HELP.update(
    {
        "link": f"**Plugin : **`link`\
        \n\n  »  **Perintah :** `{cmd}link` <username/userid> <opsional teks> (atau) Reply pesan {cmd}link <teks opsional>\
        \n  »  **Kegunaan : **Membuat link permanen ke profil pengguna dengan teks ubah sesuaikan opsional.\
        \n  •  **Contoh : **{cmd}link @AyiinXd Ganteng\
    "
    }
)


CMD_HELP.update(
    {
        "scraper": f"**Plugin : **`scraper`\
        \n\n  »  **Perintah :** `{cmd}getmember`\
        \n  »  **Kegunaan : **Untuk Mengumpulkan Anggota dari group chat.\
        \n\n  »  **Perintah :** `{cmd}addmember`\
        \n  »  **Kegunaan : **Untuk Menambahkan Anggota ke group chat.\
        \n\n**Cara Menggunakannya:** \
        \n1. Anda harus melakukan `{cmd}getmember` terlebih dahulu di Grup Chat Orang lain.\
        \n2. Buka Grup Anda dan ketik `{cmd}addmember` untuk menambahkan mereka ke grup Anda.\
    "
    }
)
