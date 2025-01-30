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

from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd

from . import cmd

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@ayiin_cmd(pattern=r"ayiin(?: |$)(.*)")
async def _(y):
    ayiin = await y.edit("**Hai... Perkenalkan Nama Saya Ayiin**")
    sleep(3)
    await ayiin.edit("**Umur 21 Tahun...**")
    sleep(2)
    await ayiin.edit("**Tinggal Di Bali...**")
    sleep(3)
    await ayiin.edit("**Owner Dari [Ayiin-Userbot](https://github.com/AyiinXd/AyiinXd-Userbot)... Salam Kenal** 😁")
# Create by myself @AyiinXd


@ayiin_cmd(pattern=r"sayang(?: |$)(.*)")
async def _(i):
    xx = await i.edit("**Aku Cuma Mau Bilang...**")
    sleep(3)
    await xx.edit("**Aku Sayang Kamu Mwaahh** 😘❤")
# Create by myself @AyiinXd


@ayiin_cmd(pattern=r"semangat(?: |$)(.*)")
async def _(n):
    ayiin = await n.edit("**Apapun Yang Terjadi...**")
    sleep(3)
    await ayiin.edit("**Tetaplah Bernafas...**")
    sleep(1)
    await ayiin.edit("**Dan Bersyukur...**")
# Create by myself @AyiinXd


@ayiin_cmd(pattern=r"mengeluh(?: |$)(.*)")
async def _(s):
    ayiin = await s.edit("**Apapun Yang Terjadi...**")
    sleep(3)
    await ayiin.edit("**Tetaplah Mengeluh...**")
    sleep(1)
    await ayiin.edit("**Dan Putus Asa...**")
# Create by myself @AyiinXd


CMD_HELP.update(
    {
        "yinsubot3": f"**Plugin : **`Ayiin-Userbot`\
        \n\n  »  **Perintah :** `{cmd}uputt`\
        \n  »  **Kegunaan : **Perkenalan diri Ayiin\
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
