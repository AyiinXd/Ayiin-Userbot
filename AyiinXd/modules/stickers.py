# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
import io
import math
import urllib.request
from os import remove
from secrets import choice

import requests
from bs4 import BeautifulSoup as bs
from PIL import Image
from telethon import events
from telethon.errors import PackShortNameOccupiedError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions, types
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import (
    DocumentAttributeFilename,
    DocumentAttributeSticker,
    InputStickerSetID,
    MessageMediaPhoto,
    MessageMediaUnsupported,
)
from telethon.utils import get_input_document

from AyiinXd import CMD_HELP
from AyiinXd import bot
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from AyiinXd.ayiin.misc import animator, create_quotly
from AyiinXd.database.variable import cek_var, get_var, set_var

from . import (
    cmd,
    var
)

custompack = var.S_PACK_NAME
KANGING_STR = [
    "Gua Ijin Maling Sticker Lu Tod...",
    "Ini Sticker Gua Curi Ya Tod Yahaha!",
    "Waw Sticker Lu Bagus Nih Tod...",
    "Ehh, Keren Nih Tod... Gua Ambil Ya...",
    "Sticker Lu Keren Anjing.. Gua Minta Ya~",
]


@ayiin_cmd(pattern="(?:tikel|kang)\\s?(.)?")
async def kang(args):
    user = await args.client.get_me()
    if not user.username:
        user.username = user.first_name
    message = await args.get_reply_message()
    photo = None
    emojibypass = False
    is_video = False
    is_anim = False
    emoji = None

    if not message:
        return await eod(args, "**Silahkan Reply Ke Pesan Media Untuk Mencuri Sticker itu!**")

    if isinstance(message.media, MessageMediaPhoto):
        xx = await eor(args, f"`{choice(KANGING_STR)}`")
        photo = io.BytesIO()
        photo = await args.client.download_media(message.photo, photo)
    elif isinstance(message.media, MessageMediaUnsupported):
        await eod(
            args,
            "**File Tidak Didukung, Silahkan Reply ke Media Foto/GIF !**"
        )
    elif message.file and "image" in message.file.mime_type.split("/"):
        xx = await eor(args, f"`{choice(KANGING_STR)}`")
        photo = io.BytesIO()
        await args.client.download_file(message.media.document, photo)
        if (
            DocumentAttributeFilename(file_name="sticker.webp")
            in message.media.document.attributes
        ):
            emoji = message.media.document.attributes[1].alt
            if emoji != "✨":
                emojibypass = True
    elif message.file and "tgsticker" in message.file.mime_type:
        xx = await eor(args, f"`{choice(KANGING_STR)}`")
        await args.client.download_file(message.media.document, "AnimatedSticker.tgs")
        attributes = message.media.document.attributes
        for attribute in attributes:
            if isinstance(attribute, DocumentAttributeSticker):
                emoji = attribute.alt
        emojibypass = True
        is_anim = True
        photo = 1
    elif message.media.document.mime_type in ["video/mp4", "video/webm"]:
        if message.media.document.mime_type == "video/webm":
            xx = await eor(args, f"`{choice(KANGING_STR)}`")
            await args.client.download_media(message.media.document, "Video.webm")
        else:
            xx = await eor(args, "**Mengunduh...**")
            await animator(message, args, xx)
            await xx.edit(f"`{choice(KANGING_STR)}`")
        is_video = True
        emoji = "✨"
        emojibypass = True
        photo = 1
    else:
        return await eod(
            args,
            "**File Tidak Didukung, Silahkan Reply ke Media Foto/GIF !**"
        )
    if photo:
        splat = args.text.split()
        if not emojibypass:
            emoji = "✨"
        pack = 1
        if len(splat) == 3:
            pack = splat[2]
            emoji = splat[1]
        elif len(splat) == 2:
            if splat[1].isnumeric():
                pack = int(splat[1])
            else:
                emoji = splat[1]

        packname = f"Sticker_u{user.id}_Ke{pack}"
        if custompack is not None:
            packnick = f"{custompack}"
        else:
            f_name = f"@{user.username}" if user.username else user.first_name
            packnick = f"Sticker Pack {f_name}"
        cmd = "/newpack"
        file = io.BytesIO()

        if is_video:
            packname += "_vid"
            packnick += " (Video)"
            cmd = "/newvideo"
        elif is_anim:
            packname += "_anim"
            packnick += " (Animated)"
            cmd = "/newanimated"
        else:
            image = await resize_photo(photo)
            file.name = "sticker.png"
            image.save(file, "PNG")

        response = urllib.request.urlopen(
            urllib.request.Request(f"http://t.me/addstickers/{packname}")
        )
        htmlstr = response.read().decode("utf8").split("\n")

        if (
            "  A <strong>Telegram</strong> user has created the <strong>Sticker&nbsp;Set</strong>."
            not in htmlstr
        ):
            async with args.client.conversation("@Stickers") as conv:
                try:
                    await conv.send_message("/addsticker")
                except YouBlockedUserError:
                    await args.client(UnblockRequest("@Stickers"))
                    await conv.send_message("/addsticker")
                await conv.get_response()
                await args.client.send_read_acknowledge(conv.chat_id)
                await conv.send_message(packname)
                x = await conv.get_response()
                limit = "50" if (is_anim or is_video) else "120"
                while limit in x.text:
                    pack += 1
                    if custompack is not None:
                        packname = f"Sticker_u{user.id}_Ke{pack}"
                        packnick = f"{custompack}"
                    else:
                        f_name = (
                            f"@{user.username}" if user.username else user.first_name)
                        packname = f"Sticker_u{user.id}_Ke{pack}"
                        packnick = f"Sticker Pack {f_name}"
                    await xx.edit(
                        f"`Membuat Sticker Pack Baru {str(pack)} Karena Sticker Pack Sudah Penuh`"
                    )
                    await conv.send_message(packname)
                    x = await conv.get_response()
                    if x.text == "Gagal Memilih Pack.":
                        await conv.send_message(cmd)
                        await conv.get_response()
                        await args.client.send_read_acknowledge(conv.chat_id)
                        await conv.send_message(packnick)
                        await conv.get_response()
                        await args.client.send_read_acknowledge(conv.chat_id)
                        if is_anim:
                            await conv.send_file("AnimatedSticker.tgs")
                            remove("AnimatedSticker.tgs")
                        elif is_video:
                            await conv.send_file("Video.webm")
                            remove("Video.webm")
                        else:
                            file.seek(0)
                            await conv.send_file(file, force_document=True)
                        await conv.get_response()
                        await conv.send_message(emoji)
                        await args.client.send_read_acknowledge(conv.chat_id)
                        await conv.get_response()
                        await conv.send_message("/publish")
                        if is_anim:
                            await conv.get_response()
                            await conv.send_message(f"<{packnick}>")
                        await conv.get_response()
                        await args.client.send_read_acknowledge(conv.chat_id)
                        await conv.send_message("/skip")
                        await args.client.send_read_acknowledge(conv.chat_id)
                        await conv.get_response()
                        await conv.send_message(packname)
                        await args.client.send_read_acknowledge(conv.chat_id)
                        await conv.get_response()
                        await args.client.send_read_acknowledge(conv.chat_id)
                        return await xx.edit(
                            f"""
**Sticker ditambahkan ke pack yang berbeda !
Ini pack yang baru saja dibuat!
Tekan [Sticker Pack](t.me/addstickers/{packname}) Untuk Melihat Sticker Pack**""",
                            parse_mode="md",
                        )
                if is_anim:
                    await conv.send_file("AnimatedSticker.tgs")
                    remove("AnimatedSticker.tgs")
                elif is_video:
                    await conv.send_file("Video.webm")
                    remove("Video.webm")
                else:
                    file.seek(0)
                    await conv.send_file(file, force_document=True)
                rsp = await conv.get_response()
                if "Sorry, the file type is invalid." in rsp.text:
                    return await xx.edit(
                        "**Gagal Menambahkan Sticker, Gunakan @Stickers Bot Untuk Menambahkan Sticker Anda.**"
                    )
                await conv.send_message(emoji)
                await args.client.send_read_acknowledge(conv.chat_id)
                await conv.get_response()
                await conv.send_message("/done")
                await conv.get_response()
                await args.client.send_read_acknowledge(conv.chat_id)
        else:
            await xx.edit("`Membuat Sticker Pack Baru`")
            async with args.client.conversation("@Stickers") as conv:
                try:
                    await conv.send_message(cmd)
                except YouBlockedUserError:
                    await args.client(UnblockRequest("@Stickers"))
                    await conv.send_message(cmd)
                await conv.get_response()
                await args.client.send_read_acknowledge(conv.chat_id)
                await conv.send_message(packnick)
                await conv.get_response()
                await args.client.send_read_acknowledge(conv.chat_id)
                if is_anim:
                    await conv.send_file("AnimatedSticker.tgs")
                    remove("AnimatedSticker.tgs")
                elif is_video:
                    await conv.send_file("Video.webm")
                    remove("Video.webm")
                else:
                    file.seek(0)
                    await conv.send_file(file, force_document=True)
                rsp = await conv.get_response()
                if "Sorry, the file type is invalid." in rsp.text:
                    return await xx.edit(
                        "`Membuat Sticker Pack Baru`"
                    )
                await conv.send_message(emoji)
                await args.client.send_read_acknowledge(conv.chat_id)
                await conv.get_response()
                await conv.send_message("/publish")
                if is_anim:
                    await conv.get_response()
                    await conv.send_message(f"<{packnick}>")
                await conv.get_response()
                await args.client.send_read_acknowledge(conv.chat_id)
                await conv.send_message("/skip")
                await args.client.send_read_acknowledge(conv.chat_id)
                await conv.get_response()
                await conv.send_message(packname)
                await args.client.send_read_acknowledge(conv.chat_id)
                await conv.get_response()
                await args.client.send_read_acknowledge(conv.chat_id)

        await eor(
            args, 
            f"""
**STICKER LU UDAH JADI TOD**

**     ╭✠━━━━❖━━━━✠╮**
**            [AMBIL TOD](t.me/addstickers/{packname})**
**     ╰✠━━━━❖━━━━✠╯**

**Untuk Menggunakan Stickers**
            """,
            parse_mode="md",
        )


