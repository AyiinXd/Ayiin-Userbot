# Credits: @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import os

import heroku3
from telethon.tl.functions.users import GetFullUserRequest

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import AyiinChanger, ayiin_cmd, eod, eor
from AyiinXd.database.sudoer import add_sudo, del_sudo, sudoer

from . import cmd


@ayiin_cmd(pattern="sudo$")
async def sudo(event):
    listsudo = AyiinChanger(sudoer())
    text = "Daftar sudo\n\n"
    no = 0
    if listsudo:
        for sudo in listsudo:
            no += 1
            text += f"{no}. {sudo}\n"
        await eor(
            event,
            text
        )
    else:
        await eod(event, "🔮 **Sudo:** `Dinonaktifkan`")


@ayiin_cmd(pattern="addsudo(?:\\s|$)([\\s\\S]*)", allow_sudo=False)
async def add(event):
    suu = event.text[9:]
    if f"{cmd}add " in event.text:
        return
    sudo = AyiinChanger(sudoer())
    xxnx = await eor(event, '**Memproses...**')
    var = "SUDO_USERS"
    reply = await event.get_reply_message()
    if not suu and not reply:
        return await eod(
            xxnx,
            "Balas ke pengguna atau berikan user id untuk menambahkannya ke daftar pengguna sudo anda.",
            time=45,
        )
    if suu and not suu.isnumeric():
        return await eod(
            xxnx,
            "Berikan User ID atau reply ke pesan penggunanya.",
            time=45
        )
    if event is None:
        return
    if suu:
        target = suu
    elif reply:
        target = await get_user(event)
    if target in sudo:
        await xxnx.edit("Pengguna sudah ada di database.")
    else:
        add_sudo(target)
        await xxnx.edit(
            f"**Berhasil Menambahkan** `{target}` **ke Pengguna Sudo.**"
        )


@ayiin_cmd(pattern="delsudo(?:\\s|$)([\\s\\S]*)", allow_sudo=False)
async def _(event):
    suu = event.text[8:]
    sudo = AyiinChanger(sudoer())
    xxx = await eor(event, '**Memproses...**')
    reply = await event.get_reply_message()
    if not suu and not reply:
        return await eod(
            xxx, 
            "Balas ke pengguna atau berikan user id untuk menghapusnya dari daftar pengguna sudo Anda.",
            time=45,
        )
    if suu and not suu.isnumeric():
        return await eod(
            xxx,
            "Berikan User ID atau reply ke pesan penggunanya.",
            time=45
        )
    if event is None:
        return
    if suu != "" and suu.isnumeric():
        target = suu
    elif reply:
        target = await get_user(event)
    if target in sudo:
        del_sudo(target)
        await xxx.edit(
            f"**Berhasil Menghapus** `{target}` **dari Pengguna Sudo.**"
        )
    else:
        await eod(
            xxx,
            "**Pengguna ini tidak ada dalam Daftar Pengguna Sudo anda.**",
            time=45
        )


async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    return replied_user.user.id


CMD_HELP.update(
    {
        "sudo": f"**Plugin : **`sudo`\
        \n\n  »  **Perintah :** `{cmd}sudo`\
        \n  »  **Kegunaan : **Untuk Mengecek informasi Sudo.\
        \n\n  »  **Perintah :** `{cmd}addsudo` <reply/user id>\
        \n  »  **Kegunaan : **Untuk Menambahkan User ke Pengguna Sudo.\
        \n\n  »  **Perintah :** `{cmd}delsudo` <reply/user id>\
        \n  »  **Kegunaan : **Untuk Menghapus User dari Pengguna Sudo.\
        \n\n  •  **NOTE: Berikan Hak Sudo anda Kepada orang yang anda percayai**\
    "
    }
)
