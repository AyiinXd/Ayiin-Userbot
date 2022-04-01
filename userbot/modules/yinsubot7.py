# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


from time import sleep
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import ayiin_cmd, edit_or_reply


@ayiin_cmd(pattern="cacad(?: |$)(.*)")
async def _(cacad):
    yins = await edit_or_reply(cacad, "**Cacad 😏**")
    sleep(2)
    await yins.edit("**Najis Akunnya Cacad 😂**")
    sleep(1)
    await yins.edit("**Hahahaha Cacad 🤣**")
    sleep(2)
    await yins.edit("**Canda Akun Cacad 😂🤣**")


@ayiin_cmd(pattern="hayo(?: |$)(.*)")
async def _(hylo):
    ayiin = await edit_or_reply(hylo, "**Hayolo 😂**")
    sleep(1)
    await ayiin.edit("**Hayoloo 😂**")
    sleep(1)
    await ayiin.edit("**Hayolooo 😂**")
    sleep(1)
    await ayiin.edit("**Hayoloooo 😂**")
    sleep(3)
    await ayiin.edit("**Hayolooooo 🤣**")
    sleep(2)
    await ayiin.edit("**Haayolooooo 🤣**")
    sleep(2)
    await ayiin.edit("**Botnya Mati Ya?**")
    sleep(2)
    await ayiin.edit("**Botnya Mati Ya? kasiaaaan** 😂")


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "yinsubot7": f"**Plugin : **`yinsubot7`\
        \n\n  •  **Syntax :** `{cmd}cacad`\
        \n  •  **Function :** Coba Sendiri Tod.\
        \n\n  •  **Syntax :** `{cmd}hayolo`\
        \n  •  **Function :** Coba Senditi Tod.\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
