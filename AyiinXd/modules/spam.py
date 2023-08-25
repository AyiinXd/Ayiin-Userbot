# Copyright (C) 2020 Catuserbot <https://github.com/sandy1709/catuserbot>
# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from telethon.tl import functions, types
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.utils import get_display_name

from AyiinXd import CMD_HELP, LOGS
from AyiinXd.database.variable import set_var, get_var
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from AyiinXd.ayiin.tools import media_type

from . import cmd, var


async def unsavegif(event, spammer):
    try:
        await event.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=spammer.media.document.id,
                    access_hash=spammer.media.document.access_hash,
                    file_reference=spammer.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        LOGS.info(f"{e}")


async def spam_function(event, spammer, xnxx, sleeptimem, sleeptimet, DelaySpam=False):
    counter = int(xnxx[0])
    if len(xnxx) == 2:
        spam_message = str(xnxx[1])
        for _ in range(counter):
            if get_var("spamwork") is None:
                return
            if event.reply_to_msg_id:
                await spammer.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and spammer.media:
        for _ in range(counter):
            if get_var("spamwork") is None:
                return
            spammer = await event.client.send_file(
                event.chat_id, spammer, caption=spammer.text
            )
            await unsavegif(event, spammer)
            await asyncio.sleep(sleeptimem)
        if var.BOTLOG_CHATID:
            if DelaySpam is not True:
                if event.is_private:
                    await event.client.send_message(
                        var.BOTLOG_CHATID, 
                        f"#SPAM\nSpam berhasil dieksekusi di [Pengguna](tg://user?id={event.chat_id}) mengobrol dengan {counter} kali dengan pesan di bawah"
                    )
                else:
                    await event.client.send_message(
                        var.BOTLOG_CHATID,
                        f"#SPAM\nSpam berhasil dieksekusi di {get_display_name(await event.get_chat())}(`{event.chat_id}`) dengan {counter} kali dengan pesan di bawah".format(get_display_name(await event.get_chat()), event.chat_id, counter)
                    )
            elif event.is_private:
                await event.client.send_message(
                    var.BOTLOG_CHATID,
                    f"#DELAYSPAM\nDelay spam berhasil dieksekusi di [Pengguna](tg://user?id={event.chat_id}) mengobrol dengan {counter} kali dengan pesan di bawah ini dengan penundaan {sleeptimet} detik"
                )
            else:
                await event.client.send_message(
                    var.BOTLOG_CHATID,
                    f"#DELAYSPAM\nDelay spam berhasil dieksekusi di {get_display_name(await event.get_chat())}(`{event.chat_id}`) dengan {counter} kali dengan pesan di bawah ini dengan penundaan {sleeptimet} detik"
                )

            spammer = await event.client.send_file(var.BOTLOG_CHATID, spammer)
            await unsavegif(event, spammer)
        return
    elif event.reply_to_msg_id and spammer.text:
        spam_message = spammer.text
        for _ in range(counter):
            if get_var("spamwork") is None:
                return
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    else:
        return
    if DelaySpam is not True:
        if var.BOTLOG_CHATID:
            if event.is_private:
                await event.client.send_message(
                    var.BOTLOG_CHATID,
                    f"#SPAM\nSpam berhasil dieksekusi di [Pengguna](tg://user?id={event.chat_id}) mengobrol dengan {counter} pesan dari \n`{spam_message}`"
                )
            else:
                await event.client.send_message(
                    var.BOTLOG_CHATID, 
                    f"#SPAM\nSpam berhasil dieksekusi di {get_display_name(await event.get_chat())}(`{event.chat_id}`) mengobrol dengan {counter} pesan dari \n`{spam_message}`"
                )
    elif var.BOTLOG_CHATID:
        if event.is_private:
            await event.client.send_message(
                var.BOTLOG_CHATID,
                f"#DELAYSPAM\nDelay Spam berhasil dieksekusi di [Pengguna](tg://user?id={event.chat_id}) mengobrol dengan penundaan {sleeptimet} detik dan dengan {counter} pesan \n`{spam_message}`"
            )
        else:
            await event.client.send_message(
                var.BOTLOG_CHATID,
                f"#DELAYSPAM\nDelay spam berhasil dieksekusi di {get_display_name(await event.get_chat())}(`{event.chat_id}`) mengobrol dengan penundaan {sleeptimet} detik dan dengan {counter} pesan \n`{spam_message}`"
            )


