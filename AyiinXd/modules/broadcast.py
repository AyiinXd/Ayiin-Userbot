# Credit by https://github.com/sandy1709/catuserbot
# Ported by @X_ImFine
# Recode by @mrismanaziz
# @SharingUserbot

from asyncio import sleep

from AyiinXd import CMD_HELP, LOGS
from AyiinXd.ayiin import AyiinChanger, ayiin_cmd, eor, parse_pre
from AyiinXd.database.broadcast import (
    add_broadcast,
    cek_is_braodcast,
    del_broadcast,
)

from . import cmd, var


@ayiin_cmd(pattern=r"sendto ?(.*)")
async def catbroadcast_send(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await eor(
            event,
            "**Ke kategori mana saya harus mengirim pesan ini?**",
            parse_mode=parse_pre
        )
    reply = await event.get_reply_message()
    if not reply:
        return await eor(
            event,
            "**apa yang harus saya kirim ke kategori ini?**",
            parse_mode=parse_pre
        )
    keyword = catinput_str.lower()
    chats = AyiinChanger(cek_is_braodcast(keyword))
    if not chats:
        return await event.edit(
            event,
            f"**Tidak ada kategori dengan nama** `{keyword}` **Silahkan Cek** `{cmd}bclistall`",
            parse_mode=parse_pre,
        )
    catevent = await eor(
        event,
        "**mengirim pesan ini ke semua grup dalam kategori**",
        parse_mode=parse_pre,
    )
    i = 0
    for chat in chats:
        try:
            if int(event.chat_id) == int(chat):
                continue
            await event.client.send_message(int(chat), reply)
            i += 1
        except Exception as e:
            LOGS.info(str(e))
        await sleep(0.5)
    resultext = f"**Pesan dikirim ke** `{i}` **obrolan keluar** `{len(chats)}` **obrolan dalam kategori** `{keyword}`"
    await catevent.edit(resultext)
    if var.BOTLOG_CHATID:
        await event.client.send_message(
            var.BOTLOG_CHATID,
            f"**Sebuah pesan dikirim ke** `{i}` **obrolan keluar** `{len(chats)}` **obrolan dalam kategori** `{keyword}`",
            parse_mode=parse_pre,
        )


@ayiin_cmd(pattern=r"fwdto ?(.*)")
async def catbroadcast_send(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await eor(
            event,
            "**Ke kategori mana saya harus mengirim pesan ini?**",
            parse_mode=parse_pre
        )
    reply = await event.get_reply_message()
    if not reply:
        return await eor(
            event,
            "**apa yang harus saya kirim ke kategori ini?**",
            parse_mode=parse_pre
        )
    keyword = catinput_str.lower()
    chats = AyiinChanger(cek_is_braodcast(keyword))
    if not chats:
        return await eor(
            event,
            f"**Tidak ada kategori dengan nama** `{keyword}` **Silahkan Cek** `{cmd}bclistall`",
            parse_mode=parse_pre,
        )
    catevent = await eor(
        event,
        "**mengirim pesan ini ke semua grup dalam kategori**",
        parse_mode=parse_pre,
    )
    i = 0
    for chat in chats:
        try:
            if int(event.chat_id) == int(chat):
                continue
            await event.client.forward_messages(int(chat), reply)
            i += 1
        except Exception as e:
            LOGS.info(str(e))
        await sleep(0.5)
    resultext = f"**Pesan dikirim ke** `{i}` **obrolan keluar** `{len(chats)}` **obrolan dalam kategori** `{keyword}`"
    await catevent.edit(resultext)
    if var.BOTLOG_CHATID:
        await event.client.send_message(
            var.BOTLOG_CHATID,
            f"**Sebuah pesan dikirim ke** `{i}` **obrolan keluar** `{len(chats)}` **obrolan dalam kategori** `{keyword}`",
            parse_mode=parse_pre,
        )


@ayiin_cmd(pattern=r"addto ?(.*)")
async def catbroadcast_add(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await eor(
            event,
            "Di kategori mana saya harus menambahkan obrolan ini?",
            parse_mode=parse_pre
        )
    keyword = catinput_str.lower()
    check = AyiinChanger(cek_is_braodcast(keyword))
    if event.chat_id in check:
        return await eor(
            event,
            f"Obrolan ini sudah ada dalam kategori ini {keyword}",
            parse_mode=parse_pre,
        )
    add_broadcast(keyword, event.chat_id)
    await eor(
        event,
        f"Obrolan ini Sekarang ditambahkan ke kategori {keyword}",
        parse_mode=parse_pre
    )
    chat = await event.get_chat()
    if var.BOTLOG_CHATID:
        try:
            await event.client.send_message(
                var.BOTLOG_CHATID,
                f"Obrolan {chat.title} ditambahkan ke kategori {keyword}",
                parse_mode=parse_pre,
            )
        except Exception:
            await event.client.send_message(
                var.BOTLOG_CHATID,
                f"Pengguna {chat.first_name} ditambahkan ke kategori {keyword}",
                parse_mode=parse_pre,
            )


@ayiin_cmd(pattern=r"rmfrom ?(.*)")
async def catbroadcast_remove(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await eor(
            event,
            "Dari kategori mana saya harus menghapus obrolan ini",
            parse_mode=parse_pre
        )
    keyword = catinput_str.lower()
    check = AyiinChanger(cek_is_braodcast(keyword))
    if event.chat_id not in check:
        return await eor(
            event,
            f"Obrolan ini tidak ada dalam kategori {keyword}",
            parse_mode=parse_pre
        )
    del_broadcast(keyword, event.chat_id)
    await eor(
        event,
        f"Obrolan ini Sekarang dihapus dari kategori {keyword}",
        parse_mode=parse_pre,
    )
    chat = await event.get_chat()
    if var.BOTLOG_CHATID:
        try:
            await event.client.send_message(
                var.BOTLOG_CHATID,
                f"Obrolan {chat.title} dihapus dari kategori {keyword}",
                parse_mode=parse_pre,
            )
        except Exception:
            await event.client.send_message(
                var.BOTLOG_CHATID,
                f"pengguna {chat.first_name} dihapus dari kategori {keyword}",
                parse_mode=parse_pre,
            )


@ayiin_cmd(pattern=r"bclist ?(.*)")
async def catbroadcast_list(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await event.edit(
            f"Obrolan kategori mana yang harus saya daftarkan?\nCek `{cmd}bclistall`",
            parse_mode=parse_pre,
        )
    keyword = catinput_str.lower()
    chats = AyiinChanger(cek_is_braodcast(keyword))
    if not chats:
        return await event.edit(
            f"Tidak ada kategori dengan nama {keyword}. Cek `{cmd}bclistall`",
            parse_mode=parse_pre,
        )
    catevent = await event.edit(
        f"Fetching info of the category {keyword}",
        parse_mode=parse_pre
    )
    resultlist = f"**kategori `{keyword}` memiliki `{len(chats)}` obrolan dan ini tercantum di bawah ini :**\n\n"
    errorlist = ""
    for chat in chats:
        try:
            chatinfo = await event.client.get_entity(int(chat))
            try:
                if chatinfo.broadcast:
                    resultlist += f" 👉 📢 **Channel** \n  •  **Name : **{chatinfo.title} \n  •  **id : **`{int(chat)}`\n\n"
                else:
                    resultlist += f" 👉 👥 **Group** \n  •  **Name : **{chatinfo.title} \n  •  **id : **`{int(chat)}`\n\n"
            except AttributeError:
                resultlist += f" 👉 👤 **User** \n  •  **Name : **{chatinfo.first_name} \n  •  **id : **`{int(chat)}`\n\n"
        except Exception:
            errorlist += f" 👉 __ID ini {int(chat)} dalam basis data mungkin Anda meninggalkan obrolan/saluran atau mungkin id tidak valid.\nHapus id ini dari database dengan menggunakan perintah ini__ `{cmd}frmfrom {keyword} {int(chat)}` \n\n"
    finaloutput = resultlist + errorlist
    await catevent.edit(finaloutput)



CMD_HELP.update(
    {
        "broadcast": f"**Plugin : **`broadcast`\
        \n\n  »  **Perintah :** `{cmd}sendto` <category_name>\
        \n  »  **Kegunaan : **akan mengirim pesan balasan ke semua obrolan dalam kategori yang diberikan.\
        \n\n  »  **Perintah :** `{cmd}fwdto` <category_name>\
        \n  »  **Kegunaan : **akan meneruskan pesan yang dibalas ke semua obrolan di kategori berikan. \
        \n\n  »  **Perintah :** `{cmd}addto` <category name>\
        \n  »  **Kegunaan : **Ini akan menambahkan obrolan / pengguna / saluran ini ke kategori nama yang diberikan. \
        \n\n  »  **Perintah :** `{cmd}rmfrom` <category name>\
        \n  »  **Kegunaan : **Untuk menghapus Obrolan / pengguna / saluran dari nama kategori yang diberikan. \
        \n\n  »  **Perintah :** `{cmd}bclist` <category_name>\
        \n  »  **Kegunaan : **Akan menampilkan daftar semua obrolan dalam kategori yang diberikan. \
    "
    }
)
