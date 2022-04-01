# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

from datetime import datetime as dt

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, BOTLOG_CHATID
from userbot.events import register
from userbot.utils import ayiin_cmd, edit_or_reply


@ayiin_cmd(pattern="btpm(?: |$)(.*)")
async def listbtpm(list):
    ayiin = await edit_or_reply(list, "`Processing...`")
    if list.pattern_match.group(1):
        text, link = list.pattern_match.group(1).split()
    else:
        await list.edit("**Yang Benerlah Kentod, Biar Bisa Buat List!!!**")
        return

    n_ch = text.replace(".", " ")
    d_form = "%d - %B - %Y"
    user = await list.client.get_me()
    await ayiin.edit(f"**𝙱𝚃𝙿𝙼 𝙲𝙷:** {n_ch}\n"
                     f"**𝚃𝙰𝙽𝙶𝙶𝙰𝙻 : {dt.now().strftime(d_form)}**\n\n"
                     f"**𝙰𝙳𝙼𝙸𝙽 : @{user.username}**\n"
                     f"**𝙲𝙷: {link}**\n"
                     f"**----------------------------------**\n"
                     f"**• 𝟶𝟶.𝟶𝟶 - 𝟶𝟸.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟶𝟸.𝟶𝟶 - 𝟶𝟺.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟶𝟺.𝟶𝟶 - 𝟶𝟼.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟶𝟼.𝟶𝟶 - 𝟶𝟾.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟶𝟾.𝟶𝟶 - 𝟷𝟶.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟷𝟶.𝟶𝟶 - 𝟷𝟸.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**----------------------------------------------**\n"
                     f"**• 𝟷𝟸.𝟶𝟶 - 𝟷𝟺.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟷𝟺.𝟶𝟶 - 𝟷𝟼.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟷𝟼.𝟶𝟶 - 𝟷𝟾.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟷𝟾.𝟶𝟶 - 𝟸𝟶.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟸𝟶.𝟶𝟶 - 𝟸𝟸.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**• 𝟸𝟸.𝟶𝟶 - 𝟶𝟶.𝟶𝟶 : **\n"
                     f"**-𝙰𝙳𝙼𝙸𝙽 : **\n"
                     f"**-----------------------------------------------**\n"
                     f"**❗𝙼𝚊𝚞 𝟸 𝚓𝚊𝚖 𝚕𝚎𝚋𝚒𝚑 𝚋𝚒𝚜𝚊 𝚕𝚊𝚗𝚐𝚜𝚞𝚗𝚐 𝚕𝚒𝚜𝚝**\n"
                     f"**❗𝙺𝚘𝚗𝚝𝚎𝚗 𝚔𝚎𝚎𝚙 𝟷 𝚇 𝟸𝟺 𝚓𝚊𝚖**\n"
                     f"**❗️𝙽𝙾 𝚂𝙷𝙾𝚁𝚃𝙻𝙸𝙽𝙺**")


@register(outgoing=True,
          pattern=r"\$\w*",
          ignore_unsafe=True,
          disable_errors=True)
async def on_btpm(event):
    """ Fbtpm logic. """
    try:
        from userbot.ayiinxd.btpm_ayiin import get_btpm
    except AttributeError:
        return
    name = event.text[1:]
    btpm = get_btpm(name)
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    if btpm and btpm.f_mesg_id:
        msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                ids=int(btpm.f_mesg_id))
        await event.client.send_message(event.chat_id,
                                        msg_o.message,
                                        reply_to=message_id_to_reply,
                                        file=msg_o.media)
        await event.delete()
    elif btpm and btpm.reply:
        await event.client.send_message(event.chat_id,
                                        btpm.reply,
                                        reply_to=message_id_to_reply)
        await event.delete()


@ayiin_cmd(pattern=r"savebt (\w*)")
async def on_btpm_save(event):
    """ For .savebt command, saves btpm for future use. """
    try:
        from userbot.ayiinxd.btpm_ayiin import add_btpm
    except AtrributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return
    keyword = event.pattern_match.group(1)
    string = event.text.partition(keyword)[2]
    msg = await event.get_reply_message()
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID, f"#BTPM\
            \nKEYWORD: {keyword}\
            \n\n**Pesan berikut disimpan sebagai data untuk btpm, JANGAN dihapus!!!**"
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=event.chat_id,
                silent=True)
            msg_id = msg_o.id
        else:
            await event.edit(
                "**Menyimpan list btpm dengan media memerlukan BOTLOG_CHATID untuk disetel.**"
            )
            return
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    success = "**Daftar Btpm {} Disimpan. Gunakan** `${}` **di mana saja untuk menggunakannya**"
    if add_btpm(keyword, string, msg_id) is False:
        await event.edit(success.format("Diperbarui", keyword))
    else:
        await event.edit(success.format("Berhasil", keyword))


@ayiin_cmd(pattern="listbt$")
async def on_btpm_list(event):
    """ For .listbt command, list btpm saved by you. """
    try:
        from userbot.ayiinxd.btpm_ayiin import get_fbtpm
    except AttributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return

    message = "Daftar Btpm yang tersedia :\n\n"
    all_fbtpm = get_fbtpm()
    for lbtpm in all_fbtpm:
        if message == "**Tidak ada daftar btpm yang tersedia saat ini.**":
            message = "Daftar Btpm yang tersedia :\n\n"
            message += f"`${lbtpm.btpm}`\n"
        else:
            message += f"`${lbtpm.btpm}`\n"

    await event.edit(message)


@ayiin_cmd(pattern=r"delbt (\w*)")
async def on_btpm_delete(event):
    """ For .delbt command, deletes a list btpm. """
    try:
        from userbot.ayiinxd.btpm_ayiin import remove_btpm
    except AttributeError:
        await event.edit("`Running on Non-SQL mode!`")
        return
    name = event.pattern_match.group(1)
    if remove_btpm(name) is True:
        await event.edit(f"**Berhasil menghapus daftar btpm:** `{name}`")
    else:
        await event.edit(f"**Tidak dapat menemukan daftar btpm:** `{name}`")


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "btpmayiin": f"**Plugin:** `btpmayiin`\
        \n\n  • **Perintah :** `{cmd}btpm` <nama_ch (TanpaSpasi)> <username ch>\
        \n  •  **Kegunaan :** __Untuk Mendapatkan List Btpm Kosong.__\
        \n\n  • **Perintah :** `{cmd}savebt` <nama_list>\
        \n  •  **Kegunaan :** __Untuk Menyimpan List Btpm, Gunakan Nama Yang Berbeda.__\
        \n\n  • **Perintah :** `{cmd}$`<nama_list>\
        \n  •  **Kegunaan :** __Untuk Mendapatkan List Btpm Yang Tersimpan.__\
        \n\n  • **Perintah :** `{cmd}delbt` <nama_list>\
        \n  •  **Kegunaan :** __Menghapus List Btpm Yang Tersimpan.__\
        \n\n  • **Perintah :** `{cmd}listbt` <nama_list>\
        \n  •  **Kegunaan :** __Untuk Menlihat Semua List Btpm Yang Tersimpan.__\
    "
    }
)
