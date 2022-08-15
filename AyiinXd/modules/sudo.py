# Credits: @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import os

import heroku3
from telethon.tl.functions.users import GetFullUserRequest

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, HEROKU_API_KEY, HEROKU_APP_NAME, SUDO_HANDLER, SUDO_USERS
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USERS") or ""


@ayiin_cmd(pattern="sudo$")
async def sudo(event):
    sudo = "True" if SUDO_USERS else "False"
    users = sudousers
    listsudo = users.replace(" ", "\n» ")
    if sudo == "True":
        await eor(
            event, get_string("sudo_1").format(listsudo, SUDO_HANDLER)
        )
    else:
        await eod(event, get_string("sudo_2"))


@ayiin_cmd(pattern="addsudo(?:\\s|$)([\\s\\S]*)", allow_sudo=False)
async def add(event):
    suu = event.text[9:]
    if f"{cmd}add " in event.text:
        return
    xxnx = await eor(event, get_string("com_1"))
    var = "SUDO_USERS"
    reply = await event.get_reply_message()
    if not suu and not reply:
        return await eod(
            xxnx, get_string("adsu_1"),
            time=45,
        )
    if suu and not suu.isnumeric():
        return await eod(
            xxnx, get_string("adsu_2"), time=45
        )
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await eod(xxnx, get_string("adsu_3")
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    if suu:
        target = suu
    elif reply:
        target = await get_user(event)
    suudo = f"{sudousers} {target}"
    newsudo = suudo.replace("{", "")
    newsudo = newsudo.replace("}", "")
    await xxnx.edit(get_string("adsu_4").format(target)
    )
    heroku_Config[var] = newsudo


@ayiin_cmd(pattern="delsudo(?:\\s|$)([\\s\\S]*)", allow_sudo=False)
async def _(event):
    suu = event.text[8:]
    xxx = await eor(event, get_string("com_1"))
    reply = await event.get_reply_message()
    if not suu and not reply:
        return await eod(
            xxx, get_string("dlsu_1"),
            time=45,
        )
    if suu and not suu.isnumeric():
        return await eod(
            xxx, get_string("adsu_2"), time=45
        )
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await eod(xxx, get_string("dlsu_2")
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    if suu != "" and suu.isnumeric():
        target = suu
    elif reply:
        target = await get_user(event)
    gett = str(target)
    if gett in sudousers:
        newsudo = sudousers.replace(gett, "")
        await xxx.edit(get_string("dlsu_3").format(target)
        )
        var = "SUDO_USERS"
        heroku_Config[var] = newsudo
    else:
        await eod(xxx, get_string("dlsu_4"), time=45
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