async def resize_photo(photo):
    image = Image.open(photo)
    if (image.width and image.height) < 512:
        size1 = image.width
        size2 = image.height
        if size1 > size2:
            scale = 512 / size1
            size1new = 512
            size2new = size2 * scale
        else:
            scale = 512 / size2
            size1new = size1 * scale
            size2new = 512
        size1new = math.floor(size1new)
        size2new = math.floor(size2new)
        sizenew = (size1new, size2new)
        image = image.resize(sizenew)
    else:
        maxsize = (512, 512)
        image.thumbnail(maxsize)

    return image


@ayiin_cmd(pattern="pkang(?:\\s|$)([\\s\\S]*)")
async def _(event):
    xnxx = await eor(event, f"`{choice(KANGING_STR)}`")
    reply = await event.get_reply_message()
    query = event.text[7:]
    AyiinBot = await bot.get_me()
    BOT_USERNAME = AyiinBot.username
    bot_ = BOT_USERNAME
    bot_un = bot_.replace("@", "")
    user = await event.client.get_me()
    OWNER_ID = user.id
    un = f"@{user.username}" if user.username else user.first_name
    un_ = user.username or OWNER_ID
    if not reply:
        return await eod(
            xnxx,
            "**Mohon Balas sticker untuk mencuri semua Sticker Pack itu.**"
        )
    pname = f"{un} Sticker Pack" if query == "" else query
    if reply.media and reply.media.document.mime_type == "image/webp":
        tikel_id = reply.media.document.attributes[1].stickerset.id
        tikel_hash = reply.media.document.attributes[1].stickerset.access_hash
        got_stcr = await event.client(
            functions.messages.GetStickerSetRequest(
                stickerset=types.InputStickerSetID(id=tikel_id, access_hash=tikel_hash)
            )
        )
        stcrs = []
        for sti in got_stcr.documents:
            inp = get_input_document(sti)
            stcrs.append(
                types.InputStickerSetItem(
                    document=inp,
                    emoji=(sti.attributes[1]).alt,
                )
            )
        try:
            get_var("PKANG")
        except BaseException:
            set_var("PKANG", "0")
        x = get_var("PKANG")
        try:
            pack = int(x) + 1
        except BaseException:
            pack = 1
        await xnxx.edit(f"`{choice(KANGING_STR)}`")
        try:
            create_st = await bot(
                functions.stickers.CreateStickerSetRequest(
                    user_id=OWNER_ID,
                    title=pname,
                    short_name=f"Ayiin_{un_}_V{pack}_by_{bot_un}",
                    stickers=stcrs,
                )
            )
            set_var("PKANG", str(pack))
        except PackShortNameOccupiedError:
            await asyncio.sleep(1)
            await xnxx.edit("`Sedang membuat paket sticker baru...`")
            pack += 1
            create_st = await bot(
                functions.stickers.CreateStickerSetRequest(
                    user_id=OWNER_ID,
                    title=pname,
                    short_name=f"Ayiin_{un_}_V{pack}_by_{bot_un}",
                    stickers=stcrs,
                )
            )
            set_var("PKANG", str(pack))
        await xnxx.edit(
            f"**Berhasil Mencuri Sticker Pack Tod,** [Klik Disini](t.me/addstickers/{create_st.set.short_name}) **Untuk Melihat Pack anda**"
        )
    else:
        await xnxx.edit("**Berkas Tidak Didukung. Harap Balas ke stiker saja.**")