@ayiin_cmd(pattern="spam ([\\s\\S]*)")
async def nyespam(event):
    if event.chat_id in var.BLACKLIST_CHAT:
        return await event.edit("**[ᴋᴏɴᴛᴏʟ]** - Perintah Itu Dilarang Di Group Chat Ini...")
    spammer = await event.get_reply_message()
    xnxx = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    try:
        counter = int(xnxx[0])
    except Exception:
        return await eod(
            event,
            f"**Gunakan sintaks yang tepat untuk spam. Ketik** `{cmd}help spam` **bila butuh bantuan.**"
        )
    if counter > 50:
        sleeptimet = 0.5
        sleeptimem = 1
    else:
        sleeptimet = 0.1
        sleeptimem = 0.3
    await event.delete()
    set_var("spamwork", True)
    await spam_function(event, spammer, xnxx, sleeptimem, sleeptimet)


@ayiin_cmd(pattern="sspam$")
async def stickerpack_spam(event):
    if event.chat_id in var.BLACKLIST_CHAT:
        return await event.edit("**[ᴋᴏɴᴛᴏʟ]** - Perintah Itu Dilarang Di Group Chat Ini...")
    reply = await event.get_reply_message()
    if not reply or media_type(
            reply) is None or media_type(reply) != "Sticker":
        return await eod(
            event,
            "**Balas stiker apa pun untuk mengirim semua stiker dalam paket itu**"
        )
    try:
        stickerset_attr = reply.document.attributes[1]
        xyz = await eor(event, "`Mengambil detail Sticker Pack...`")
    except BaseException:
        await eod(event, "**Ini bukan stiker. Silahkan Reply ke stiker.")
        return
    try:
        get_stickerset = await event.client(
            GetStickerSetRequest(
                types.InputStickerSetID(
                    id=stickerset_attr.stickerset.id,
                    access_hash=stickerset_attr.stickerset.access_hash,
                )
            )
        )
    except Exception:
        return await eod(
            xyz,
            "**Stiker ini bukan bagian dari sticker pack mana pun jadi saya tidak bisa kang paket stiker ini coba kang untuk stiker ini**"
        )
    reqd_sticker_set = await event.client(
        functions.messages.GetStickerSetRequest(
            stickerset=types.InputStickerSetShortName(
                short_name=f"{get_stickerset.set.short_name}"
            )
        )
    )
    set_var("spamwork", True)
    for m in reqd_sticker_set.documents:
        if get_var("spamwork") is None:
            return
        await event.client.send_file(event.chat_id, m)
        await asyncio.sleep(0.7)
    if var.BOTLOG_CHATID:
        if event.is_private:
            await event.client.send_message(
                var.BOTLOG_CHATID,
                f"#STICKERPACK_SPAM\nSticker Pack Spam berhasil dieksekusi di [Pengguna](tg://user?id={event.chat_id}) mengobrol dengan paket "
            )
        else:
            await event.client.send_message(
                var.BOTLOG_CHATID,
                f"#STICKERPACK_SPAM\nSticker Pack Spam berhasil dieksekusi di {get_display_name(await event.get_chat())}(`{event.chat_id}`) mengobrol dengan paket"
            )
        await event.client.send_file(var.BOTLOG_CHATID, reqd_sticker_set.documents[0])


