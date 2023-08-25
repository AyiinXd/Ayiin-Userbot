# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for filter commands """

from asyncio import sleep
from re import IGNORECASE, escape, search

from AyiinXd import CMD_HELP, Ayiin
from AyiinXd.database.filters import add_filter, del_filter, get_all_filters, update_filter
from AyiinXd.events import ayiin_cmd, register

from . import cmd, var


def check_for_filters(chat_id, trigger):
    all_filters = get_all_filters(chat_id)
    for keywords in all_filters:
        keyword = keywords[1]
        if trigger == keyword:
            return True
    return False


@register(incoming=True, disable_edited=True, disable_errors=True)
async def filter_incoming_handler(handler):
    """Checks if the incoming message contains handler of a filter"""
    try:
        if not (await handler.get_sender()).bot:
            name = handler.raw_text
            filters = get_all_filters(handler.chat_id)
            if not filters:
                return
            for trigger in filters:
                pattern = r"( |^|[^\w])" + \
                    escape(trigger[1]) + r"( |$|[^\w])"
                pro = search(pattern, name, flags=IGNORECASE)
                if pro and trigger[3]:
                    msg_o = await handler.client.get_messages(
                        entity=var.BOTLOG_CHATID, ids=int(trigger[3])
                    )
                    await handler.reply(msg_o.message, file=msg_o.media)
                elif pro and trigger[2]:
                    await handler.reply(trigger[2])
    except AttributeError:
        pass


@Ayiin.on(ayiin_cmd(outgoing=True, pattern=r"filter (.*)"))
async def add_new_filter(new_handler):
    """For .filter command, allows adding new filters in a chat"""
    if new_handler.chat_id in var.BLACKLIST_CHAT:
        return await new_handler.edit(
            "**[ᴋᴏɴᴛᴏʟ]** - Perintah Itu Dilarang Di Group Chat Ini..."
        )
    value = new_handler.pattern_match.group(1).split(None, 1)
    """ - The first words after .filter(space) is the keyword - """
    keyword = value[0]
    try:
        string = value[1]
    except IndexError:
        string = None
    msg = await new_handler.get_reply_message()
    msg_id = None
    if msg and msg.media and not string:
        if var.BOTLOG_CHATID:
            await new_handler.client.send_message(
                var.BOTLOG_CHATID,
                f"**#FILTER\nID OBROLAN:** {new_handler.chat_id}\n**TRIGGER:** `{keyword}`\n\n**Pesan Berikut Disimpan Sebagai Data Balasan Filter Untuk Obrolan, Mohon Jangan Menghapusnya**"
            )
            msg_o = await new_handler.client.forward_messages(
                entity=var.BOTLOG_CHATID,
                messages=msg,
                from_peer=new_handler.chat_id,
                silent=True,
            )
            msg_id = msg_o.id
        else:
            return await new_handler.edit(
                "**Untuk menyimpan media sebagai balasan ke filter** `BOTLOG_CHATID` **harus disetel.**"
            )
    elif new_handler.reply_to_msg_id and not string:
        rep_msg = await new_handler.get_reply_message()
        string = rep_msg.text
    cek = check_for_filters(new_handler.chat_id, keyword)
    if not cek:
        add_filter(str(new_handler.chat_id), keyword, string, msg_id)
        await new_handler.edit(f"**Berhasil Menambahkan Filter** `{keyword}` **Disini**")
    else:
        update_filter(str(new_handler.chat_id), keyword, string, msg_id)
        await new_handler.edit(f"**Berhasil Memperbarui Filter** `{keyword}` **Disini**")


@Ayiin.on(ayiin_cmd(outgoing=True, pattern=r"stop (.*)"))
async def remove_a_filter(r_handler):
    """For .stop command, allows you to remove a filter from a chat."""
    filt = r_handler.pattern_match.group(1)
    cek = check_for_filters(r_handler.chat_id, filt)
    if not cek:
        return await r_handler.edit(f"**Filter** `{filt}` **Tidak Ada Disini**.")
    else:
        del_filter(r_handler.chat_id, filt)
        await r_handler.edit(
            f"**Berhasil Menghapus Filter** `{filt}`"
        )


@Ayiin.on(ayiin_cmd(outgoing=True, pattern=r"delfilterbot (.*)"))
async def kick_marie_filter(event):
    """ For .bersihkanbotfilter command, allows you to kick all \
        Marie(or her clones) filters from a chat. """
    bot_type = event.pattern_match.group(1).lower()
    if bot_type not in ["marie", "rose"]:
        return await event.edit("**Bot Itu Belum Didukung!**")
    await event.edit("`Saya Akan Menghapus Semua Filter!`")
    await sleep(3)
    resp = await event.get_reply_message()
    filters = resp.text.split("-")[1:]
    for i in filters:
        if bot_type.lower() == "marie":
            await event.reply("/stop %s" % (i.strip()))
        if bot_type.lower() == "rose":
            i = i.replace("`", "")
            await event.reply("/stop %s" % (i.strip()))
        await sleep(0.3)
    await event.respond("**Berhasil Menghapus Semua Filter Bot!**")
    if var.BOTLOG_CHATID:
        await event.client.send_message(
            var.BOTLOG_CHATID,
            f"Saya Membersihkan Semua Filter Bot Di `{str(event.chat_id)}`"
        )


@Ayiin.on(ayiin_cmd(outgoing=True, pattern=r"filters$"))
async def filters_active(event):
    """For .filters command, lists all of the active filters in a chat."""
    transact = "**✮ Daftar Filter Yang Aktif Disini:**\n"
    filters = get_all_filters(event.chat_id)
    if filters:
        for filt in filters:
            transact += f" ⍟ `{filt[1]}`\n"
        await event.edit(transact)
    else:
        await event.edit("Tidak Ada Filter Apapun Disini")


CMD_HELP.update(
    {
        "filter": f"**Plugin : **`filter`\
        \n\n  »  **Perintah :** `{cmd}filters`\
        \n  »  **Kegunaan : **Melihat filter userbot yang aktif di obrolan.\
        \n\n  »  **Perintah :** `{cmd}filter` <keyword> <balasan> atau balas ke pesan ketik `{cmd}filter` <keyword>\
        \n  »  **Kegunaan : **Membuat filter di obrolan, Bot Akan Membalas Jika Ada Yang Menyebut 'keyword' yang dibuat. Bisa dipakai ke media/sticker/vn/file.\
        \n\n  »  **Perintah :** `{cmd}stop` <keyword>\
        \n  »  **Kegunaan : **Untuk Nonaktifkan Filter.\
        \n\n  »  **Perintah :** `{cmd}delfilterbot` <marie/rose>\
        \n  »  **Kegunaan : **Menghapus semua filter yang ada di bot grup (Saat ini bot yang didukung: Marie, Rose.) dalam obrolan.\
    "
    }
)