@ayiin_cmd(pattern="stickerinfo$")
async def get_pack_info(event):
    if not event.is_reply:
        return await eod(event, "**Mohon Balas Ke Sticker**")

    rep_msg = await event.get_reply_message()
    if not rep_msg.document:
        return await eod(
            event,
            "**Balas ke sticker untuk melihat detail pack**"
        )

    try:
        stickerset_attr = rep_msg.document.attributes[1]
        xx = await eor(event, '**Memproses...**')
    except BaseException:
        return await eod(xx, "**Ini bukan sticker, Mohon balas ke sticker.**")

    if not isinstance(stickerset_attr, DocumentAttributeSticker):
        return await eod(xx, "**Ini bukan sticker, Mohon balas ke sticker.**")

    get_stickerset = await event.client(
        GetStickerSetRequest(
            InputStickerSetID(
                id=stickerset_attr.stickerset.id,
                access_hash=stickerset_attr.stickerset.access_hash,
            )
        )
    )
    pack_emojis = []
    for document_sticker in get_stickerset.packs:
        if document_sticker.emoticon not in pack_emojis:
            pack_emojis.append(document_sticker.emoticon)

    OUTPUT = (
        f"""
➠ **Nama Sticker:** [{get_stickerset.set.title}](http://t.me/addstickers/{get_stickerset.set.short_name})
➠ **Official:** `{get_stickerset.set.official}`
➠ **Arsip:** `{get_stickerset.set.archived}`
➠ **Sticker Dalam Pack:** `{(len(get_stickerset.packs))}`
➠ **Emoji Dalam Pack:** {(' '.join(pack_emojis))}
"""
    )
    await xx.edit(OUTPUT)