@ayiin_cmd(pattern="cspam ([\\s\\S]*)")
async def tmeme(event):
    if event.chat_id in var.BLACKLIST_CHAT:
        return await event.edit("**[ᴋᴏɴᴛᴏʟ]** - Perintah Itu Dilarang Di Group Chat Ini...")
    cspam = str("".join(event.text.split(maxsplit=1)[1:]))
    message = cspam.replace(" ", "")
    await event.delete()
    set_var("spamwork", True)
    for letter in message:
        if get_var("spamwork") is None:
            return
        await event.respond(letter)
    if var.BOTLOG_CHATID:
        if event.is_private:
            await event.client.send_message(
                var.BOTLOG_CHATID,
                f"#CSPAM\nSpam Surat berhasil dieksekusi di [Pengguna](tg://user?id={event.chat_id}) chat dengan : `{message}`"
            )
        else:
            await event.client.send_message(
                var.BOTLOG_CHATID,
                f"#CSPAM\nSpam Surat berhasil dieksekusi di {get_display_name(await event.get_chat())}(`{event.chat_id}`) chat dengan : `{message}`"
            )


@ayiin_cmd(pattern="wspam ([\\s\\S]*)")
async def tmeme(event):
    if event.chat_id in var.BLACKLIST_CHAT:
        return await event.edit("**[ᴋᴏɴᴛᴏʟ]** - Perintah Itu Dilarang Di Group Chat Ini...")
    wspam = str("".join(event.text.split(maxsplit=1)[1:]))
    message = wspam.split()
    await event.delete()
    set_var("spamwork", True)
    for word in message:
        if get_var("spamwork") is None:
            return
        await event.respond(word)
    if var.BOTLOG_CHATID:
        if event.is_private:
            await event.client.send_message(
                var.BOTLOG_CHATID,
                f"#WSPAM\nWord Spam berhasil dieksekusi di [Pengguna](tg://user?id={event.chat_id}) chat dengan : `{message}`"
            )
        else:
            await event.client.send_message(
                var.BOTLOG_CHATID,
                f"#WSPAM\nWord Spam berhasil dieksekusi di {get_display_name(await event.get_chat())}(`{event.chat_id}`) chat dengan : `{message}`"
            )


@ayiin_cmd(pattern="(delayspam|dspam) ([\\s\\S]*)")
async def dlyspam(event):
    if event.chat_id in var.BLACKLIST_CHAT:
        return await event.edit("**[ᴋᴏɴᴛᴏʟ]** - Perintah Itu Dilarang Di Group Chat Ini...")
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    try:
        sleeptimet = sleeptimem = float(input_str[0])
    except Exception:
        return await eod(
            event,
            f"**Gunakan sintaks yang tepat untuk delayspam. Ketik** `{cmd}help spam` **bila butuh bantuan.**"
        )
    xnxx = input_str[1:]
    try:
        int(xnxx[0])
    except Exception:
        return await eod(
            event,
            f"**Gunakan sintaks yang tepat untuk delayspam. Ketik** `{cmd}help spam` **bila butuh bantuan.**"
        )
    await event.delete()
    set_var("spamwork", True)
    await spam_function(event, reply, xnxx, sleeptimem, sleeptimet, DelaySpam=True)


CMD_HELP.update(
    {
        "spam": f"**Plugin : **`spam`\
        \n\n  »  **Perintah :** `{cmd}spam` <jumlah spam> <text>\
        \n  »  **Kegunaan : **Membanjiri teks dalam obrolan!!\
        \n\n  »  **Perintah :** `{cmd}cspam` <text>\
        \n  »  **Kegunaan : **Spam surat teks dengan huruf.\
        \n\n  »  **Perintah :** `{cmd}sspam` <reply sticker>\
        \n  »  **Kegunaan : **Spam sticker dari Seluruh isi Sticker Pack.\
        \n\n  »  **Perintah :** `{cmd}wspam` <text>\
        \n  »  **Kegunaan : **Spam kata teks demi kata.\
        \n\n  »  **Perintah :** `{cmd}picspam` <jumlah spam> <link image/gif>\
        \n  »  **Kegunaan : **Spam Foto Seolah-olah spam teks tidak cukup !!\
        \n\n  »  **Perintah :** `{cmd}delayspam` <detik> <jumlah spam> <text>\
        \n  »  **Kegunaan : **Spam surat teks dengan huruf.\
        \n\n  •  **NOTE : Spam dengan Risiko Anda sendiri**\
    "
    }
)
