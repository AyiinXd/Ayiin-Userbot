# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for changing your Telegram profile details+ now u can steal personal details of user. """

import os

from telethon.errors import ImageProcessFailedError, PhotoCropSizeSmallError
from telethon.errors.rpcerrorlist import PhotoExtInvalidError, UsernameOccupiedError
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from telethon.tl.functions.photos import (
    DeletePhotosRequest,
    GetUserPhotosRequest,
    UploadProfilePhotoRequest,
)
from telethon.tl.types import (
    Channel,
    Chat,
    InputPhoto,
    MessageMediaPhoto,
    User,
)

from AyiinXd import CMD_HELP, Ayiin
from AyiinXd.ayiin import ayiin_cmd, eod, eor

from . import cmd


@ayiin_cmd(pattern="reserved$")
async def mine(event):
    result = await event.client(GetAdminedPublicChannelsRequest())
    output_str = "".join(
        f"{channel_obj.title}\n@{channel_obj.username}\n\n"
        for channel_obj in result.chats
    )
    await eor(event, output_str)


@ayiin_cmd(pattern="name", allow_sudo=False)
async def update_name(name):
    newname = name.text[6:]
    if " " not in newname:
        firstname = newname
        lastname = ""
    else:
        namesplit = newname.split(" ", 1)
        firstname = namesplit[0]
        lastname = namesplit[1]

    await name.client(UpdateProfileRequest(first_name=firstname, last_name=lastname))
    await eor(name, "```Nama Anda Telah Berhasil Diubah.```")


@ayiin_cmd(pattern="setpfp$", allow_sudo=False)
async def set_profilepic(propic):
    replymsg = await propic.get_reply_message()
    photo = None
    if replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await propic.client.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split("/"):
            photo = await propic.client.download_file(replymsg.media.document)
        else:
            await eod(propic, "**Media Tidak Valid**")

    if photo:
        try:
            await propic.client(
                UploadProfilePhotoRequest(await propic.client.upload_file(photo))
            )
            os.remove(photo)
            await propic.edit("```Foto Profil Anda Telah Berhasil Diubah.```")
        except PhotoCropSizeSmallError:
            await propic.edit("**Gambar Terlalu Kecil**")
        except ImageProcessFailedError:
            await propic.edit("```Kegagalan Terjadi Saat Proses Gambar, Foto Profil Gagal Diubah.```")
        except PhotoExtInvalidError:
            await propic.edit("**Media Tidak Valid**")


@ayiin_cmd(pattern="setbio (.*)", allow_sudo=False)
async def set_biograph(setbio):
    newbio = setbio.pattern_match.group(1)
    await setbio.client(UpdateProfileRequest(about=newbio))
    await eor(setbio, "```Bio Anda Telah Berhasil Diubah.```")


@ayiin_cmd(pattern="username (.*)", allow_sudo=False)
async def update_username(username):
    newusername = username.pattern_match.group(1)
    try:
        await username.client(UpdateUsernameRequest(newusername))
        await eor(username, "```Username Anda Sudah Diubah.```")
    except UsernameOccupiedError:
        await eod(username, "```Mohon Maaf, Username Itu Sudah Ada Yang Menggunakannya.```")


@ayiin_cmd(pattern="count$")
async def count(event):
    u = 0
    g = 0
    c = 0
    bc = 0
    b = 0
    result = ""
    xx = await eor(event, "**Mmeproses...**")
    dialogs = await Ayiin.get_dialogs(limit=None, ignore_migrated=True)
    for d in dialogs:
        currrent_entity = d.entity
        if isinstance(currrent_entity, User):
            if currrent_entity.bot:
                b += 1
            else:
                u += 1
        elif isinstance(currrent_entity, Chat):
            g += 1
        elif isinstance(currrent_entity, Channel):
            if currrent_entity.broadcast:
                bc += 1
            else:
                c += 1
        else:
            print(d)
    result += f"**Pengguna:**\t`{u}`\n"
    result += f"**Grup:**\t`{g}`\n"
    result += f"**Super Grup:**\t`{c}`\n"
    result += f"**Channel:**\t`{bc}`\n"
    result += f"**Bot:**\t`{b}`"
    await xx.edit(result)


@ayiin_cmd(pattern="delpfp", allow_sudo=False)
async def remove_profilepic(delpfp):
    group = delpfp.text[8:]
    if group == "all":
        lim = 0
    elif group.isdigit():
        lim = int(group)
    else:
        lim = 1
    pfplist = await delpfp.client(
        GetUserPhotosRequest(user_id=delpfp.sender_id, offset=0, max_id=0, limit=lim)
    )
    input_photos = [
        InputPhoto(
            id=sep.id,
            access_hash=sep.access_hash,
            file_reference=sep.file_reference,
        )
        for sep in pfplist.photos
    ]
    await delpfp.client(DeletePhotosRequest(id=input_photos))
    await delpfp.edit(f"`Berhasil Menghapus {len(input_photos)} Foto Profil.`")


CMD_HELP.update(
    {
        "profil": f"**Plugin : **`profil`\
        \n\n  »  **Perintah :** `{cmd}username` <username baru>\
        \n  »  **Kegunaan : **Menganti Username Telegram.\
        \n\n  »  **Perintah :** `{cmd}name` <nama depan> atau `{cmd}name` <Nama Depan> <Nama Belakang>\
        \n  »  **Kegunaan : **Menganti Nama Telegram Anda.\
        \n\n  »  **Perintah :** `{cmd}setbio` <bio baru>\
        \n  »  **Kegunaan : **Untuk Mengganti Bio Telegram.\
        \n\n  »  **Perintah :** `{cmd}setpfp`\
        \n  »  **Kegunaan : **Balas Ke Gambar Ketik {cmd}setpfp Untuk Mengganti Foto Profil Telegram.\
        \n\n  »  **Perintah :** `{cmd}delpfp` atau `{cmd}delpfp` <berapa profil>/<all>\
        \n  »  **Kegunaan : **Menghapus Foto Profil Telegram.\
        \n\n  »  **Perintah :** `{cmd}reserved`\
        \n  »  **Kegunaan : **Menunjukkan nama pengguna yang dipesan oleh Anda.\
        \n\n  »  **Perintah :** `{cmd}count`\
        \n  »  **Kegunaan : **Menghitung Grup, Chat, Bot dll.\
    "
    }
)