@ayiin_cmd(pattern="delsticker ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await eod(event, "**Mohon Reply ke Sticker yang ingin anda Hapus.**")
        return
    reply_message = await event.get_reply_message()
    chat = "@Stickers"
    if reply_message.sender.bot:
        await eod(event, "**Mohon Balas Ke Sticker**")
        return
    xx = await eor(event, '**Memproses...**')
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=429000)
            )
            await conv.send_message("/delsticker")
            await conv.get_response()
            await asyncio.sleep(2)
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await conv.send_message("/delsticker")
            await conv.get_response()
            await asyncio.sleep(2)
            await event.client.forward_messages(chat, reply_message)
            response = await response
        if response.text.startswith(
            "Sorry, I can't do this, it seems that you are not the owner of the relevant pack."
        ):
            await xx.edit("**Maaf, Sepertinya Anda bukan Pemilik Sticker pack ini.**")
        elif response.text.startswith(
            "You don't have any sticker packs yet. You can create one using the /newpack command."
        ):
            await xx.edit("**Anda Tidak Memiliki Stiker untuk di Hapus**")
        elif response.text.startswith("Please send me the sticker."):
            await xx.edit("**Mohon Reply ke Sticker yang ingin anda Hapus.**")
        elif response.text.startswith("Invalid pack selected."):
            await xx.edit("**Maaf Paket yang dipilih tidak valid.**")
        else:
            await xx.edit("**Berhasil Menghapus Stiker.**")


