# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

from time import sleep

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, eor
from Stringyins import get_string


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@ayiin_cmd(pattern=r"yins(?: |$)(.*)")
async def _(y):
    ayiin = await eor(y, get_string("yibot_77"))
    sleep(3)
    await ayiin.edit(get_string("yibot_78"))
    sleep(2)
    await ayiin.edit(get_string("yibot_79"))
    sleep(3)
    await ayiin.edit(get_string("yibot_80"))
# Create by myself @AyiinXd


@ayiin_cmd(pattern=r"sayang(?: |$)(.*)")
async def _(i):
    xx = await eor(i, get_string("yibot_81"))
    sleep(3)
    await xx.edit(get_string("yibot_82"))
# Create by myself @AyiinXd


@ayiin_cmd(pattern=r"semangat(?: |$)(.*)")
async def _(n):
    ayiin = await eor(n, get_string("yibot_83"))
    sleep(3)
    await ayiin.edit(get_string("yibot_84"))
    sleep(1)
    await ayiin.edit(get_string("yibot_85"))
# Create by myself @AyiinXd


@ayiin_cmd(pattern=r"mengeluh(?: |$)(.*)")
async def _(s):
    ayiin = await eor(s, get_string("yibot_83"))
    sleep(3)
    await ayiin.edit(get_string("yibot_86"))
    sleep(1)
    await ayiin.edit(get_string("yibot_87"))
# Create by myself @AyiinXd


CMD_HELP.update(
    {
        "yinsubot3": f"**Plugin : **`yinsubot3`\
        \n\n  »  **Perintah :** `{cmd}yins`\
        \n  »  **Kegunaan : **Perkenalan diri Yins\
        \n\n  »  **Perintah :** `{cmd}sayang`\
        \n  »  **Kegunaan : **Bucin\
        \n\n  »  **Perintah :** `{cmd}semangat`\
        \n  »  **Kegunaan : **Memberikan semangat!\
        \n\n  »  **Perintah :** `{cmd}mengeluh`\
        \n  »  **Kegunaan : **Ngeledek\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
