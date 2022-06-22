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

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd import S_PACK_NAME as custompack
from AyiinXd import tgbot
from AyiinXd.modules.sql_helper.globals import addgvar, gvarstatus
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from AyiinXd.ayiin.misc import animator, create_quotly
from Stringyins import get_string

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
        return await eod(args, get_string("stkr_1")
        )

    if isinstance(message.media, MessageMediaPhoto):
        xx = await eor(args, f"`{choice(KANGING_STR)}`")
        photo = io.BytesIO()
        photo = await args.client.download_media(message.photo, photo)
    elif isinstance(message.media, MessageMediaUnsupported):
        await eod(args, get_string("stkr_2")
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
            xx = await eor(args, get_string("com_5"))
            await animator(message, args, xx)
            await xx.edit(f"`{choice(KANGING_STR)}`")
        is_video = True
        emoji = "✨"
        emojibypass = True
        photo = 1
    else:
        return await eod(args, get_string("stkr_2")
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
                    await xx.edit(get_string("stkr_3").format(str(pack))
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
                        return await xx.edit(get_string("stkr_4").format(packname),
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
                    return await xx.edit(get_string("stkr_5")
                    )
                await conv.send_message(emoji)
                await args.client.send_read_acknowledge(conv.chat_id)
                await conv.get_response()
                await conv.send_message("/done")
                await conv.get_response()
                await args.client.send_read_acknowledge(conv.chat_id)
        else:
            await xx.edit(get_string("stkr_6"))
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
                    return await xx.edit(get_string("stkr_6")
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
            get_string("stkr_7").format(packname),
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
    AyiinBot = await tgbot.get_me()
    BOT_USERNAME = AyiinBot.username
    bot_ = BOT_USERNAME
    bot_un = bot_.replace("@", "")
    user = await event.client.get_me()
    OWNER_ID = user.id
    un = f"@{user.username}" if user.username else user.first_name
    un_ = user.username or OWNER_ID
    if not reply:
        return await eod(xnxx, get_string("stkr_8")
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
            gvarstatus("PKANG")
        except BaseException:
            addgvar("PKANG", "0")
        x = gvarstatus("PKANG")
        try:
            pack = int(x) + 1
        except BaseException:
            pack = 1
        await xnxx.edit(f"`{choice(KANGING_STR)}`")
        try:
            create_st = await tgbot(
                functions.stickers.CreateStickerSetRequest(
                    user_id=OWNER_ID,
                    title=pname,
                    short_name=f"Ayiin_{un_}_V{pack}_by_{bot_un}",
                    stickers=stcrs,
                )
            )
            addgvar("PKANG", str(pack))
        except PackShortNameOccupiedError:
            await asyncio.sleep(1)
            await xnxx.edit(get_string("stkr_10"))
            pack += 1
            create_st = await tgbot(
                functions.stickers.CreateStickerSetRequest(
                    user_id=OWNER_ID,
                    title=pname,
                    short_name=f"Ayiin_{un_}_V{pack}_by_{bot_un}",
                    stickers=stcrs,
                )
            )
            addgvar("PKANG", str(pack))
        await xnxx.edit(get_string("stkr_9").format(create_st.set.short_name)
        )
    else:
        await xnxx.edit(get_string("stkr_12"))


@ayiin_cmd(pattern="stickerinfo$")
async def get_pack_info(event):
    if not event.is_reply:
        return await eod(event, get_string("stkr_13"))

    rep_msg = await event.get_reply_message()
    if not rep_msg.document:
        return await eod(
            event, get_string("stkr_14")
        )

    try:
        stickerset_attr = rep_msg.document.attributes[1]
        xx = await eor(event, get_string("com_1"))
    except BaseException:
        return await eod(xx, get_string("stkr_15"))

    if not isinstance(stickerset_attr, DocumentAttributeSticker):
        return await eod(xx, get_string("stkr_15"))

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

    OUTPUT = (get_string("stkr_16").format(get_stickerset.set.title, get_stickerset.set.short_name, get_stickerset.set.official, get_stickerset.set.archived, len(get_stickerset.packs), ' '.join(pack_emojis)))

    await xx.edit(OUTPUT)


@ayiin_cmd(pattern="delsticker ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await eod(event, get_string("delstk_1"))
        return
    reply_message = await event.get_reply_message()
    chat = "@Stickers"
    if reply_message.sender.bot:
        await eod(event, get_string("stkr_13"))
        return
    xx = await eor(event, get_string("com_1"))
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
            await xx.edit(get_string("delstk_2"))
        elif response.text.startswith(
            "You don't have any sticker packs yet. You can create one using the /newpack command."
        ):
            await xx.edit(get_string("delstk_3"))
        elif response.text.startswith("Please send me the sticker."):
            await xx.edit(get_string("delstk_1"))
        elif response.text.startswith("Invalid pack selected."):
            await xx.edit(get_string("delstk_4"))
        else:
            await xx.edit(get_string("delstk_5"))


@ayiin_cmd(pattern="editsticker ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await eod(event, get_string("edtstk_1"))
        return
    reply_message = await event.get_reply_message()
    emot = event.pattern_match.group(1)
    if reply_message.sender.bot:
        await eod(event, get_string("stkr_13"))
        return
    xx = await eor(event, get_string("com_1"))
    if emot == "":
        await xx.edit(get_string("edtstk_2"))
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
                await xx.edit(get_string("delstk_4"))
            elif response.text.startswith(
                "Please send us an emoji that best describes your sticker."
            ):
                await xx.edit(get_string("edtstk_3")
                )
            else:
                await xx.edit(get_string("edtstk_4").format(emot)
                )


@ayiin_cmd(pattern="getsticker$")
async def sticker_to_png(sticker):
    if not sticker.is_reply:
        await eod(sticker, get_string("stkr_13"))
        return False
    img = await sticker.get_reply_message()
    if not img.document:
        await eod(sticker, get_string("getstk_1"))
        return False
    xx = await eor(sticker, get_string("getstk_2"))
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
        return await eod(event, get_string("stk_1"))
    xx = await eor(event, get_string("com_2"))
    text = requests.get("https://combot.org/telegram/stickers?q=" + query).text
    soup = bs(text, "lxml")
    results = soup.find_all("div", {"class": "sticker-pack__header"})
    if not results:
        return await eod(xx, get_string("stk_2"))
    reply = get_string("stk_3").format(query)
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
        await eod(event, get_string("itos_1")
        )
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await eod(event, get_string("itos_2"))
        return
    chat = "@buildstickerbot"
    xx = await eor(event, get_string("com_1"))
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
            await xx.edit(get_string("itos_3")
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
        return await eod(event, get_string("stkr_13"))
    xx = await eor(event, get_string("getst_1"))
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