@ayiin_cmd(pattern="editsticker ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await eod(event, "**Mohon Reply ke Sticker dan Berikan emoji.**")
        return
    reply_message = await event.get_reply_message()
    emot = event.pattern_match.group(1)
    if reply_message.sender.bot:
        await eod(event, "**Mohon Balas Ke Sticker**")
        return
    xx = await eor(event, '**Memproses...**')
    if emot == "":
        await xx.edit("**Silahkan Kirimkan Emot Baru.**")
    else:
        chat = "@Stickers"
        async with event.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=429000)
                )
                await conv.send_message("/editsticker")
                await conv.get_response()
                await asyncio.sleep(2)
                await event.client.forward_messages(chat, reply_message)
                await conv.get_response()
                await asyncio.sleep(2)
                await conv.send_message(f"{emot}")
                response = await response
            except YouBlockedUserError:
                await event.client(UnblockRequest(chat))
                await conv.send_message("/editsticker")
                await conv.get_response()
                await asyncio.sleep(2)
                await event.client.forward_messages(chat, reply_message)
                await conv.get_response()
                await asyncio.sleep(2)
                await conv.send_message(f"{emot}")
                response = await response
            if response.text.startswith("Invalid pack selected."):
                await xx.edit("**Maaf Paket yang dipilih tidak valid.**")
            elif response.text.startswith(
                "Please send us an emoji that best describes your sticker."
            ):
                await xx.edit(
                    "**Silahkan Kirimkan emoji yang paling menggambarkan stiker Anda.**"
                )
            else:
                await xx.edit(
                    f"**Berhasil Mengedit Emoji Stiker**\n**Emoji Baru:** {emot}"
                )


@ayiin_cmd(pattern="getsticker$")
async def sticker_to_png(sticker):
    if not sticker.is_reply:
        await eod(sticker, "**Mohon Balas Ke Sticker**")
        return False
    img = await sticker.get_reply_message()
    if not img.document:
        await eod(sticker, "**Maaf , Ini Bukan Sticker**")
        return False
    xx = await eor(sticker, "`Berhasil Mengambil Sticker!`")
    image = io.BytesIO()
    await sticker.client.download_media(img, image)
    image.name = "sticker.png"
    image.seek(0)
    await sticker.client.send_file(
        sticker.chat_id, image, reply_to=img.id, force_document=True
    )
    await xx.delete()


@ayiin_cmd(pattern="stickers ?([\\s\\S]*)")
async def cb_sticker(event):
    query = event.pattern_match.group(1)
    if not query:
        return await eod(event, "**Masukan Nama Sticker Pack!**")
    xx = await eor(event, "**Sedang Mencari...**")
    text = requests.get("https://combot.org/telegram/stickers?q=" + query).text
    soup = bs(text, "lxml")
    results = soup.find_all("div", {"class": "sticker-pack__header"})
    if not results:
        return await eod(xx, "**Tidak Dapat Menemukan Sticker Pack 🥺**")
    reply = f"**Paket Stiker Kata Kunci:**\n {query}\n\n**Hasil:**\n"
    for pack in results:
        if pack.button:
            packtitle = (pack.find("div", "sticker-pack__title")).get_text()
            packlink = (pack.a).get("href")
            reply += f" •  [{packtitle}]({packlink})\n"
    await xx.edit(reply)


