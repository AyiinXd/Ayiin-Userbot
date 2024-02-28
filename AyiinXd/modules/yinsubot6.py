# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


from time import sleep
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd

from . import cmd


@ayiin_cmd(pattern="cacad(?: |$)(.*)")
async def _(x):
    ayiin = await x.edit("**Cacad 😏**")
    sleep(2)
    await ayiin.edit("**Najis Akunnya Cacad 😂**")
    sleep(1)
    await ayiin.edit("*Hahahaha Cacad 🤣**")
    sleep(2)
    await ayiin.edit("**Canda Akun Cacad 😂🤣**")


@ayiin_cmd(pattern="hayo(?: |$)(.*)")
async def _(d):
    ayiin = await d.reply("**Hayolo 😂**")
    sleep(1)
    await ayiin.edit("**Hayoloo 😭**")
    sleep(1)
    await ayiin.edit("**Hayolooo 😆**")
    sleep(1)
    await ayiin.edit("**Hayoloooo 😭🕺**")
    sleep(3)
    await ayiin.edit("**Hayolooooo 👻**")
    sleep(2)
    await ayiin.edit("**Haayolooooo 🤭**")
    sleep(2)
    await ayiin.edit("**Botnya Mati Ya?**")
    sleep(2)
    await ayiin.edit("**Botnya Mati Ya? kasiaaaan** 😭🤌")


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "yinsubot6": f"**Plugin : **`Ayiin-Userbot`\
        \n\n  »  **Perintah :** `{cmd}cacad`\
        \n  »  **Kegunaan :** Coba Sendiri Tod.\
        \n\n  »  **Perintah :** `{cmd}hayolo`\
        \n  »  **Kegunaan :** Coba Senditi Tod.\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
  )