@ayiin_cmd(pattern="itos$")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await eod(
            event,
            "Pak ini bukan pesan gambar balas pesan gambar"
        )
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await eod(
            event,
            "Pak, ini bukan gambar"
        )
        return
    chat = "@buildstickerbot"
    xx = await eor(event, '**Memproses...**')
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=164977173)
            )
            msg = await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            msg = await event.client.forward_messages(chat, reply_message)
            response = await response
        if response.text.startswith("Hi!"):
            await xx.edit(
                "Bisakah Anda menonaktifkan pengaturan privasi penerusan Anda untuk selamanya?"
            )
        else:
            await xx.delete()
            await event.client.send_read_acknowledge(conv.chat_id)
            await event.client.send_message(event.chat_id, response.message)
            await event.client.delete_message(event.chat_id, [msg.id, response.id])


@ayiin_cmd(pattern="get$")
async def _(event):
    rep_msg = await event.get_reply_message()
    if not event.is_reply or not rep_msg.sticker:
        return await eod(event, "**Mohon Balas Ke Sticker**")
    xx = await eor(event, "`Mengconvert ke foto...`")
    foto = io.BytesIO()
    foto = await event.client.download_media(rep_msg.sticker, foto)
    im = Image.open(foto).convert("RGB")
    im.save("sticker.png", "png")
    await event.client.send_file(
        event.chat_id,
        "sticker.png",
        reply_to=rep_msg,
    )
    await xx.delete()
    remove("sticker.png")


CMD_HELP.update(
    {
        "stickers": f"**Plugin : **`stickers`\
        \n\n  »  **Perintah :** `{cmd}kang` atau `{cmd}tikel` [emoji]\
        \n  »  **Kegunaan : **Balas .kang Ke Sticker Atau Gambar Untuk Menambahkan Ke Sticker Pack Mu\
        \n\n  »  **Perintah :** `{cmd}kang` [emoji] atau `{cmd}tikel` [emoji]\
        \n  »  **Kegunaan : **Balas {cmd}kang emoji Ke Sticker Atau Gambar Untuk Menambahkan dan costum emoji sticker Ke Pack Mu\
        \n\n  »  **Perintah :** `{cmd}pkang` <nama sticker pack>\
        \n  »  **Kegunaan : **Balas {cmd}pkang Ke Sticker Untuk Mencuri semua sticker pack tersebut\
        \n\n  »  **Perintah :** `{cmd}delsticker` <reply sticker>\
        \n  »  **Kegunaan : **Untuk Menghapus sticker dari Sticker Pack.\
        \n\n  »  **Perintah :** `{cmd}editsticker` <reply sticker> <emoji>\
        \n  »  **Kegunaan : **Untuk Mengedit emoji stiker dengan emoji yang baru.\
        \n\n  »  **Perintah :** `{cmd}stickerinfo`\
        \n  »  **Kegunaan : **Untuk Mendapatkan Informasi Sticker Pack.\
        \n\n  »  **Perintah :** `{cmd}stickers` <nama sticker pack >\
        \n  »  **Kegunaan : **Untuk Mencari Sticker Pack.\
        \n\n  •  **NOTE:** Untuk Membuat Sticker Pack baru Gunakan angka dibelakang `{cmd}kang`\
        \n  •  **CONTOH:** `{cmd}kang 2` untuk membuat dan menyimpan ke sticker pack ke 2\
    "
    }
)


CMD_HELP.update(
    {
        "sticker_v2": f"**Plugin : **`stickers`\
        \n\n  »  **Perintah :** `{cmd}getsticker`\
        \n  »  **Kegunaan : **Balas Ke Stcker Untuk Mendapatkan File 'PNG' Sticker.\
        \n\n  »  **Perintah :** `{cmd}get`\
        \n  »  **Kegunaan : **Balas ke sticker untuk mendapatkan foto sticker\
        \n\n  »  **Perintah :** `{cmd}itos`\
        \n  »  **Kegunaan : **Balas ke foto untuk membuat foto menjadi sticker\
    "
    }
)
